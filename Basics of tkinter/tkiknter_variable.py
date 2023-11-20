import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Tkinter variables")

#widgets
label = ttk.Label(master=window, text="label")
label.pack()

#entry
entry = ttk.Entry(master=window)
entry.pack()
