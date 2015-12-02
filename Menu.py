from tkinter import *
from tkinter import ttk

def add(*args):
    try:
        value1 = int(reams.get())
        value2 = int(moreReams.get())
        reams.set(value1 + value2)
    except ValueError:
        pass

def logout():
    root.destroy()

root = Tk()
root.geometry('{}x{}'.format(270, 130))
root.title("Dunder Mifflin GUI")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

name = "John"
reams = StringVar()
moreReams = StringVar()
reams.set("1")

welcome = "Welcome, " + name + "!"

reams_entry = ttk.Entry(mainframe, width = 7, textvariable = moreReams)

ttk.Label(mainframe, text = welcome).grid(column = 2, row = 1, sticky = W)

ttk.Label(mainframe, text = "Current Sales:").grid(column = 1, row = 2, sticky = W)
ttk.Label(mainframe, textvariable = reams).grid(column = 2, row = 2, sticky = (E))
ttk.Label(mainframe, text = "reams").grid(column = 3, row = 2, sticky = W)

ttk.Label(mainframe, text = "Add Sales").grid(column = 1, row = 3, sticky = W)
reams_entry.grid(column = 2, row = 3, sticky = (W, E))
ttk.Button(mainframe, text = "Add", command = add(reams, moreReams)).grid(column = 3, row = 3, sticky = W)

ttk.Button(mainframe, text = "Log Out", command = logout).grid(column = 2, row = 4, sticky = W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

reams_entry.focus()
root.bind('<Return>', add)

root.mainloop()
