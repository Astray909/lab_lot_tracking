import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import simpledialog

def fun_1():
    fahrenheit = entry_1_value.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    entry_1_result["text"] = f"{round(celsius, 2)}"

def fun_2():
    fahrenheit = entry_2_value.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    entry_2_result["text"] = f"{round(celsius, 2)}"

# Set-up the window
window = tk.Tk()
window.title("Lot Tracker")
window.resizable(width=False, height=False)

# MODULE 1
# Create the entry frame with an Entry
# widget and label in it
entry_1 = tk.Frame(master=window)
entry_1_value = tk.Entry(master=entry_1, width=10)
entry_1_init = tk.Label(master=entry_1)

# Layout the Entry and Label in entry_1
# using the .grid() geometry manager
entry_1_value.grid(row=0, column=0, sticky="e")
entry_1_init.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
entry_1_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_1
)
entry_1_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_1.grid(row=0, column=0, padx=10)
entry_1_button.grid(row=0, column=1, pady=10)
entry_1_result.grid(row=0, column=2, padx=10)

# MODULE 2
# Create the entry frame with an Entry
# widget and label in it
entry_2 = tk.Frame(master=window)
entry_2_value = tk.Entry(master=entry_2, width=10)
entry_2_init = tk.Label(master=entry_2)

# Layout the Entry and Label in entry_2
# using the .grid() geometry manager
entry_2_value.grid(row=1, column=0, sticky="e")
entry_2_init.grid(row=1, column=1, sticky="w")

# Create the conversion Button and result display Label
entry_2_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_2_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_2.grid(row=1, column=0, padx=10)
entry_2_button.grid(row=1, column=1, pady=10)
entry_2_result.grid(row=1, column=2, padx=10)

# Run the application
window.mainloop()
