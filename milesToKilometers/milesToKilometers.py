import tkinter as tk
from tkinter import ttk #widgets that we want
import ttkbootstrap as ttk #better version of ttk "pip install ttkbootstrap"


def convert():
    mile_input = entry_Int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#window 
window = ttk.Window(themename='darkly')
window.title("Demo")
window.geometry("300x150")

#title
title_label = ttk.Label(master = window, text = "Miles to kilometers", font = "Calibri 24 bold")
title_label.pack()

#input field 
input_frame = ttk.Frame(master=window )
entry_Int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable= entry_Int)
button = ttk.Button(master = input_frame, text = "convert", command= convert)

input_frame.pack(pady= 10)
entry.pack(side= "left", padx= 10)
button.pack(side= "left")

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text = "Output: ",
    font = "Calibri 20",
    textvariable= output_string)
output_label.pack(padx=50)

#run
window.mainloop()