from scapy.all import *
import re
import pdb 

whitelist ="^[-a-zA-Z ,.()?]*$"
reg_whitelist = re.compile(whitelist)
def pkt_callback(pkt):
        pkt.show()
	#Inspect the UDP Layer
	pkt.getlayer("UDP")	
	#The Raw Layer is where the raw app data is stored.
	pkt.getlayer("Raw")
        pdb.set_trace() 
sniff(prn=pkt_callback, filter="port 7777", store=0)

