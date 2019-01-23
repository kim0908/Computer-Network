import time
import sys
import os
from socket import *

if len(sys.argv) != 3:
    print "Usage: python UDPPingerClient <server ip address> <server port no>"
    os._exit(1)
    

clientSocket = socket(AF_INET, SOCK_DGRAM)


clientSocket.settimeout(1)


remoteAddr = (sys.argv[1],int(sys.argv[2]))

for i in range(10):
    
    sendTime = time.time()
    message = 'PING ' + str(i + 1) + "_" + str(time.strftime("%H:%M:%S"))
    clientSocket.sendto(message, remoteAddr)
    
    try:
        data, server = clientSocket.recvfrom(1024)
        recdTime = time.time()
        rtt = recdTime - sendTime
        print "Message Received\n", data
        print "Round Trip Time", rtt
       
    
    except timeout:
        print 'REQUEST TIMED OUT'
