#!/usr/bin/env python

# Adapted from pymotw.com/2/socket/udp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host = 'localhost'
port = 7777
server_address = (host, port)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    
    if data:
	if(data in ["cat", "cat password.txt"]):
		sent = sock.sendto('FLG_Ae194iz3', address)
	else:	
		sent = sock.sendto('OK' , address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)





