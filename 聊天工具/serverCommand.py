import socket
import sys
from thread import *
#INITIONLIZE
host=''
port=12345
# create an INET, STREAMing socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'serverSocket created'
# bind the socket to a public host, and a well-known port
serversocket.bind((host,port))
print 'serverSocket bind complete'
# become a server socket
serversocket.listen(5)
print 'serverSocket now listening'
def clientthread(clientsocket):
	clientsocket.send('Welcome to the server. Type something and hit enter\n')
	while True:
		data=clientsocket.recv(1024)
		#reply = 'server:' + data
		if not data: 
			break
		print data
	clientsocket.close()
#loop
while True:
	# accept connections from client
	(clientsocket,address)=serversocket.accept()
	print 'Connected with ' + address[0] + ':' + str(address[1])
	start_new_thread(clientthread ,(clientsocket,))
serversocket.close()
