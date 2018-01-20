#!/usr/bin/python3           # This is client.py file

import socket

# get local machine name
host = socket.gethostname()                           

port = 9999

socket = socket.create_connection((host,port))                         

# Receive no more than 1024 bytes
while True:
    msg = input('Text to send: ')
    socket.send(msg.encode('ascii'))
    response = socket.recv(1024)
    print (response.decode('ascii'))

socket.close()
