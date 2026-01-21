from scapy.all import rdpcap, IP, Ether, TCP, Raw, wrpcap
import os

def parse_pcap(pcap_path):
    """Parses a PCAP and returns a list of packets"""
    packets = rdpcap(pcap_path)
    return packets

def generate_sample_pcap(pcap_path="build/pcaps/sample_traffic.pcap"):
    """Generates a sample PCAP if it doesn’t exist"""
    if not os.path.exists(os.path.dirname(pcap_path)):
        os.makedirs(os.path.dirname(pcap_path))
    
    from scapy.all import Ether, IP, TCP, Raw, wrpcap

    # Minimal packet example
    pkt = Ether()/IP(dst="1.1.1.1")/TCP()/Raw(load="test")
    wrpcap(pcap_path, [pkt])
    return [pkt]
