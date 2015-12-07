from tkinter import *
from tkinter import ttk
import socket

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class MenuFrame(Frame):

    def __init__(self, master):
        super().__init__(master)
        
        self.sales = StringVar()
        self.moreSales = StringVar()
        self.sales.set("1")

        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)


        welcome = "Logged in."

        sales_entry = ttk.Entry(mainframe, width = 7, textvariable = self.moreSales)

        ttk.Label(mainframe, text = welcome).grid(column = 2, row = 1, sticky = W)

        ttk.Label(mainframe, text = "Current Sales:").grid(column = 1, row = 2, sticky = W)
        ttk.Label(mainframe, textvariable = self.sales).grid(column = 2, row = 2, sticky = (E))
        ttk.Label(mainframe, text = "sales").grid(column = 3, row = 2, sticky = W)

        ttk.Label(mainframe, text = "Add Sales").grid(column = 1, row = 3, sticky = W)
        sales_entry.grid(column = 2, row = 3, sticky = (W, E))
        ttk.Button(mainframe, text = "Add", command = self.add).grid(column = 3, row = 3, sticky = W)

        ttk.Button(mainframe, text = "Log Out", command = self.logout).grid(column = 2, row = 4, sticky = W)

    def add(self):

        try:
            value1 = int(self.sales.get())
            value2 = int(self.moreSales.get())
            self.sales.set(value1 + value2)
            
            
        except ValueError:
            pass

    def logout(self):
        self.destroy()
