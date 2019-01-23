
import socket
import sys
from thread import *

host=''
port= 6789
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serverSocket.bind((host,port))
except socket.error:
    print("sending error")
    sys.exit()
print("socket has been bond")
serverSocket.listen(5)
print("ready to server...")
def clientthread(connection):
    wellcomemsg="wellcome to server.\n"
    connection.send(wellcomemsg.encode())

    while True:
        data = connection.recv(1024)
        reply="OK."+data.decode()
        if not data:
            break
        print(reply)
        connection.sendall(data)
    connection.close()
while 1:
    connection,addr = serverSocket.accept()
    print("connect with "+addr[0]+":"+str(addr[1]))
    start_new_thread(clientthread,(connection,))

serverSocket.close()

