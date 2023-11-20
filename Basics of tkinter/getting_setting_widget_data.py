import tkinter as tk 
from tkinter import ttk

#get the content of the entry
def button_func():
    get = entry.get()
    print(get)

    #update the label
    label["text"] = get
    entry['state'] = "disabled"

def enable():
    entry['state'] = "enabled"
    label['text'] = "Some text"

#window 
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry("300x150")

#widgets+++++

# Label
label = ttk.Label(master=window, text="This is a label")
label.pack()

#entry
entry = ttk.Entry(master= window)
entry.pack()

# button
button = ttk.Button(master=window, text="Press", command=button_func)
button.pack()

#button2
button2 = ttk.Button(master=window, text="Enable", command = enable)
button2.pack()

#run
window.mainloop()