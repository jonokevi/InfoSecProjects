
import socket 


def portScanner(port):
#try:
    if sock.connect_ex((host, port)): 
        print("The port is closed.")
    else:
        print("The port is open.")
#except ValueError: 
    #print("Invalid Entry. Please try again.")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

try:
    host = input("IP Address: ")                                                           #host should be target IP
    port = int(input("Port: "))                                                            #adjust port to select which port needs to be scanned.
    portScanner(port)
except: 
    print("Invalid Entry. Please try again.")