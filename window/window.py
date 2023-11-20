#abosule basic of tkinter

import tkinter as tk
from tkinter import ttk

def button_func():
    print("A button was pressed")

#create a window 
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

#ttk widgets
label = ttk.Label(master=window , text="this is a test")
label.pack()

#create widgets
text = tk.Text(master=window)
text.pack()

#ttk entry
entry = ttk.Entry(master= window)
entry.pack()

#another text and buttons
another_text = tk.Label(master=window, text = "my label")
another_text.pack()

#ttk button
button = ttk.Button(master=window, text="press", command= button_func)
button.pack()

#another button
another_button = ttk.Button(master=window, text= "another button", command= lambda: print("hello"))
another_button.pack()

#run
window.mainloop()
