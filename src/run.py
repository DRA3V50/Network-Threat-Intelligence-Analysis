"""
Single entry point for the Network Threat Intelligence pipeline
Executed via: python -m src.run
"""

from ingestion.threat_feed_pull import pull_osint_iocs
from analysis.pcap_parser import parse_pcap
from analysis.ioc_correlation import correlate_iocs
from analysis.risk_scoring import score_vulnerabilities
from reporting.generate_charts import generate_top_ip_chart

def main():
    print("[+] Starting Network Threat Intelligence Pipeline")

    print("[+] Pulling OSINT IOCs...")
    iocs = pull_osint_iocs()

    print("[+] Parsing PCAP traffic...")
    traffic = parse_pcap()

    print("[+] Correlating traffic with IOCs...")
    matches = correlate_iocs(traffic, iocs)

    print("[+] Scoring vulnerabilities...")
    score_vulnerabilities(matches)

    print("[+] Generating charts...")
    generate_top_ip_chart()

    print("[+] Pipeline completed successfully")

if __name__ == "__main__":
    main()
