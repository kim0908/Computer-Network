from socket import *
import time

serverName = "127.0.0.1"
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1) 
maxarr=[]
minarr=[]
avg=0
k=0

for i in range(10):
	message = "Ping"
	start=time.time() 
	clientSocket.sendto(message,(serverName, 12000))
	
	try:
		message, address = clientSocket.recvfrom(1024)
		rtt = (time.time()-start)
		maxarr.append(rtt)
		minarr.append(rtt)
		avg=avg+rtt
		k=k+1
		print i
		print message
		print "RTT=" + str(rtt) + " seconds" 
		
	except timeout:
		maxarr.append(-10)
		minarr.append(10)
		print i
		print "Request timed out"

clientSocket.close()

print "max RTT is =>",max([maxarr[0],maxarr[1],maxarr[2],maxarr[3],maxarr[4],maxarr[5],maxarr[6],maxarr[7],maxarr[8],maxarr[9]]),"sec"
print "min RTT is =>",min([minarr[0],minarr[1],minarr[2],minarr[3],minarr[4],minarr[5],minarr[6],minarr[7],minarr[8],minarr[9]]),"sec"
print "avg RTT is =>",(avg/k),"sec"
print "packet loss rate is =>",(10-k)*10,"%"
