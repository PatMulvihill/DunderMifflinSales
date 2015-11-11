#DunderMifflinClient.py

import socket
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

username = input("Username: ")
clientSocket.sendto(username.encode('UTF-8'),(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
print(modifiedMessage.decode('UTF-8'))

clientSocket.close()
