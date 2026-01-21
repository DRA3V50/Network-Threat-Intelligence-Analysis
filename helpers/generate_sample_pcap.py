from scapy.all import IP, TCP, Ether, wrpcap

pkt = Ether()/IP(dst="1.2.3.4")/TCP(dport=80)
wrpcap("build/pcaps/sample_traffic.pcap", [pkt])

print("[+] Sample PCAP generated in build/pcaps/sample_traffic.pcap")
