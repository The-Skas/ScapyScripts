#!/usr/bin/env python

import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if (len(sys.argv) <> 3):
  print len(sys.argv)
  print "Usage: python UDPClient.py host port"
  sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

server_address = (host, port)

try:
	while(1):
	    # Send data
	    message = raw_input('Enter msg: ')
	    sent = sock.sendto(message, server_address)

	    # Receive response
	    data, server = sock.recvfrom(4096)
	    print "Server:",data

finally:
	    print >>sys.stderr, 'closing socket'
	    sock.close()
