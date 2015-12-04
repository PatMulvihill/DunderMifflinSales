from tkinter import *
from tkinter import ttk

class MenuFrame(Frame):

    sales = StringVar()

    def __init__(self, master):
        super().__init__(master)
        
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)

        name = "John"
        sales = StringVar()
        moreSales = StringVar()
        sales.set("1")

        welcome = "Welcome, " + name + "!"

        sales_entry = ttk.Entry(mainframe, width = 7, textvariable = moreSales)

        ttk.Label(mainframe, text = welcome).grid(column = 2, row = 1, sticky = W)

        ttk.Label(mainframe, text = "Current Sales:").grid(column = 1, row = 2, sticky = W)
        ttk.Label(mainframe, textvariable = sales).grid(column = 2, row = 2, sticky = (E))
        ttk.Label(mainframe, text = "sales").grid(column = 3, row = 2, sticky = W)

        ttk.Label(mainframe, text = "Add Sales").grid(column = 1, row = 3, sticky = W)
        sales_entry.grid(column = 2, row = 3, sticky = (W, E))
        ttk.Button(mainframe, text = "Add", command = MenuFrame.add(sales, moreSales)).grid(column = 3, row = 3, sticky = W)

        ttk.Button(mainframe, text = "Log Out", command = MenuFrame.logout).grid(column = 2, row = 4, sticky = W)

    def add(sales, moreSales):
        
        try:
            value1 = int(sales.get())
            value2 = int(moreSales.get())
            sales.set(value1 + value2)
        except ValueError:
            pass

    def logout():
        root.destroy()

root = Tk()
root.title("Dunder Mifflin GUI")
mf = MenuFrame(root)
root.mainloop()
