from scapy.all import *

p = sniff(filter='icmp', iface='eth0',  count=5,  prn = lambda x:x.summary())

wrpcap('packets.pcap', p)
