import socket
s=socket.socket()
s.bind(('192.168.1.108',9999))
s.listen(5)

while 1:
    cs,address = s.accept()
    print ('got connected from',address)
    cs.send('hello I am server,welcome')
    ra=cs.recv(512)
    print (ra)
    cs.close()