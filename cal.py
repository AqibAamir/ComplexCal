import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equals():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Haytch Error")

root = tk.Tk()
root.title("Aqib's Calculator")

# Styling
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 16),
                padding=10)
style.configure("TEntry",
                font=("Helvetica", 20),
                padding=10)

# Entry widget to display input and results
entry = ttk.Entry(root)
entry.grid(row=0, column=0, columnspan=4, sticky="ew")

# Number buttons
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("0", 4, 0),
    (".", 4, 1)
]

for button in buttons:
    text, row, col = button
    ttk.Button(root, text=text, command=lambda text=text: button_click(text)).grid(row=row, column=col, sticky="nsew")

# Operator buttons
operators = [
    ("/", 1, 3),
    ("*", 2, 3),
    ("-", 3, 3),
    ("+", 4, 3)
]

for operator in operators:
    text, row, col = operator
    ttk.Button(root, text=text, command=lambda text=text: button_click(text)).grid(row=row, column=col, sticky="nsew")

# Special buttons
ttk.Button(root, text="C", command=button_clear).grid(row=4, column=2, sticky="nsew")
ttk.Button(root, text="=", command=button_equals).grid(row=4, column=1, sticky="nsew")

# Configuring grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()

