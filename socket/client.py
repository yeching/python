import socket
s=socket.socket()
s.connect(('192.168.1.108',9999))   
data=s.recv(512)
print ('the data received is\n    ',data)
s.send('hihi I am client')


s.close()		