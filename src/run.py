from datetime import datetime
from pathlib import Path

# INGESTION
from src.ingestion.threat_feed_pull import pull_osint_iocs

# ANALYSIS
from src.analysis.pcap_parser import parse_pcap
from src.analysis.vuln_analysis import generate_vulnerabilities

# FINALIZATION
from src.scripts.finalize_outputs import finalize_outputs

BUILD_DIR = Path("build")


def main():
    print("[*] Starting Network Threat Intelligence Pipeline")

    pull_osint_iocs(BUILD_DIR / "iocs")
    generate_vulnerabilities(BUILD_DIR / "vulnerabilities")
    parse_pcap(BUILD_DIR / "pcaps")

    finalize_outputs()

    print(f"[+] Pipeline completed @ {datetime.utcnow()} UTC")


if __name__ == "__main__":
    main()
