#DunderMifflinClient.py

import socket
import time
from tkinter import *
import tkinter.messagebox as tm

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# GUI

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        #print("Clicked")
        username = self.entry_1.get()
        clientSocket.sendto(username.encode('UTF-8'),(serverName, serverPort))
        
        password = self.entry_2.get()
        clientSocket.sendto(password.encode('UTF-8'),(serverName, serverPort))

        #print(username, password)
        message, address = clientSocket.recvfrom(1024)
        message = message.decode('UTF-8')
        print(message)

        if message == "ok":
            tm.showinfo("Login info", "Welcome")
        else:
            tm.showinfo("Login error", message)

root = Tk()
lf = LoginFrame(root)
root.mainloop()
