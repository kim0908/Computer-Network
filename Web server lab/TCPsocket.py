#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

serverPort = 50306
serverSocket.bind(('',serverPort))
serverSocket.listen(5)

while True:
 #Establish the connection
 print('Ready to server...\n')
 connectionSocket, addr = serverSocket.accept()

 try:
     message = connectionSocket.recv(1024)
     filename = message.split()[1]
     f=open(filename[1:])
     #Send one HTTP header line into socket

     outputdata = f.readlines()
     connectionSocket.send('HTTP/1.1 200 OK\r\nConnect-Type:text/html\r\n')
     connectionSocket.send('\r\n')
     
     #Send the content of the requested file to the client
     for i in range(0, len(outputdata)):
         connectionSocket.send(outputdata[i].encode())
     connectionSocket.send("\r\n".encode())
     connectionSocket.close()
 except IOError:
     #Send response message for file not found
     connectionSocket.send('HTTP/1.1 404 not found\n') 
     #Close client socket
     connectionSocket.close()
     
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 