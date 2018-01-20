import socket

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

serversocket.listen(5)

#establish a connection
clientsocket,addr = serversocket.accept()
print("Got a connection from %s" % str(addr))

msg = 'Message Received' + "\r\n"


while True:
    res = clientsocket.recv(1024)
    print('Message Received: ' + res.decode('ascii'))
    clientsocket.send(msg.encode('ascii'))
    
