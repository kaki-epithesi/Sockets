#!/usr/bin/env python3

import socket

client = socket.socket()

client.connect(('localhost', 2406))

name = input('Enter you name : ')

client.send(bytes(name,'utf-8'))

print(client.recv(1024).decode())
