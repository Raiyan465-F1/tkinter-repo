import tkinter as tk
from tkinter import ttk

def button_func():
    print("A button was pressed")

def print_hello():
    print("hello")

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
another_button = ttk.Button(master=window, text= "press", command= print_hello)

another_text.pack()
another_button.pack()

#ttk button
button = ttk.Button(master=window, text="press", command= button_func)
button.pack()

#run
window.mainloop()
