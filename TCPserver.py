import socket #plugin is imported


#Creating socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #serversocket is the object socket.AF_INET (INET specifically indicates IPv4)


host = 'xxx.xxx.xx.x'   #host IP redacted for uploading purposes
#host = socket.gethostname() 
port = 444

#Binding to socket
serversocket.bind((host, port)) #Host will be replaced/substituted with IP, if changed and not running on host.

#starting TCP listener
serversocket.listen(4) #listener is specified and how many requests it can have (4)(how many devices can listen in on port)

while True:
    print("Server Active")
    #Starting the connection
    clientsocket,address = serversocket.accept()
  
    print("received connection from %s " % str(address)) #prints dialogue when client is connected from (address)

    message = 'Thank you for connecting to the server.' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close() 