import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'xxx.xxx.xx.x' #host IP redacted for uploading purposes
#host = socket.gethostname()

port = 444

clientsocket.connect ((host, port))

message = clientsocket.recv(1024) #max data allowed to come through the port

clientsocket.close()

print(message.decode('ascii'))