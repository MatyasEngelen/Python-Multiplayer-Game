import socket     

def EnterQueue():
          
    s = socket.socket()        
    port = 12345               
    s.connect(('127.0.0.1', port))
    s.send("EnterQueue".encode())
    print (s.recv(1024).decode())
    s.close()    