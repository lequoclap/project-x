__author__ = 'dimage01'


import socket               # Import socket module

s = socket.socket()         # Create a socket object
 host = socket.gethostname() # Get local machine name
# host = "127.0.0.1"

#port = 2200                # Reserve a port for your service.
port = 12345
s.connect((host, port))
print s.recv(1024)
s.close

