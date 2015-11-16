#DunderMifflinClient.py

import socket
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

username = input("Username: ")
clientSocket.sendto(username.encode('UTF-8'),(serverName, serverPort))

message, serverAddress = clientSocket.recvfrom(1024)
message = message.decode('UTF-8')

if message == "ok":
    password = input("Password: ")
    clientSocket.sendto(password.encode('UTF-8'),(serverName, serverPort))

else:
    print("Invalid username")
    clientSocket.close()
