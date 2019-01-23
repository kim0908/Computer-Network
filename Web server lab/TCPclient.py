from socket import *
import socket
import sys

try:
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except:
	print("error to connect")
	sys.exit()
print("socket ok.\n")

host="127.0.0.1"
port=5678

client_socket.connect((host,port))
print("socket connect with "+host)
message="GET / HTTP/1.1\r\n\r\n"

try:
	client_socket.sendall(message,encode())
except socket.error:
	print("error")
	sys.exit()

print("sending success")
reply=client_socket.recv(4096)
print(reply.decode())

client_socket.close()
