#hey john
#somewhere in this file (server), you need to send the contents of row[3] for the user
#that logs in
#from there, you need to receive the amount that the user would like to add from Menu.py
#you need to add that number to the number that you originally sent and send the result
#you also need to replace the number in row[3] with the new number
#good luck and thank you. i'll be up 10ish working on this report so text me




import socket
# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    # Receive the client packet along with the address it is coming from
    username, address = serverSocket.recvfrom(1024)
    username = username.decode('UTF-8')

    password, address = serverSocket.recvfrom(1024)
    password = password.decode('UTF-8')


    infile = open("DunderMifflin.txt", 'r')

    for rows in infile:    #equivalent to: Recs=infile.readline()
                        #this gets 1 line at a time as a string including \n
        rows = rows.strip()
        rowsList = rows.split('\t')
        #message += row + "\n" # + str(rowsList)
        username2 = rowsList[0].strip(' ')
        if username == username2:

            password2 = rowsList[1]
            if password == password2:

                # the server responds
                message = "200 OK"
                message = message.encode('UTF-8')
                serverSocket.sendto(message, address)

                

            else:
                # the server responds
                message = "401 Unauthorized"
                message = message.encode('UTF-8')
                serverSocket.sendto(message, address)
        
        
        #Lname=stuRecLst[1]
        #T1=float(stuRecLst[2])
        #T2=float(stuRecLst[3])
        #T3=float(stuRecLst[4])
        #Tav=(T1+T2+T3)/3
        #print(ID,Lname,T1,T2,T3)

    # the server responds
    message = "401 Unauthorized"
    message = message.encode('UTF-8')
    serverSocket.sendto(message, address)
    
    infile.close()
