import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import simpledialog

import main as main_cla

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

# MODULE 3
# Create the entry frame with an Entry
# widget and label in it
entry_3 = tk.Frame(master=window)
entry_3_value = tk.Entry(master=entry_3, width=10)
entry_3_init = tk.Label(master=entry_3)

# Layout the Entry and Label in entry_3
# using the .grid() geometry manager
entry_3_value.grid(row=2, column=0, sticky="e")
entry_3_init.grid(row=2, column=1, sticky="w")

# Create the conversion Button and result display Label
entry_3_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_3_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_3.grid(row=2, column=0, padx=10)
entry_3_button.grid(row=2, column=1, pady=10)
entry_3_result.grid(row=2, column=2, padx=10)

# MODULE 4
# Create the entry frame with an Entry
# widget and label in it
entry_4 = tk.Frame(master=window)
entry_4_value = tk.Entry(master=entry_4, width=10)
entry_4_init = tk.Label(master=entry_4)

# Layout the Entry and Label in entry_4
# using the .grid() geometry manager
entry_4_value.grid(row=3, column=0, sticky="e")
entry_4_init.grid(row=3, column=1, sticky="w")

# Create the conversion Button and result display Label
entry_4_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_4_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_4.grid(row=3, column=0, padx=10)
entry_4_button.grid(row=3, column=1, pady=10)
entry_4_result.grid(row=3, column=2, padx=10)

# MODULE 5
# Create the entry frame with an Entry
# widget and label in it
entry_5 = tk.Frame(master=window)
entry_5_value = tk.Entry(master=entry_5, width=10)
entry_5_init = tk.Label(master=entry_5)

# Layout the Entry and Label in entry_5
# using the .grid() geometry manager
entry_5_value.grid(row=4, column=0, sticky="e")
entry_5_init.grid(row=4, column=1, sticky="w")

# Create the conversion Button and result display Label
entry_5_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_5_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_5.grid(row=4, column=0, padx=10)
entry_5_button.grid(row=4, column=1, pady=10)
entry_5_result.grid(row=4, column=2, padx=10)

# MODULE 6
# Create the entry frame with an Entry
# widget and label in it
entry_6 = tk.Frame(master=window)
entry_6_value = tk.Entry(master=entry_6, width=10)
entry_6_init = tk.Label(master=entry_6)

# Layout the Entry and Label in entry_6
# using the .grid() geometry manager
entry_6_value.grid(row=5, column=0, sticky="e")
entry_6_init.grid(row=5, column=1, sticky="w")

# Create the conversion Button and result display Label
entry_6_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_6_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_6.grid(row=5, column=0, padx=10)
entry_6_button.grid(row=5, column=1, pady=10)
entry_6_result.grid(row=5, column=2, padx=10)

# MODULE 7
# Create the entry frame with an Entry
# widget and label in it
entry_7 = tk.Frame(master=window)
entry_7_value = tk.Entry(master=entry_7, width=10)
entry_7_init = tk.Label(master=entry_7)

# Layout the Entry and Label in entry_7
# using the .grid() geometry manager
entry_7_value.grid(row=0, column=3, sticky="e")
entry_7_init.grid(row=0, column=4, sticky="w")

# Create the conversion Button and result display Label
entry_7_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_7_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_7.grid(row=0, column=3, padx=10)
entry_7_button.grid(row=0, column=4, pady=10)
entry_7_result.grid(row=0, column=5, padx=10)

# MODULE 8
# Create the entry frame with an Entry
# widget and label in it
entry_8 = tk.Frame(master=window)
entry_8_value = tk.Entry(master=entry_8, width=10)
entry_8_init = tk.Label(master=entry_8)

# Layout the Entry and Label in entry_8
# using the .grid() geometry manager
entry_8_value.grid(row=1, column=3, sticky="e")
entry_8_init.grid(row=1, column=4, sticky="w")

# Create the conversion Button and result display Label
entry_8_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_8_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_8.grid(row=1, column=3, padx=10)
entry_8_button.grid(row=1, column=4, pady=10)
entry_8_result.grid(row=1, column=5, padx=10)

# MODULE 9
# Create the entry frame with an Entry
# widget and label in it
entry_9 = tk.Frame(master=window)
entry_9_value = tk.Entry(master=entry_9, width=10)
entry_9_init = tk.Label(master=entry_9)

# Layout the Entry and Label in entry_9
# using the .grid() geometry manager
entry_9_value.grid(row=2, column=3, sticky="e")
entry_9_init.grid(row=2, column=4, sticky="w")

# Create the conversion Button and result display Label
entry_9_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_9_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_9.grid(row=2, column=3, padx=10)
entry_9_button.grid(row=2, column=4, pady=10)
entry_9_result.grid(row=2, column=5, padx=10)

# MODULE 10
# Create the entry frame with an Entry
# widget and label in it
entry_10 = tk.Frame(master=window)
entry_10_value = tk.Entry(master=entry_10, width=10)
entry_10_init = tk.Label(master=entry_10)

# Layout the Entry and Label in entry_10
# using the .grid() geometry manager
entry_10_value.grid(row=3, column=3, sticky="e")
entry_10_init.grid(row=3, column=4, sticky="w")

# Create the conversion Button and result display Label
entry_10_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_10_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_10.grid(row=3, column=3, padx=10)
entry_10_button.grid(row=3, column=4, pady=10)
entry_10_result.grid(row=3, column=5, padx=10)

# MODULE 11
# Create the entry frame with an Entry
# widget and label in it
entry_11 = tk.Frame(master=window)
entry_11_value = tk.Entry(master=entry_11, width=10)
entry_11_init = tk.Label(master=entry_11)

# Layout the Entry and Label in entry_11
# using the .grid() geometry manager
entry_11_value.grid(row=4, column=3, sticky="e")
entry_11_init.grid(row=4, column=4, sticky="w")

# Create the conversion Button and result display Label
entry_11_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_11_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_11.grid(row=4, column=3, padx=10)
entry_11_button.grid(row=4, column=4, pady=10)
entry_11_result.grid(row=4, column=5, padx=10)

# MODULE 12
# Create the entry frame with an Entry
# widget and label in it
entry_12 = tk.Frame(master=window)
entry_12_value = tk.Entry(master=entry_12, width=10)
entry_12_init = tk.Label(master=entry_12)

# Layout the Entry and Label in entry_12
# using the .grid() geometry manager
entry_12_value.grid(row=5, column=3, sticky="e")
entry_12_init.grid(row=5, column=4, sticky="w")

# Create the conversion Button and result display Label
entry_12_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_12_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_12.grid(row=5, column=3, padx=10)
entry_12_button.grid(row=5, column=4, pady=10)
entry_12_result.grid(row=5, column=5, padx=10)

# MODULE 13
# Create the entry frame with an Entry
# widget and label in it
entry_13 = tk.Frame(master=window)
entry_13_value = tk.Entry(master=entry_13, width=10)
entry_13_init = tk.Label(master=entry_13)

# Layout the Entry and Label in entry_13
# using the .grid() geometry manager
entry_13_value.grid(row=0, column=6, sticky="e")
entry_13_init.grid(row=0, column=7, sticky="w")

# Create the conversion Button and result display Label
entry_13_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_13_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_13.grid(row=0, column=6, padx=10)
entry_13_button.grid(row=0, column=7, pady=10)
entry_13_result.grid(row=0, column=8, padx=10)

# MODULE 14
# Create the entry frame with an Entry
# widget and label in it
entry_14 = tk.Frame(master=window)
entry_14_value = tk.Entry(master=entry_14, width=10)
entry_14_init = tk.Label(master=entry_14)

# Layout the Entry and Label in entry_14
# using the .grid() geometry manager
entry_14_value.grid(row=1, column=6, sticky="e")
entry_14_init.grid(row=1, column=7, sticky="w")

# Create the conversion Button and result display Label
entry_14_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_14_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_14.grid(row=1, column=6, padx=10)
entry_14_button.grid(row=1, column=7, pady=10)
entry_14_result.grid(row=1, column=8, padx=10)

# MODULE 15
# Create the entry frame with an Entry
# widget and label in it
entry_15 = tk.Frame(master=window)
entry_15_value = tk.Entry(master=entry_15, width=10)
entry_15_init = tk.Label(master=entry_15)

# Layout the Entry and Label in entry_15
# using the .grid() geometry manager
entry_15_value.grid(row=2, column=6, sticky="e")
entry_15_init.grid(row=2, column=7, sticky="w")

# Create the conversion Button and result display Label
entry_15_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_15_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_15.grid(row=2, column=6, padx=10)
entry_15_button.grid(row=2, column=7, pady=10)
entry_15_result.grid(row=2, column=8, padx=10)

# MODULE 16
# Create the entry frame with an Entry
# widget and label in it
entry_16 = tk.Frame(master=window)
entry_16_value = tk.Entry(master=entry_16, width=10)
entry_16_init = tk.Label(master=entry_16)

# Layout the Entry and Label in entry_16
# using the .grid() geometry manager
entry_16_value.grid(row=3, column=6, sticky="e")
entry_16_init.grid(row=3, column=7, sticky="w")

# Create the conversion Button and result display Label
entry_16_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_16_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_16.grid(row=3, column=6, padx=10)
entry_16_button.grid(row=3, column=7, pady=10)
entry_16_result.grid(row=3, column=8, padx=10)

# MODULE 17
# Create the entry frame with an Entry
# widget and label in it
entry_17 = tk.Frame(master=window)
entry_17_value = tk.Entry(master=entry_17, width=10)
entry_17_init = tk.Label(master=entry_17)

# Layout the Entry and Label in entry_17
# using the .grid() geometry manager
entry_17_value.grid(row=4, column=6, sticky="e")
entry_17_init.grid(row=4, column=7, sticky="w")

# Create the conversion Button and result display Label
entry_17_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_17_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_17.grid(row=4, column=6, padx=10)
entry_17_button.grid(row=4, column=7, pady=10)
entry_17_result.grid(row=4, column=8, padx=10)

# MODULE 18
# Create the entry frame with an Entry
# widget and label in it
entry_18 = tk.Frame(master=window)
entry_18_value = tk.Entry(master=entry_18, width=10)
entry_18_init = tk.Label(master=entry_18)

# Layout the Entry and Label in entry_18
# using the .grid() geometry manager
entry_18_value.grid(row=5, column=6, sticky="e")
entry_18_init.grid(row=5, column=7, sticky="w")

# Create the conversion Button and result display Label
entry_18_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_18_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_18.grid(row=5, column=6, padx=10)
entry_18_button.grid(row=5, column=7, pady=10)
entry_18_result.grid(row=5, column=8, padx=10)

# MODULE 19
# Create the entry frame with an Entry
# widget and label in it
entry_19 = tk.Frame(master=window)
entry_19_value = tk.Entry(master=entry_19, width=10)
entry_19_init = tk.Label(master=entry_19)

# Layout the Entry and Label in entry_19
# using the .grid() geometry manager
entry_19_value.grid(row=0, column=9, sticky="e")
entry_19_init.grid(row=0, column=10, sticky="w")

# Create the conversion Button and result display Label
entry_19_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_19_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_19.grid(row=0, column=9, padx=10)
entry_19_button.grid(row=0, column=10, pady=10)
entry_19_result.grid(row=0, column=11, padx=10)

# MODULE 20
# Create the entry frame with an Entry
# widget and label in it
entry_20 = tk.Frame(master=window)
entry_20_value = tk.Entry(master=entry_20, width=10)
entry_20_init = tk.Label(master=entry_20)

# Layout the Entry and Label in entry_20
# using the .grid() geometry manager
entry_20_value.grid(row=1, column=9, sticky="e")
entry_20_init.grid(row=1, column=10, sticky="w")

# Create the conversion Button and result display Label
entry_20_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_20_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_20.grid(row=1, column=9, padx=10)
entry_20_button.grid(row=1, column=10, pady=10)
entry_20_result.grid(row=1, column=11, padx=10)

# MODULE 21
# Create the entry frame with an Entry
# widget and label in it
entry_21 = tk.Frame(master=window)
entry_21_value = tk.Entry(master=entry_21, width=10)
entry_21_init = tk.Label(master=entry_21)

# Layout the Entry and Label in entry_21
# using the .grid() geometry manager
entry_21_value.grid(row=2, column=9, sticky="e")
entry_21_init.grid(row=2, column=10, sticky="w")

# Create the conversion Button and result display Label
entry_21_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_21_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_21.grid(row=2, column=9, padx=10)
entry_21_button.grid(row=2, column=10, pady=10)
entry_21_result.grid(row=2, column=11, padx=10)

# MODULE 22
# Create the entry frame with an Entry
# widget and label in it
entry_22 = tk.Frame(master=window)
entry_22_value = tk.Entry(master=entry_22, width=10)
entry_22_init = tk.Label(master=entry_22)

# Layout the Entry and Label in entry_22
# using the .grid() geometry manager
entry_22_value.grid(row=3, column=9, sticky="e")
entry_22_init.grid(row=3, column=10, sticky="w")

# Create the conversion Button and result display Label
entry_22_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_22_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_22.grid(row=3, column=9, padx=10)
entry_22_button.grid(row=3, column=10, pady=10)
entry_22_result.grid(row=3, column=11, padx=10)

# MODULE 23
# Create the entry frame with an Entry
# widget and label in it
entry_23 = tk.Frame(master=window)
entry_23_value = tk.Entry(master=entry_23, width=10)
entry_23_init = tk.Label(master=entry_23)

# Layout the Entry and Label in entry_23
# using the .grid() geometry manager
entry_23_value.grid(row=4, column=9, sticky="e")
entry_23_init.grid(row=4, column=10, sticky="w")

# Create the conversion Button and result display Label
entry_23_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_23_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_23.grid(row=4, column=9, padx=10)
entry_23_button.grid(row=4, column=10, pady=10)
entry_23_result.grid(row=4, column=11, padx=10)

# MODULE 24
# Create the entry frame with an Entry
# widget and label in it
entry_24 = tk.Frame(master=window)
entry_24_value = tk.Entry(master=entry_24, width=10)
entry_24_init = tk.Label(master=entry_24)

# Layout the Entry and Label in entry_24
# using the .grid() geometry manager
entry_24_value.grid(row=5, column=9, sticky="e")
entry_24_init.grid(row=5, column=10, sticky="w")

# Create the conversion Button and result display Label
entry_24_button = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fun_2
)
entry_24_result = tk.Label(master=window)

# Set-up the layout using the .grid() geometry manager
entry_24.grid(row=5, column=9, padx=10)
entry_24_button.grid(row=5, column=10, pady=10)
entry_24_result.grid(row=5, column=11, padx=10)

# Run the application
window.mainloop()
