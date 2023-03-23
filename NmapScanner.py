#!/usr/bin/python3
 
import nmap #importing nmap tool
 
scanner = nmap.PortScanner()         #creating scanner var using nmap tool

print("Welcome, this is a simple nmap automation tool")
print ("-------------------------------------")

ip_address = input("Enter IP Address for scan: ")  #creating ip address variable for input
print("IP entered: ", ip_address)
type(ip_address)

#creating options for types of scan and input responsse variable
response = input(""" \nPlease enter the type of scan you want to run:    
                     1)SYN ACK Scan
                     2)UDP Scan
                     3)Comprehensive Scan \n""")
print("You have selected: ", response)

if response == '1': 
    print("Nmap Version: ", scanner.nmap_version()) #prints out nmap version  
    scanner.scan(ip_address, '1-1024', '-v -sS')  #provide ip address, +port, and type of scan desired
    print(scanner.scaninfo())
    print("IP Status:  ", scanner[ip_address].state())  
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
    
elif response == '2':
    print("Nmap Version: ", scanner.nmap_version()) #prints out nmap version  
    scanner.scan(ip_address, '1-1024', '-v -sU')  #provide ip address, +port, and type of scan desired
    print(scanner.scaninfo())
    print("IP Status:  ", scanner[ip_address].state())  
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['udp'].keys())

elif response == '3':
    print("Nmap Version: ", scanner.nmap_version()) #prints out nmap version  
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O ' )  #provide ip address, +port, and type of scan desired
    print(scanner.scaninfo())
    print("IP Status:  ", scanner[ip_address].state())  
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())

elif response >= '4' :
    print ("Invalid Entry. Please try again.") 
