# src/run.py
import shutil
import os

from src.ingestion.threat_feed_pull import pull_osint_iocs
from src.analysis.pcap_parser import generate_sample_pcap, parse_pcap
from src.analysis.ioc_correlation import correlate_iocs
from src.analysis.risk_scoring import score_vulnerabilities
from src.visualization.charts import generate_top_ip_chart
from scripts.update_readme import update_readme

# --- Hard reset every run ---
shutil.rmtree("build", ignore_errors=True)
shutil.rmtree("outputs", ignore_errors=True)

os.makedirs("build/iocs", exist_ok=True)
os.makedirs("build/pcaps", exist_ok=True)
os.makedirs("build/vulnerabilities", exist_ok=True)
os.makedirs("outputs/charts", exist_ok=True)
os.makedirs("outputs/logs", exist_ok=True)

IOC_PATH = "build/iocs/osint_iocs.csv"
PCAP_PATH = "build/pcaps/sample_traffic.pcap"
VULN_PATH = "build/vulnerabilities/vuln_scan_sample.csv"

def main():
    print("[+] Pulling OSINT IOCs")
    iocs = pull_osint_iocs(IOC_PATH)

    print("[+] Generating PCAP")
    generate_sample_pcap(PCAP_PATH)

    print("[+] Parsing PCAP")
    traffic = parse_pcap(PCAP_PATH)

    print("[+] Correlating IOCs")
    matches = correlate_iocs(traffic, iocs)

    print("[+] Scoring vulnerabilities")
    stats = score_vulnerabilities(matches, VULN_PATH)

    print("[+] Generating chart")
    generate_top_ip_chart("outputs/charts/top_source_ips.png")

    print("[+] Updating README")
    update_readme(stats)

    print("[+] Pipeline complete")

if __name__ == "__main__":
    main()
