import socket
import os, sys
# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

def write(username, sales):
    infile = open("DunderMifflin.txt", 'r')
    outfile = open("DunderMifflin2.txt", 'w')

    for rows in infile:

        rows = rows.strip()
        rowsList = rows.split('\t')
        username2 = rowsList[0]
        password = rowsList[1]
        name = rowsList[2]
        if username == username2:
            sales2 = sales
        else:
            sales2 = rowsList[3]
        str = rowsList[0] + '\t' + rowsList[1] + '\t' + rowsList[2] + '\t' + sales2 + '\n'
        outfile.write(str)

    infile.close()
    outfile.close()

while True:
    # Receive the client packet along with the address it is coming from
    username, address = serverSocket.recvfrom(1024)
    username = username.decode('UTF-8')

    password, address = serverSocket.recvfrom(1024)
    password = password.decode('UTF-8')


    file = open("DunderMifflin.txt", 'r')

    for rows in file:    #equivalent to: Recs=infile.readline()
                        #this gets 1 line at a time as a string including \n
        rows = rows.strip()
        rowsList = rows.split('\t')
        username2 = rowsList[0].strip(' ')
        if username == username2:

            password2 = rowsList[1]
            if password == password2:

                # the server responds
                message = "200 OK"
                message = message.encode('UTF-8')
                serverSocket.sendto(message, address)

                message, address = serverSocket.recvfrom(1024)
                message = message.decode('UTF-8')

                if message == "GET name, sales":

                    name = rowsList[2]
                    name = name.encode('UTF-8')
                    serverSocket.sendto(name, address)

                    sales = rowsList[3]
                    sales = sales.encode('UTF-8')
                    serverSocket.sendto(sales, address)

                    message, address = serverSocket.recvfrom(1024)
                    sales = message.decode('UTF-8')

                    write(username, sales)

            else:
                # the server responds
                message = "401 Unauthorized"
                message = message.encode('UTF-8')
                serverSocket.sendto(message, address)
        
    # the server responds
    message = "401 Unauthorized"
    message = message.encode('UTF-8')
    serverSocket.sendto(message, address)

    file.close()
    
    os.remove("DunderMifflin.txt")
    os.rename("DunderMifflin2.txt", "DunderMifflin.txt")
