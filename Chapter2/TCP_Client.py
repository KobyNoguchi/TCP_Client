"""
This TCP CLient makes some assumptions about sockets to be aware of

1. That our connection will always succeed

2. The server expects us to send data first. Some servers expect to 
   send data to you first and wait for a response
3. That the server will always return data to us in a timely fashion.py

Advanced: Figure out how to deal with blocking sockets, exepction-handling in sockets although
not necessary for penetration testing.
"""

import socket

target_host = "www.google.com"
target_port = 80

#create a socket object
# AF_INET parameter indicates that we'll use a standard IPv4 address or hostname
# SOCK_STREAM indicates that this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the client
client.connect((target_host, target_port))

#send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#recieve some data
response = client.recv(4096)

print(response.decode())
client.close()


