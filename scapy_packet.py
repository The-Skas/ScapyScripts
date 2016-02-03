from scapy.all import *
import re
import pdb 

whitelist ="^[-a-zA-Z ,.()?]*$"
reg_whitelist = re.compile(whitelist)

#A ports of services running on our server
services = [7777, 1337]

paranoid_mode = False
def pkt_callback(pkt):
	#Returns if no data in packet
	if not pkt.load:
		return 
	
	#We check to see if its one of our
	#services sending the current packet
	if pkt.sport in services: 
	   is_flag_stolen(pkt) 

	##Check if data is not safe .
	elif not reg_whitelist.search(pkt.load):
		print "ALERT: Scary Packets Ahead!"	
		print "packet_data:",pkt.load  


def is_flag_stolen(pkt):
	#Check if the data contains the substring
	#	FLG_*
	if 'FLG_' in pkt.load:
		print "ALERT:  Flag found in packet!"	

sniff(prn=pkt_callback, filter="port 7777", store=0)

"""
#Inspect the UDP Layer
pkt.getlayer("UDP")	
#The Raw Layer is where the raw app data is stored.
raw = pkt.getlayer("Raw")
"""

