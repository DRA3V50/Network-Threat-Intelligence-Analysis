from datetime import datetime
from pathlib import Path

# INGESTION
from src.ingestion.threat_feed_pull import pull_osint_iocs

# ANALYSIS
from src.analysis.pcap_parser import parse_pcap
from src.analysis.vuln_analysis import generate_vulnerabilities

# FINALIZATION
from src.scripts.finalize_outputs import finalize_outputs


# -----------------------------
# PATHS
# -----------------------------
BUILD_DIR = Path("build")
IOC_DIR = BUILD_DIR / "iocs"
VULN_DIR = BUILD_DIR / "vulnerabilities"
PCAP_DIR = BUILD_DIR / "pcaps"


def main():
    print("[*] Starting Network Threat Intelligence Pipeline")

    # Ensure directories exist
    BUILD_DIR.mkdir(exist_ok=True)
    IOC_DIR.mkdir(exist_ok=True)
    VULN_DIR.mkdir(exist_ok=True)
    PCAP_DIR.mkdir(exist_ok=True)

    # 1️⃣ OSINT ingestion
    print("[*] Pulling OSINT threat indicators")
    pull_osint_iocs(output_dir=IOC_DIR)

    # 2️⃣ Vulnerability analysis
    print("[*] Generating vulnerability findings")
    generate_vulnerabilities(output_dir=VULN_DIR)

    # 3️⃣ Network traffic analysis
    print("[*] Parsing PCAP and extracting network signals")
    parse_pcap(output_dir=PCAP_DIR)

    # 4️⃣ Finalization (charts + README)
    print("[*] Finalizing outputs (charts + README)")
    finalize_outputs()   # ✅ FIXED — no arguments

    print(f"[+] Pipeline completed successfully @ {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}")


if __name__ == "__main__":
    main()
