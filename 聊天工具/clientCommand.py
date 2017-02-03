import socket
import sys
from thread import *
#INITIONLIZE
host=''
port=12345
# create an INET, STREAMing socket
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'clientSocket created'
# connect the client to host
clientsocket.connect((host,port))
print 'clientSocket connect success'
def clientthread():
#loop
  while True:
	data=clientsocket.recv(1024)
	if not data: 
		break
	print data
clientsocket.close()
