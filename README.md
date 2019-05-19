# HTTP-Client-Server
Simple HTTP Client and Server

Using TCP sockets, you will write a simplified version of a HTTP client and server.  The client program will use the HTTP protocol to fetch a file from the server using the HTTP GET method, cache it, and then subsequently use conditional GET operations to fetch the file only if it has been modified. 



The HTTP client will perform the following functions:

Take in a single command line argument that specifies a web url containing the hostname and port where the server is running, as well as the name of the file to be fetched, in the appropriate format. Example: localhost:12000/filename.html

If the file is not yet cached, use a HTTP GET operation to fetch the file named in the URL

Print out the contents of the file 

Cache the file

If the file is cached, use a Conditional GET operation for the file named in the URL 

If the server indicates the file has not been modified since last downloaded, print output saying so (no need to print file contents in this case)

Otherwise, indicate that the file has been modified, and print and cache new contents



The HTTP server will perform the following functions:

Read a command-line argument specifying IP address and port server is to listen on e.g. 127.0.0.1 12000

Open a TCP socket and listen for incoming HTTP Get and Conditional GET requests from one or more HTTP Clients at above address and port

In the case of a HTTP Get request:

Read the named file and return a HTTP GET Response, including the Last-Modified header field 

In the case of a HTTP Conditional Get Request:

If the file has not been modified since that indicated by If-Modified-Since, return the appropriate Not Modified response (return code 304)

If the file has been modified, return the file contents as in step 2

In the case that the named file does not exist, return the appropriate “Not Found” error (return code 404)

The server must ignore all header fields in HTTP Requests it does not understand 
