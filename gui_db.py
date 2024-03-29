from datetime import date, time
import time
import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import tkinter.font as tkFont
from PIL import ImageTk,Image 

from tkinter.filedialog import asksaveasfile

import sqlite3, csv

global_fs_state = True

class Database:
    # Builds an empty database if not detected
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY,\
                                                            STATUS text,\
                                                            UID text,\
                                                            YEAR integer,\
                                                            WEEK integer,\
                                                            DEPT text,\
                                                            TESTER text,\
                                                            PROGRAM text,\
                                                            BOX text,\
                                                            PRODUCT text,\
                                                            DATECODE text,\
                                                            LOT text,\
                                                            TEST text,\
                                                            PACKAGE text,\
                                                            HOUR text,\
                                                            STACK_TRAY text,\
                                                            DEVICE_NUM text,\
                                                            QTY integer,\
                                                            RECEIVED_FROM text,\
                                                            WOR_FORM integer,\
                                                            RECEIVED_ORDER_DATE text,\
                                                            TEST_START_DATE text,\
                                                            TOTAL_TIME_CONSUMED text,\
                                                            DATE_OUT text,\
                                                            COMMENTS text,\
                                                            PRINT_LABEL text)")
        self.conn.commit()

    # Fetches all rows containing a certain UID
    def fetch(self, UID=''):
        self.cur.execute(
            "SELECT * FROM entries WHERE UID LIKE ? ORDER BY id DESC", ('%'+UID+'%',))
        rows = self.cur.fetchall()
        return rows

    # Custom SQL query entry, returns all results
    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    # inserts a new row into database
    def insert(self, STATUS, UID, YEAR, WEEK, DEPT, TESTER, PROGRAM, BOX, PRODUCT, DATECODE, LOT, TEST, PACKAGE, HOUR, STACK_TRAY, DEVICE_NUM, QTY, RECEIVED_FROM, WOR_FORM, RECEIVED_ORDER_DATE, TEST_START_DATE, TOTAL_TIME_CONSUMED, DATE_OUT, COMMENTS, PRINT_LABEL):
        self.cur.execute("INSERT INTO entries VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (STATUS, UID, YEAR, WEEK, DEPT, TESTER, PROGRAM, BOX, PRODUCT, DATECODE, LOT, TEST, PACKAGE, HOUR, STACK_TRAY, DEVICE_NUM, QTY, RECEIVED_FROM, WOR_FORM, RECEIVED_ORDER_DATE, TEST_START_DATE, TOTAL_TIME_CONSUMED, DATE_OUT, COMMENTS, PRINT_LABEL))
        self.conn.commit()

    # removes a row with given rowid
    def remove(self, id):
        self.cur.execute("DELETE FROM entries WHERE id=?", (id,))
        self.conn.commit()

    # update a row with given rowid
    def update(self, id, STATUS, UID, YEAR, WEEK, DEPT, TESTER, PROGRAM, BOX, PRODUCT, DATECODE, LOT, TEST, PACKAGE, HOUR, STACK_TRAY, DEVICE_NUM, QTY, RECEIVED_FROM, WOR_FORM, RECEIVED_ORDER_DATE, TEST_START_DATE, TOTAL_TIME_CONSUMED, DATE_OUT, COMMENTS, PRINT_LABEL):
        self.cur.execute("UPDATE entries SET STATUS = ?, UID = ?, YEAR = ?, WEEK = ?, DEPT = ?, TESTER = ?, PROGRAM = ?, BOX = ?, PRODUCT = ?, DATECODE = ?, LOT = ?, TEST = ?, PACKAGE = ?, HOUR = ?, STACK_TRAY = ?, DEVICE_NUM = ?, QTY = ?, RECEIVED_FROM = ?, WOR_FORM = ?, RECEIVED_ORDER_DATE = ?, TEST_START_DATE = ?, TOTAL_TIME_CONSUMED = ?, DATE_OUT = ?, COMMENTS = ?, PRINT_LABEL = ? WHERE id = ?",
                         (STATUS, UID, YEAR, WEEK, DEPT, TESTER, PROGRAM, BOX, PRODUCT, DATECODE, LOT, TEST, PACKAGE, HOUR, STACK_TRAY, DEVICE_NUM, QTY, RECEIVED_FROM, WOR_FORM, RECEIVED_ORDER_DATE, TEST_START_DATE, TOTAL_TIME_CONSUMED, DATE_OUT, COMMENTS, PRINT_LABEL, id))
        # self.cur.execute("SELECT * FROM entries ORDER BY id DESC;")
        self.conn.commit()

    # closes db connection
    def __del__(self):
        self.conn.close()

# points to a db file, can be changed
db = Database("X:\\PLC\\Prod Docs\\Qual\\qrw_script\\dataAnalysis\\dailylist.db")


# displays filtered db in treeview with given UID
def populate_list(UID=''):
    for i in entry_tree_view.get_children():
        entry_tree_view.delete(i)
    for row in db.fetch(UID):
        entry_tree_view.insert('', 'end', values=row)

# displays filtered db in treeview wuth custom query
def populate_list2(query='select * from entries'):
    for i in entry_tree_view.get_children():
        entry_tree_view.delete(i)
    for row in db.fetch2(query):
        entry_tree_view.insert('', 'end', values=row)

# get all entries and populate db
def add_entry():
    create_backup()
    # if STATUS_text.get() == '' or UID_text.get() == '' or YEAR_text.get() == '' or WEEK_text.get() == '' or DEPT_text.get() == '' or TESTER_text.get() == '' or PROGRAM_text.get() == '' or BOX_text.get() == '' or PRODUCT_text.get() == '' or DATECODE_text.get() == '' or LOT_text.get() == '' or TEST_text.get() == '' or PACKAGE_text.get() == '' or HOUR_text.get() == '' or STACK_TRAY_text.get() == '' or DEVICE_NUM_text.get() == '' or QTY_text.get() == '' or RECEIVED_FROM_text.get() == '' or WOR_FORM_text.get() == '' or RECEIVED_ORDER_DATE_text.get() == '' or TEST_START_DATE_text.get() == '' or TOTAL_TIME_CONSUMED_text.get() == '' or DATE_OUT_text.get() == '' or COMMENTS_text.get() == '' or PRINT_LABEL_text.get() == '':
    #     messagebox.showerror('Required Fields', 'Please include all fields')
    #     return
    db.insert(STATUS_text.get(), UID_text.get(), YEAR_text.get(), WEEK_text.get(), DEPT_text.get(), TESTER_text.get(), PROGRAM_text.get(), BOX_text.get(), PRODUCT_text.get(), DATECODE_text.get(), LOT_text.get(), TEST_text.get(), PACKAGE_text.get(), HOUR_text.get(), STACK_TRAY_text.get(), DEVICE_NUM_text.get(), QTY_text.get(), RECEIVED_FROM_text.get(), WOR_FORM_text.get(), RECEIVED_ORDER_DATE_text.get(), TEST_START_DATE_text.get(), TOTAL_TIME_CONSUMED_text.get(), DATE_OUT_text.get(), COMMENTS_text.get(), PRINT_LABEL_text.get())
    clear_text()
    populate_list()
    sort_desc()

# selects a row entry, replaces original entry values with selected row values
def select_entry(event):
    try:
        global selected_item
        index = entry_tree_view.selection()[0]
        selected_item = entry_tree_view.item(index)['values']
        UID_entry.delete(0, END)
        UID_entry.insert(END, selected_item[2])
        YEAR_entry.delete(0, END)
        YEAR_entry.insert(END, selected_item[3])
        WEEK_entry.delete(0, END)
        WEEK_entry.insert(END, selected_item[4])
        DEPT_entry.delete(0, END)
        DEPT_entry.insert(END, selected_item[5])
        TESTER_entry.delete(0, END)
        TESTER_entry.insert(END, selected_item[6])
        PROGRAM_entry.delete(0, END)
        PROGRAM_entry.insert(END, selected_item[7])
        BOX_entry.delete(0, END)
        BOX_entry.insert(END, selected_item[8])
        PRODUCT_entry.delete(0, END)
        PRODUCT_entry.insert(END, selected_item[9])
        DATECODE_entry.delete(0, END)
        DATECODE_entry.insert(END, selected_item[10])
        LOT_entry.delete(0, END)
        LOT_entry.insert(END, selected_item[11])
        TEST_entry.delete(0, END)
        TEST_entry.insert(END, selected_item[12])
        PACKAGE_entry.delete(0, END)
        PACKAGE_entry.insert(END, selected_item[13])
        HOUR_entry.delete(0, END)
        HOUR_entry.insert(END, selected_item[14])
        STACK_TRAY_entry.delete(0, END)
        STACK_TRAY_entry.insert(END, selected_item[15])
        DEVICE_NUM_entry.delete(0, END)
        DEVICE_NUM_entry.insert(END, selected_item[16])
        QTY_entry.delete(0, END)
        QTY_entry.insert(END, selected_item[17])
        RECEIVED_FROM_entry.delete(0, END)
        RECEIVED_FROM_entry.insert(END, selected_item[18])
        WOR_FORM_entry.delete(0, END)
        WOR_FORM_entry.insert(END, selected_item[19])
        RECEIVED_ORDER_DATE_entry.delete(0, END)
        RECEIVED_ORDER_DATE_entry.insert(END, selected_item[20])
        TEST_START_DATE_entry.delete(0, END)
        TEST_START_DATE_entry.insert(END, selected_item[21])
        TOTAL_TIME_CONSUMED_entry.delete(0, END)
        TOTAL_TIME_CONSUMED_entry.insert(END, selected_item[22])
        DATE_OUT_entry.delete(0, END)
        DATE_OUT_entry.insert(END, selected_item[23])
        STATUS_entry.delete(0, END)
        STATUS_entry.insert(END, selected_item[1])
        COMMENTS_entry.delete(0, END)
        COMMENTS_entry.insert(END, selected_item[24])
        PRINT_LABEL_entry.delete(0, END)
        PRINT_LABEL_entry.insert(END, selected_item[25])
    except IndexError:
        pass

# removes a row entry, displays a tkinter confirmation popup
def remove_entry():
    MsgBox = messagebox.askquestion('Remove Entry','Are you sure you want to remove the selected entry?',icon = 'warning')
    if MsgBox == 'yes':
        create_backup()
        db.remove(selected_item[0])
        clear_text()
        populate_list()
        sort_desc()
    else:
        pass

# updates a row entry, displays a tkinter confirmation popup
def update_entry():
    MsgBox = messagebox.askquestion('Update Entry','Are you sure you want to update the selected entry?',icon = 'warning')
    if MsgBox == 'yes':
        create_backup()
        db.update(selected_item[0], STATUS_text.get(), UID_text.get(), YEAR_text.get(), WEEK_text.get(), DEPT_text.get(), TESTER_text.get(), PROGRAM_text.get(), BOX_text.get(), PRODUCT_text.get(), DATECODE_text.get(), LOT_text.get(), TEST_text.get(), PACKAGE_text.get(), HOUR_text.get(), STACK_TRAY_text.get(), DEVICE_NUM_text.get(), QTY_text.get(), RECEIVED_FROM_text.get(), WOR_FORM_text.get(), RECEIVED_ORDER_DATE_text.get(), TEST_START_DATE_text.get(), TOTAL_TIME_CONSUMED_text.get(), DATE_OUT_text.get(), COMMENTS_text.get(), PRINT_LABEL_text.get())
        populate_list()
        sort_desc()
    else:
        pass

# deletes values all entries, does not affect values stored in db
def clear_text():
    UID_entry.delete(0, END)
    YEAR_entry.delete(0, END)
    WEEK_entry.delete(0, END)
    DEPT_entry.delete(0, END)
    TESTER_entry.delete(0, END)
    PROGRAM_entry.delete(0, END)
    BOX_entry.delete(0, END)
    PRODUCT_entry.delete(0, END)
    DATECODE_entry.delete(0, END)
    LOT_entry.delete(0, END)
    TEST_entry.delete(0, END)
    PACKAGE_entry.delete(0, END)
    HOUR_entry.delete(0, END)
    STACK_TRAY_entry.delete(0, END)
    DEVICE_NUM_entry.delete(0, END)
    QTY_entry.delete(0, END)
    RECEIVED_FROM_entry.delete(0, END)
    WOR_FORM_entry.delete(0, END)
    RECEIVED_ORDER_DATE_entry.delete(0, END)
    TEST_START_DATE_entry.delete(0, END)
    TOTAL_TIME_CONSUMED_entry.delete(0, END)
    DATE_OUT_entry.delete(0, END)
    STATUS_entry.delete(0, END)
    COMMENTS_entry.delete(0, END)
    PRINT_LABEL_entry.delete(0, END)

# search by uid
def search_uid():
    UID = UID_search.get()
    populate_list(UID)

# execute custom query
def execute_query():
    query = query_search.get()
    populate_list2(query)

# save search scope as a .csv file, explorer window will default .csv format
def save_csv():
    files = [('CSV File', '*.csv')] #sets default file format
    file = asksaveasfile(filetypes = files, defaultextension = files) #ask user for output directory as well as file name
    file = str(file).replace("<_io.TextIOWrapper name='",'').replace("' mode='w' encoding='cp1252'>",'') #changes encoding format

    # writes searchsope to csv row by row
    with open(str(file), "w", newline='') as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        csvwriter.writerow(['id','STATUS','UID','YEAR','WEEK','DEPT','TESTER','PROGRAM','BOX','PRODUCT','DATECODE','LOT','TEST','PACKAGE','HOUR','STACK_TRAY','DEVICE_NUM','QTY','RECEIVED_FROM','WOR_FORM','RECEIVED_ORDER_DATE','TEST_START_DATE','TOTAL_TIME_CONSUMED','DATE_OUT','COMMENTS','PRINT_LABEL'])
        
        for row_id in entry_tree_view.get_children():
            row = entry_tree_view.item(row_id)['values']
            csvwriter.writerow(row)
    myfile.close()

# automatically populates current date
def today_date():
    today = date.today()
    today_date = today.strftime("%d-%b-%y")
    RECEIVED_ORDER_DATE_entry.delete(0, END)
    RECEIVED_ORDER_DATE_entry.insert(END, today_date)

# reset treeview column widths to default
def reset_width():
    entry_tree_view.column("id", width=32)
    for col in columns[1:]:
        entry_tree_view.column(col, width=72)
        entry_tree_view.heading(col, text=col)

# sort db by id in desc
def sort_desc():
    populate_list2("SELECT * FROM entries ORDER BY id DESC")

def create_backup():
    backup_dirs = get_immediate_subdirectories('X:\\PLC\\Prod Docs\\Qual\\qrw_script\\dataAnalysis\\dailylist_backup')
    if len(backup_dirs) >= 50:
        dirs_to_remove = backup_dirs[:(len(backup_dirs)-49)]
        for dir in dirs_to_remove:
            shutil.rmtree(dir)
    filenames = next(os.walk('X:\\PLC\\Prod Docs\\Qual\\qrw_script\\dataAnalysis\\'), (None, None, []))[2]  # [] if no file
    filenames = [ x for x in filenames if ".db" in x and "dailylist" in x]
    if filenames:
        modTimesinceEpoc = os.path.getmtime('X:\\PLC\\Prod Docs\\Qual\\qrw_script\\dataAnalysis\\' + filenames[0])
        arc_dir_name = '\\' + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(modTimesinceEpoc))

        if not os.path.exists('X:\\PLC\\Prod Docs\\Qual\\qrw_script\\dataAnalysis\\dailylist_backup\\' + arc_dir_name):
            os.makedirs('X:\\PLC\\Prod Docs\\Qual\\qrw_script\\dataAnalysis\\dailylist_backup\\' + arc_dir_name)

        for file in filenames:
            shutil.copy('X:\\PLC\\Prod Docs\\Qual\\qrw_script\\dataAnalysis\\' + file, 'X:\\PLC\\Prod Docs\\Qual\\qrw_script\\dataAnalysis\\dailylist_backup\\' + arc_dir_name)

def get_immediate_subdirectories(a_dir):
    dir_names =  [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
    dir_names = [a_dir + '\\' + name for name in dir_names]
    return dir_names

def restore_backup():
    pass

def enter_fullscreen():
    global global_fs_state
    global_fs_state = not global_fs_state
    app.attributes('-fullscreen', global_fs_state)

# quits script
def destroy():
    app.destroy()

app = Tk()

frame_logo = Frame(app)
frame_logo.grid(row=0, column=0, sticky=W)

img = ImageTk.PhotoImage(Image.open("img\\gan-systems-logo-fc-340x156.png")) #Gan sys logo
gan_logo = Label(frame_logo, image = img) #attach logo img as label
gan_logo.grid(row=0, column=0)

ft = tkFont.Font(family='Times', size=10)
efs_btns = Frame(app)
efs_btns.grid(row=0, column=1, padx=0, sticky=E)

exit_btn = Button(efs_btns, text='QUIT', width=15, height = 5, relief="raised", command=destroy, bg="red", fg="white", font=ft)
exit_btn.grid(row=0, column=2, sticky=W)
fs_btn = Button(efs_btns, text='Toggle Fullscreen', width=15, height = 5, relief="raised", command=enter_fullscreen, bg="green", fg="white", font=ft)
fs_btn.grid(row=0, column=1, sticky=E)
rf_btn = Button(efs_btns, text='Refresh', width=15, height = 5, relief="raised", command=sort_desc, bg="blue", fg="white", font=ft)
rf_btn.grid(row=0, column=0, sticky=E)

frame_search = Frame(app)
frame_search.grid(row=1, column=0)

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
query_search.set("SELECT * FROM entries WHERE YEAR > 2021 ORDER BY id DESC") #default query
query_search_entry = Entry(frame_search, textvariable=query_search, width=70)
query_search_entry.grid(row=1, column=1)

frame_fields = Frame(app)
frame_fields.grid(row=2, column=0)
# UID
UID_text = StringVar()
UID_label = Label(frame_fields, text='UID', font=('bold', 12))
UID_label.grid(row=0, column=0, sticky=E)
UID_entry = Entry(frame_fields, textvariable=UID_text)
UID_entry.grid(row=0, column=1, sticky=W)
# YEAR
YEAR_text = StringVar()
YEAR_label = Label(frame_fields, text='YEAR', font=('bold', 12))
YEAR_label.grid(row=0, column=2, sticky=E)
YEAR_entry = Entry(frame_fields, textvariable=YEAR_text)
YEAR_entry.grid(row=0, column=3, sticky=W)
# WEEK
WEEK_text = StringVar()
WEEK_label = Label(frame_fields, text='WEEK', font=('bold', 12))
WEEK_label.grid(row=0, column=4, sticky=E)
WEEK_entry = Entry(frame_fields, textvariable=WEEK_text)
WEEK_entry.grid(row=0, column=5, sticky=W)
# DEPT
DEPT_text = StringVar()
DEPT_label = Label(frame_fields, text='DEPT', font=('bold', 12))
DEPT_label.grid(row=0, column=6, sticky=E)
DEPT_entry = Entry(frame_fields, textvariable=DEPT_text)
DEPT_entry.grid(row=0, column=7, sticky=W)
# TESTER
TESTER_text = StringVar()
TESTER_label = Label(frame_fields, text='TESTER', font=('bold', 12))
TESTER_label.grid(row=0, column=8, sticky=E)
TESTER_entry = Entry(frame_fields, textvariable=TESTER_text)
TESTER_entry.grid(row=0, column=9, sticky=W)
# PROGRAM
PROGRAM_text = StringVar()
PROGRAM_label = Label(frame_fields, text='PROGRAM', font=('bold', 12))
PROGRAM_label.grid(row=1, column=0, sticky=E)
PROGRAM_entry = Entry(frame_fields, textvariable=PROGRAM_text)
PROGRAM_entry.grid(row=1, column=1, sticky=W)
# BOX
BOX_text = StringVar()
BOX_label = Label(frame_fields, text='BOX', font=('bold', 12))
BOX_label.grid(row=1, column=2, sticky=E)
BOX_entry = Entry(frame_fields, textvariable=BOX_text)
BOX_entry.grid(row=1, column=3, sticky=W)
# PRODUCT
PRODUCT_text = StringVar()
PRODUCT_label = Label(frame_fields, text='PRODUCT', font=('bold', 12))
PRODUCT_label.grid(row=1, column=4, sticky=E)
PRODUCT_entry = Entry(frame_fields, textvariable=PRODUCT_text)
PRODUCT_entry.grid(row=1, column=5, sticky=W)
# DATECODE
DATECODE_text = StringVar()
DATECODE_label = Label(frame_fields, text='DATECODE', font=('bold', 12))
DATECODE_label.grid(row=1, column=6, sticky=E)
DATECODE_entry = Entry(frame_fields, textvariable=DATECODE_text)
DATECODE_entry.grid(row=1, column=7, sticky=W)
# LOT
LOT_text = StringVar()
LOT_label = Label(frame_fields, text='LOT', font=('bold', 12))
LOT_label.grid(row=1, column=8, sticky=E)
LOT_entry = Entry(frame_fields, textvariable=LOT_text)
LOT_entry.grid(row=1, column=9, sticky=W)
# TEST
TEST_text = StringVar()
TEST_label = Label(frame_fields, text='TEST', font=('bold', 12))
TEST_label.grid(row=2, column=0, sticky=E)
TEST_entry = Entry(frame_fields, textvariable=TEST_text)
TEST_entry.grid(row=2, column=1, sticky=W)
# PACKAGE
PACKAGE_text = StringVar()
PACKAGE_label = Label(frame_fields, text='PACKAGE', font=('bold', 12))
PACKAGE_label.grid(row=2, column=2, sticky=E)
PACKAGE_entry = Entry(frame_fields, textvariable=PACKAGE_text)
PACKAGE_entry.grid(row=2, column=3, sticky=W)
# HOUR
HOUR_text = StringVar()
HOUR_label = Label(frame_fields, text='HOUR', font=('bold', 12))
HOUR_label.grid(row=2, column=4, sticky=E)
HOUR_entry = Entry(frame_fields, textvariable=HOUR_text)
HOUR_entry.grid(row=2, column=5, sticky=W)
# STACK_TRAY
STACK_TRAY_text = StringVar()
STACK_TRAY_label = Label(frame_fields, text='STACK_TRAY', font=('bold', 12))
STACK_TRAY_label.grid(row=2, column=6, sticky=E)
STACK_TRAY_entry = Entry(frame_fields, textvariable=STACK_TRAY_text)
STACK_TRAY_entry.grid(row=2, column=7, sticky=W)
# DEVICE_NUM
DEVICE_NUM_text = StringVar()
DEVICE_NUM_label = Label(frame_fields, text='DEVICE_NUM', font=('bold', 12))
DEVICE_NUM_label.grid(row=2, column=8, sticky=E)
DEVICE_NUM_entry = Entry(frame_fields, textvariable=DEVICE_NUM_text)
DEVICE_NUM_entry.grid(row=2, column=9, sticky=W)
# QTY
QTY_text = StringVar()
QTY_label = Label(frame_fields, text='QTY', font=('bold', 12))
QTY_label.grid(row=3, column=0, sticky=E)
QTY_entry = Entry(frame_fields, textvariable=QTY_text)
QTY_entry.grid(row=3, column=1, sticky=W)
# RECEIVED_FROM
RECEIVED_FROM_text = StringVar()
RECEIVED_FROM_label = Label(frame_fields, text='RECEIVED_FROM', font=('bold', 12))
RECEIVED_FROM_label.grid(row=3, column=2, sticky=E)
RECEIVED_FROM_entry = Entry(frame_fields, textvariable=RECEIVED_FROM_text)
RECEIVED_FROM_entry.grid(row=3, column=3, sticky=W)
# WOR_FORM
WOR_FORM_text = StringVar()
WOR_FORM_label = Label(frame_fields, text='WOR_FORM', font=('bold', 12))
WOR_FORM_label.grid(row=3, column=4, sticky=E)
WOR_FORM_entry = Entry(frame_fields, textvariable=WOR_FORM_text)
WOR_FORM_entry.grid(row=3, column=5, sticky=W)
# RECEIVED_ORDER_DATE
RECEIVED_ORDER_DATE_text = StringVar()
RECEIVED_ORDER_DATE_label = Label(frame_fields, text='RECEIVED_ORDER_DATE', font=('bold', 12), bg='orange')
RECEIVED_ORDER_DATE_label.grid(row=3, column=6, sticky=E)
RECEIVED_ORDER_DATE_entry = Entry(frame_fields, textvariable=RECEIVED_ORDER_DATE_text)
RECEIVED_ORDER_DATE_entry.grid(row=3, column=7, sticky=W)
# TEST_START_DATE
TEST_START_DATE_text = StringVar()
TEST_START_DATE_label = Label(frame_fields, text='TEST_START_DATE', font=('bold', 12))
TEST_START_DATE_label.grid(row=3, column=8, sticky=E)
TEST_START_DATE_entry = Entry(frame_fields, textvariable=TEST_START_DATE_text)
TEST_START_DATE_entry.grid(row=3, column=9, sticky=W)
# TOTAL_TIME_CONSUMED
TOTAL_TIME_CONSUMED_text = StringVar()
TOTAL_TIME_CONSUMED_label = Label(frame_fields, text='TOTAL_TIME_CONSUMED', font=('bold', 12))
TOTAL_TIME_CONSUMED_label.grid(row=4, column=0, sticky=E)
TOTAL_TIME_CONSUMED_entry = Entry(frame_fields, textvariable=TOTAL_TIME_CONSUMED_text)
TOTAL_TIME_CONSUMED_entry.grid(row=4, column=1, sticky=W)
# DATE_OUT
DATE_OUT_text = StringVar()
DATE_OUT_label = Label(frame_fields, text='DATE_OUT', font=('bold', 12))
DATE_OUT_label.grid(row=4, column=2, sticky=E)
DATE_OUT_entry = Entry(frame_fields, textvariable=DATE_OUT_text)
DATE_OUT_entry.grid(row=4, column=3, sticky=W)
# STATUS
STATUS_text = StringVar()
STATUS_label = Label(frame_fields, text='STATUS', font=('bold', 12), bg = 'green')
STATUS_label.grid(row=4, column=4, sticky=E)
STATUS_entry = Entry(frame_fields, textvariable=STATUS_text)
STATUS_entry.grid(row=4, column=5, sticky=W)
# COMMENTS
COMMENTS_text = StringVar()
COMMENTS_label = Label(frame_fields, text='COMMENTS', font=('bold', 12))
COMMENTS_label.grid(row=4, column=6, sticky=E)
COMMENTS_entry = Entry(frame_fields, textvariable=COMMENTS_text)
COMMENTS_entry.grid(row=4, column=7, sticky=W)
# PRINT_LABEL
PRINT_LABEL_text = StringVar()
PRINT_LABEL_label = Label(frame_fields, text='PRINT_LABEL', font=('bold', 12))
PRINT_LABEL_label.grid(row=4, column=8, sticky=E)
PRINT_LABEL_entry = Entry(frame_fields, textvariable=PRINT_LABEL_text)
PRINT_LABEL_entry.grid(row=4, column=9, sticky=W)

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
                    width=12, command=search_uid)
search_btn.grid(row=0, column=2)

search_query_btn = Button(frame_search, text='Search Query',
                          width=12, command=execute_query)
search_query_btn.grid(row=1, column=2)

save_csv_btn = Button(frame_btns, text='Save CSV',
                          width=12, command=save_csv)
save_csv_btn.grid(row=0, column=4)

add_date_btn = Button(frame_btns, text="Today's Date",
                          width=12, command=today_date, bg='orange')
add_date_btn.grid(row=0, column=5, padx = 50)

reset_width_btn = Button(frame_btns, text="↓ Reset Column Width ↓",
                          width=19, command=reset_width, bg='yellow')
reset_width_btn.grid(row=0, column=6, padx = 50)

sort_desc_btn = Button(frame_btns, text="↓ Reset all Filters ↓",
                          width=19, command=sort_desc, bg='pink')
sort_desc_btn.grid(row=0, column=7, padx = 50)

frame_entry = Frame(app)
frame_entry.grid(row=4, column=0, columnspan=4, rowspan=10, pady=20, padx=30, sticky=E+W+N+S)
frame_entry.rowconfigure(0, weight=10)

columns = ['id','STATUS','UID','YEAR','WEEK','DEPT','TESTER','PROGRAM','BOX','PRODUCT','DATECODE','LOT','TEST','PACKAGE','HOUR','STACK_TRAY','DEVICE_NUM','QTY','RECEIVED_FROM','WOR_FORM','RECEIVED_ORDER_DATE','TEST_START_DATE','TOTAL_TIME_CONSUMED','DATE_OUT','COMMENTS','PRINT_LABEL']
entry_tree_view = Treeview(frame_entry, columns=columns, show="headings", height=24)
entry_tree_view.grid(row=0, column=0, sticky=E+W+N+S)
entry_tree_view.column("id", width=32)
for col in columns[1:]:
    entry_tree_view.column(col, width=72)
    entry_tree_view.heading(col, text=col)
entry_tree_view.bind('<<TreeviewSelect>>', select_entry)

scrollbar = Scrollbar(frame_entry, orient='vertical')
scrollbar.configure(command=entry_tree_view.yview)
scrollbar.grid(row=0, column=1, sticky=N+S)
entry_tree_view.config(yscrollcommand=scrollbar.set)

x_scrollbar = Scrollbar(frame_entry, orient='horizontal')
x_scrollbar.configure(command=entry_tree_view.xview)
x_scrollbar.grid(row=1, column=0, sticky=E+W)
entry_tree_view.config(xscrollcommand=x_scrollbar.set)

app.title('Test Database')
app.geometry('1920x1030') #default window resolution, change according to target resolution and monitor
app.columnconfigure(0, weight=5)
app.attributes('-fullscreen', global_fs_state) #fullscreen flag, can be changed depending on target resolution and monitor

# Populate data
populate_list()

#Sort from newest to oldest
sort_desc()

# Start program
app.mainloop()
