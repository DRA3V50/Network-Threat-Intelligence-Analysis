# run.py — single entry point for the entire pipeline

# --- Imports ---

# OSINT ingestion
from src.ingestion.threat_feed_pull import pull_osint_iocs

# TCP/IP analysis
from src.analysis.pcap_parser import generate_sample_pcap, parse_pcap

# Threat correlation
from src.analysis.ioc_correlation import correlate_iocs

# Risk scoring
from src.analysis.risk_scoring import score_vulnerabilities

# Reporting / charts
from src.reporting.generate_charts import generate_top_ip_chart

# --- Paths to built/generated files ---
IOC_PATH = "build/iocs/osint_iocs.csv"
PCAP_PATH = "build/pcaps/sample_traffic.pcap"
VULN_PATH = "build/vulnerabilities/vuln_scan_sample.csv"

# --- Main Pipeline ---
def main():
    print("[+] Generating missing sample data if needed...")

    # OSINT IOCs
    print("[+] Pulling OSINT IOCs...")
    iocs = pull_osint_iocs()  # function handles writing to IOC_PATH internally
    print(f"[+] OSINT IOCs saved to {IOC_PATH}")

    # Sample PCAP generation
    print("[+] Generating missing sample PCAP if needed...")
    packets = generate_sample_pcap(PCAP_PATH)
    print(f"[+] Parsed {len(packets)} packets from {PCAP_PATH}")

    # Parsing PCAP traffic
    print("[+] Parsing PCAP traffic...")
    traffic = parse_pcap(PCAP_PATH)

    # Correlating IOCs with traffic
    print("[+] Correlating IOCs with traffic...")
    matches = correlate_iocs(traffic, iocs)
    print(f"[+] Correlated {len(matches)} IOC matches with traffic")

    # Risk scoring
    print("[+] Scoring risks...")
    score_vulnerabilities(matches, VULN_PATH)
    print(f"[+] Risk scoring complete. Results saved to {VULN_PATH}")

    # Generating charts and reports
    print("[+] Generating charts and reports...")
    generate_top_ip_chart()
    print("[+] Charts and reports generated")

    print("[+] Pipeline completed successfully!")

# --- Entry Point ---
if __name__ == "__main__":
    main()
