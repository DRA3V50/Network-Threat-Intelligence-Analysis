from datetime import datetime
from pathlib import Path

# INGESTION
from src.ingestion.threat_feed_pull import pull_osint_iocs

# ANALYSIS
from src.analysis.pcap_parser import parse_pcap
from src.analysis.vuln_analysis import generate_vulnerabilities
from src.analysis.charting import generate_top_source_ips_chart

# OUTPUT PATHS
BUILD_DIR = Path("build")
OUTPUT_LOGS_DIR = Path("outputs/logs")
OUTPUT_CHARTS_DIR = Path("outputs/charts")

BUILD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_LOGS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_CHARTS_DIR.mkdir(parents=True, exist_ok=True)


def main():
    print("[*] Starting Network Threat Intelligence Pipeline")

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # 1. Pull OSINT IOCs
    print("[*] Pulling OSINT IOCs")
    iocs_path = BUILD_DIR / "iocs"
    iocs_path.mkdir(exist_ok=True)
    pull_osint_iocs(output_dir=iocs_path)

    # 2. Generate Vulnerabilities
    print("[*] Generating vulnerability data")
    vulns_path = BUILD_DIR / "vulnerabilities"
    vulns_path.mkdir(exist_ok=True)
    generate_vulnerabilities(output_dir=vulns_path)

    # 3. Parse PCAP
    print("[*] Parsing PCAP")
    pcaps_path = BUILD_DIR / "pcaps"
    pcaps_path.mkdir(exist_ok=True)
    parse_pcap(output_dir=pcaps_path)

    # 4. Generate chart from PCAP results
    print("[*] Generating Top Source IPs chart")
    pcap_csv = pcaps_path / "top_source_ips.csv"
    chart_output = OUTPUT_CHARTS_DIR / "top_source_ips.png"

    if pcap_csv.exists():
        generate_top_source_ips_chart(
            csv_path=pcap_csv,
            output_path=chart_output
        )
    else:
        print("[!] top_source_ips.csv not found — skipping chart")

    print(f"[+] Pipeline completed successfully at {timestamp}")


if __name__ == "__main__":
    main()
