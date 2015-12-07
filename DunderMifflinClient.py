import socket
from tkinter import *
import tkinter.messagebox as tm
from tkinter import ttk
import Menu

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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

        self.logbtn = Button(self, text="Login", command = self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):

        username = self.entry_1.get()
        clientSocket.sendto(username.encode('UTF-8'),(serverName, serverPort))

        password = self.entry_2.get()
        clientSocket.sendto(password.encode('UTF-8'),(serverName, serverPort))

        message, address = clientSocket.recvfrom(1024)
        message = message.decode('UTF-8')

        if message == "200 OK":
            mf = Menu.MenuFrame(root)
            mf.pack(fill="both", expand=True)

        else:
            tm.showinfo(message, "LOGIN ERROR")

root = Tk()
Menu.root = root
root.title("Sales Counter")
root.geometry('{}x{}'.format(300, 180))
lf = LoginFrame(root)
root.mainloop()
