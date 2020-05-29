#!/usr/bin/env python3

import socket

server = socket.socket()

server.bind(('localhost',2406))

server.listen(5)
print('connections loading ...')

while True:
    client, address = server.accept()
    name = client.recv(1024).decode()
    print('{} connected with {}'.format(name, address))
    client.send(bytes('You have succesfully connected to the server','utf-8'))
    client.close()
