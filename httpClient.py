#!/usr/bin/python3

#Ananya Singh
#as2863
#006

import sys, time, os, shutil
from socket import *

# Get the server hostname, port and data length as command line arguments
argv= sys.argv
#host = argv[1] 
#WEB URL in the form of: localhost:12000/filename.html
url = argv[1]
host = url.split(":")[0]
port = url.split("/")[0].split(":")[1]
filename = url.split("/")[1]

# Command line argument is a string, change the port and data length into integer
#port = int(port)

def cache(cacheFile, filename):
    f = open(cacheFile, "a")
    f.write("File is cached")
    shutil.copy(filename, cacheFile)
    f.close()

def checkCache(cacheFile):
    if 'File is cached' in open(cacheFile).read():
        return True
    else:
        return False


# First Client GET Request and checks if file/cache exists
if os.path.isfile('./filename.html'):
    dataRequested = "GET /" + filename + " HTTP/1.1" + "\\r\\n\n" + "Host: " + host + "\\r\\n\n" + "\\r\\n"
    print(dataRequested)
    print("\n")
    if(os.path.isfile('./cache.txt') and not checkCache('./cache.txt')):
       cache("cache.txt","filename.html")
else: 
    print("either cache or filename don't exist")

#2.	If the file is not yet cached, use a HTTP GET operation to fetch the file named in the URL
#a.	Print out the contents of the file 
#b.	Cache the file


port = int(port)





# Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
clientSocket= socket(AF_INET, SOCK_STREAM)

# Create TCP connection to server
clientSocket.connect((host, port))

# Send data through TCP connection
# print("Sending data to server: " + data)
clientSocket.send(dataRequested.encode())

# Receive the server response
dataEcho = clientSocket.recv(12000)
dataEcho = dataEcho.decode()

message404 = "HTTP/1.1 404 Not Found \\r\\n"
lastModif = "Last-Modified"


while True: 
    if message404 in dataEcho:
        print(dataEcho)
        break
    else:
        print(dataEcho) 

    for data in dataEcho.split("\r\n"):
        if lastModif in data:
            LastModifTimeOld=data[15:]
    
    dataRequested = "GET /" + filename + " HTTP/1.1" + "\\r\\n\n" + "Host: " + host + "\\r\\n\n" + "If-Modified-Since: " + LastModifTimeOld + "\\r\\n\n" + "\\r\\n"
    print(dataRequested)
    print("\n")
    break 
    
# Display the server response as an output
#print("Receive data from server: " + dataEcho.decode())

#Close the client socket
clientSocket.close()
