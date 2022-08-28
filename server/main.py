import socket			
from DataHandler import MessageSort

s = socket.socket()		
print ("Socket successfully created")
port = 12345			
s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")		

while True:

    c, addr = s.accept()	
    print ('Got connection from', addr )
    message = c.recv(1024).decode()
    MessageSort(message)
    c.send('OK'.encode())
    c.close()