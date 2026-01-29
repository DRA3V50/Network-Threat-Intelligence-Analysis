from pathlib import Path
from src.analysis.charting import generate_unified_network_chart
from src.scripts.update_readme import generate_readme

BUILD_DIR = Path("build")
OUTPUT_CHART = BUILD_DIR / "charts" / "network_activity.png"

def finalize_outputs():
    print("[*] Finalizing outputs (charts + README)")

    iocs_csv = BUILD_DIR / "iocs" / "osint_iocs.csv"
    vulns_csv = BUILD_DIR / "vulnerabilities" / "vuln_scan_sample.csv"
    pcaps_csv = BUILD_DIR / "pcaps" / "top_source_ips.csv"

    generate_unified_network_chart(
        iocs_csv=iocs_csv,
        vulns_csv=vulns_csv,
        pcaps_csv=pcaps_csv,
        output_path=OUTPUT_CHART,
        max_rows=15
    )

    generate_readme()
    print("[+] Outputs finalized")


    # Trim Vulnerabilities
    trim_csv(
        BUILD_DIR / "vulnerabilities/vuln_scan_sample.csv",
        sort_col="risk_score"
    )

    # Trim PCAP + generate chart
    pcap_csv = BUILD_DIR / "pcaps/top_source_ips.csv"
    trim_csv(pcap_csv, sort_col="count")

    generate_top_source_ips_chart(
        csv_path=pcap_csv,
        output_path=CHARTS_DIR / "top_source_ips.png"
    )

    print("[+] Final outputs trimmed and chart generated")


if __name__ == "__main__":
    finalize_outputs()
