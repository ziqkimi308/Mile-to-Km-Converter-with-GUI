"""
********************************************************************************
* Project Name:  Mile to Kilometer Converter with GUI
* Description:   Simple GUI that converts unit mile to kilometer.
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

from tkinter import *

# Function
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result.config(text=f"{km}")

# Tk
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

# Label
miles_label = Label(text="Miles")
is_equal_to = Label(text="is equal to")
km_result = Label(text="0")
km_label = Label(text="Km")

miles_label.grid(row=0, column=2)
is_equal_to.grid(row=1, column=0)
km_result.grid(row=1, column=1)
km_label.grid(row=1, column=2)

# Button
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)

# Final
window.mainloop()