'''
Task # 05
Network Packet Analyzer

Develop a packet sniffer tool that captures and analyzes network packets. 
Display relevant information such as source and destination IP addresses, protocols, 
and payload data. Ensure the ethical use of the tool for educational purposes.

'''

from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers import *

def packet_analyzer(IP):
# Check if packet is IPv4
    if packet.haslayer(IP):
         # Get source and destination IP addresses
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
# Get protocol
        protocol = packet[IP].proto
 # Check if Raw layer exists
        if packet.haslayer(Raw):
            payload = packet[Raw].load
        else:
            payload = ""

        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}")
        print("...................................")
# Start sniffing
sniff(filter="ip", prn=packet_analyzer)
        
