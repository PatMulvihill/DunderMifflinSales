#DunderMifflinServer.py

import socket
# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    # Receive the client packet along with the address it is coming from
    username, address = serverSocket.recvfrom(1024)

    username = username.decode('UTF-8')

    infile = open("DunderMifflin.txt", 'r')

    for rows in infile:    #equivalent to: Recs=infile.readline()
                        #this gets 1 line at a time as a string including \n
        rows = rows.strip()
        rowsList = rows.split('\t')
        #message += row + "\n" # + str(rowsList)
        username2 = rowsList[0].strip(' ')
        if username == username2:
            # the server responds
            message = "ok"
            message = message.encode('UTF-8')
            serverSocket.sendto(message, address)
        else:
            print()
        #Lname=stuRecLst[1]
        #T1=float(stuRecLst[2])
        #T2=float(stuRecLst[3])
        #T3=float(stuRecLst[4])
        #Tav=(T1+T2+T3)/3
        #print(ID,Lname,T1,T2,T3)

    infile.close()

    #infile=open('Dunder.txt','r')
    #stuRecLst=infile.readlines()
    #print(stuRecLst)
    
    # Capitalize the message from the client
    message = "badf"
    message = message.encode('UTF-8')
    # Otherwise, the server responds
    serverSocket.sendto(message, address)
