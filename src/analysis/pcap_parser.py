import csv
import random
from pathlib import Path


def generate_sample_pcap(pcap_path: Path):
    """
    Create a simulated PCAP placeholder file
    """
    pcap_path.parent.mkdir(parents=True, exist_ok=True)

    with open(pcap_path, "wb") as f:
        f.write(b"PCAP_SIMULATED_CONTENT")

    print(f"[+] Sample PCAP generated at {pcap_path}")


def parse_pcap(output_dir: Path, top_n: int = 10):
    """
    Simulate parsing a PCAP and extracting top source IPs
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    pcap_file = output_dir / "sample_traffic.pcap"
    csv_output = output_dir / "top_source_ips.csv"

    # Ensure a sample PCAP exists
    if not pcap_file.exists():
        generate_sample_pcap(pcap_file)

    ip_counts = {}

    for _ in range(200):
        ip = f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
        ip_counts[ip] = ip_counts.get(ip, 0) + random.randint(1, 5)

    top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

    with open(csv_output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["source_ip", "count"])
        for ip, count in top_ips:
            writer.writerow([ip, count])

    print(f"[+] Top source IPs written to {csv_output}")
