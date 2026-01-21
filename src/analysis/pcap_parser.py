from scapy.all import rdpcap

def parse_pcap(pcap_path="build/pcaps/sample_traffic.pcap"):
    """
    Parses a PCAP file and returns packets.
    """
    packets = rdpcap(pcap_path)
    print(f"[+] Parsed {len(packets)} packets from {pcap_path}")
    return packets
