#!/usr/bin/python3

#Ananya Singh
#as2863
#006

#DON'T NEED CACHE


import sys, time, os, datetime, codecs
from socket import *

def lastModif(filename):  #shoutout stack overflow
    s = os.path.getmtime(filename)
    t = time.gmtime(s) 
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", t)

argv= sys.argv
host= argv[1] 
port= argv[2]
serverIP = host
serverPort = int(port)
dataLen= 100000

serverSocket= socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverIP, serverPort))

print("Port: " + port)
print("Host: " + host)

serverSocket.listen(1)

counter = 0 

while True:
    lastModDT=""
    RD=""
    #Hints
    connectionSocket, address = serverSocket.accept()
    RequestData = connectionSocket.recv(dataLen).decode()
    t = datetime.datetime.utcnow()
    RDT = t.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print("Data was received")    
    Count=0
    for Line in RequestData.split("\r\n"):
        Count+=1
        if Count==5: #line5 split
            if "If-Modified-Since" in Line:
                lastModDT = Line[20:]
  
    for item in RequestData.split():
        if item[0] == "/":
            filename = item[1:]
    
    if not os.path.isfile(filename):
        RD = "HTTP/1.1 404 Not Found" + "\r\n" + "Date: " + RDT + "\r\n" + "\r\n"

    else:
        lastModCD = lastModif(filename)
        lastModCache = lastModif('cache.txt')
        if lastModCD < lastModCache:
            RD = "HTTP/1.1 304 Not Modified\r\n" + "Date: " + RDT + "\r\n" + "\r\n"
        else:
            html = ""
            f=codecs.open('filename.html', 'r', encoding='utf-8')
            Data = f.read()
            for line in Data.split("\n"):
                if '<p class="p1">' in line:
                    html+= line
            ContentLength = str(len(html))
            RD = "HTTP/1.1 200 OK" + "\r\n" + "Date: " + RDT  + "\r\n" + "Last-Modified: " + lastModCD + "\r\n" + "Content-Length: " + ContentLength + "\r\n" + "Content-Type: text/html; charset=UTF-8" + "\r\n" + "\r\n" + html 

    connectionSocket.send(RD.encode())
    print("Data was sent back to the client")


counter = counter + 1
connectionSocket.close()
