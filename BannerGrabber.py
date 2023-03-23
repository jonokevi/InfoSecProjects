#!/usr/bin/python3 for linux users

#import socket

#sock = socket.socket()

#ip = input("Enter IP Address: ")
#port = str(input("Enter port: "))

#sock.connect((ip, int(port)))

#print(sock.recv(1024))

import socket

def banner(ip, port): 
    try:
        sock = socket.socket()
        sock.connect((ip, int(port)))
        sock.settimeout(5)
        print(sock.recv(1024).decode())                                     #.strip('b'))      #.decode('ascii')  .strip('b') would manually strip it in output, .decode("ascii") would help filter the output better
    except ConnectionRefusedError:                                          #error handling protocol through implementing an exception
        print("Connection timed out. Please try a different port.")     
    except socket.gaierror:
        print("Invalid Entry. Please try a different input.")
    except:                                                                 #if an exception occurs that is an unknown error, a general except: will encompass those.
        print("Unknown Error Occurred.") 
  

 


def main():
    ip = input("Enter IP:")
    port = str(input("Enter Port:"))
    banner(ip, port)


    


main()
