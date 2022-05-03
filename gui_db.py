from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY,\
                UID text,\
                    Year integer,\
                        Week integer,\
                            Dept text,\
                                TESTER text,\
                                    PROGRAM text)")
        self.conn.commit()

    def fetch(self, UID=''):
        self.cur.execute(
            "SELECT * FROM entries WHERE UID LIKE ?", ('%'+UID+'%',))
        rows = self.cur.fetchall()
        return rows

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insert(self, UID, Year, Week, Dept, TESTER, PROGRAM):
        self.cur.execute("INSERT INTO entries VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                         (UID, Year, Week, Dept, TESTER, PROGRAM))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM entries WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, UID, Year, Week, Dept, TESTER, PROGRAM):
        self.cur.execute("UPDATE entries SET UID = ?, Year = ?, Week = ?, Dept = ?, TESTER = ?, PROGRAM = ? WHERE id = ?",
                         (UID, Year, Week, Dept, TESTER, PROGRAM, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database("file.db")


    
def populate_list(UID=''):
    for i in entry_tree_view.get_children():
        entry_tree_view.delete(i)
    for row in db.fetch(UID):
        entry_tree_view.insert('', 'end', values=row)

def populate_list2(query='select * from entries'):
    for i in entry_tree_view.get_children():
        entry_tree_view.delete(i)
    for row in db.fetch2(query):
        entry_tree_view.insert('', 'end', values=row)

def add_entry():
    if Year_text.get() == '' or UID_text.get() == '' or Week_text.get() == '' or Dept_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(UID_text.get(), Year_text.get(),
              Week_text.get(), Dept_text.get(),
              TESTER_text.get(), PROGRAM_text.get())
    clear_text()
    populate_list()


def select_entry(event):
    try:
        global selected_item
        index = entry_tree_view.selection()[0]
        selected_item = entry_tree_view.item(index)['values']
        UID_entry.delete(0, END)
        UID_entry.insert(END, selected_item[1])
        Year_entry.delete(0, END)
        Year_entry.insert(END, selected_item[2])
        Week_entry.delete(0, END)
        Week_entry.insert(END, selected_item[3])
        Dept_entry.delete(0, END)
        Dept_entry.insert(END, selected_item[4])
        TESTER_entry.delete(0, END)
        TESTER_entry.insert(END, selected_item[5])
        PROGRAM_entry.delete(0, END)
        PROGRAM_entry.insert(END, selected_item[6])
    except IndexError:
        pass

def remove_entry():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_entry():
    db.update(selected_item[0], UID_text.get(), Year_text.get(),
              Week_text.get(), Dept_text.get(), TESTER_text.get(), PROGRAM_text.get())
    populate_list()

def clear_text():
    Year_entry.delete(0, END)
    UID_entry.delete(0, END)
    Week_entry.delete(0, END)
    Dept_entry.delete(0, END)
    TESTER_entry.delete(0, END)
    PROGRAM_entry.delete(0, END)

def search_hostname():
    UID = UID_search.get()
    populate_list(UID)


def execute_query():
    query = query_search.get()
    populate_list2(query)

app = Tk()
frame_search = Frame(app)
frame_search.grid(row=0, column=0)

lbl_search = Label(frame_search, text='Search by UID',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=0, column=0, sticky=W)
UID_search = StringVar()
UID_search_entry = Entry(frame_search, textvariable=UID_search)
UID_search_entry.grid(row=0, column=1)

lbl_search = Label(frame_search, text='Search by Query',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=1, column=0, sticky=W)
query_search = StringVar()
query_search.set("Select * from entries where Year>1")
query_search_entry = Entry(frame_search, textvariable=query_search, width=40)
query_search_entry.grid(row=1, column=1)

frame_fields = Frame(app)
frame_fields.grid(row=1, column=0)
# UID
UID_text = StringVar()
UID_label = Label(frame_fields, text='UID', font=('bold', 12))
UID_label.grid(row=0, column=0, sticky=E)
UID_entry = Entry(frame_fields, textvariable=UID_text)
UID_entry.grid(row=0, column=1, sticky=W)
# Year
Year_text = StringVar()
Year_label = Label(frame_fields, text='Year', font=('bold', 12))
Year_label.grid(row=0, column=2, sticky=E)
Year_entry = Entry(frame_fields, textvariable=Year_text)
Year_entry.grid(row=0, column=3, sticky=W)
# Week
Week_text = StringVar()
Week_label = Label(frame_fields, text='Week', font=('bold', 12))
Week_label.grid(row=1, column=0, sticky=E)
Week_entry = Entry(frame_fields, textvariable=Week_text)
Week_entry.grid(row=1, column=1, sticky=W)
# Dept
Dept_text = StringVar()
Dept_label = Label(frame_fields, text='Dept', font=('bold', 12))
Dept_label.grid(row=1, column=2, sticky=E)
Dept_entry = Entry(frame_fields, textvariable=Dept_text)
Dept_entry.grid(row=1, column=3, sticky=W)
# TESTER
TESTER_text = StringVar()
TESTER_label = Label(frame_fields, text='TESTER', font=('bold', 12))
TESTER_label.grid(row=0, column=4, sticky=E)
TESTER_entry = Entry(frame_fields, textvariable=TESTER_text)
TESTER_entry.grid(row=0, column=5, sticky=W)
# PROGRAM
PROGRAM_text = StringVar()
PROGRAM_label = Label(frame_fields, text='PROGRAM', font=('bold', 12))
PROGRAM_label.grid(row=1, column=4, sticky=E)
PROGRAM_entry = Entry(frame_fields, textvariable=PROGRAM_text)
PROGRAM_entry.grid(row=1, column=5, sticky=W)

frame_entry = Frame(app)
frame_entry.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

columns = ['id', 'UID', 'Year', 'Week', 'Dept', 'TESTER', 'PROGRAM']
entry_tree_view = Treeview(frame_entry, columns=columns, show="headings")
entry_tree_view.column("id", width=30)
for col in columns[1:]:
    entry_tree_view.column(col, width=150)
    entry_tree_view.heading(col, text=col)
entry_tree_view.bind('<<TreeviewSelect>>', select_entry)
entry_tree_view.pack(side="left", fill="y")

scrollbar = Scrollbar(frame_entry, orient='vertical')
scrollbar.configure(command=entry_tree_view.yview)
scrollbar.pack(side="right", fill="y")
entry_tree_view.config(yscrollcommand=scrollbar.set)

scrollbar_x = Scrollbar(frame_entry, orient='horizontal')
scrollbar_x.configure(command=entry_tree_view.xview)
scrollbar_x.pack(side="bottom", fill="x")
entry_tree_view.config(xscrollcommand=scrollbar_x.set)

frame_btns = Frame(app)
frame_btns.grid(row=3, column=0)

add_btn = Button(frame_btns, text='Add Entry', width=12, command=add_entry)
add_btn.grid(row=0, column=0, pady=20)

remove_btn = Button(frame_btns, text='Remove Entry',
                    width=12, command=remove_entry)
remove_btn.grid(row=0, column=1)

update_btn = Button(frame_btns, text='Update Entry',
                    width=12, command=update_entry)
update_btn.grid(row=0, column=2)

clear_btn = Button(frame_btns, text='Clear Input',
                   width=12, command=clear_text)
clear_btn.grid(row=0, column=3)

search_btn = Button(frame_search, text='Search',
                    width=12, command=search_hostname)
search_btn.grid(row=0, column=2)

search_query_btn = Button(frame_search, text='Search Query',
                          width=12, command=execute_query)
search_query_btn.grid(row=1, column=2)

app.title('Test Database')
app.geometry('1280x720')

# Populate data
populate_list()

# Start program
app.mainloop()
