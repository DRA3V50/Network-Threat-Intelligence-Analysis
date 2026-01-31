from pathlib import Path
from src.analysis.charting import generate_unified_network_chart
from src.scripts.update_readme import generate_readme

BUILD_DIR = Path("build")
CHARTS_DIR = BUILD_DIR / "charts"

def finalize_outputs():
    print("[*] Finalizing outputs (charts + README)")

    iocs_csv = BUILD_DIR / "iocs" / "osint_iocs.csv"
    vulns_csv = BUILD_DIR / "vulnerabilities" / "vuln_scan_sample.csv"
    pcaps_csv = BUILD_DIR / "pcaps" / "top_source_ips.csv"

    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    generate_unified_network_chart(
        iocs_csv=iocs_csv,
        vulns_csv=vulns_csv,
        pcaps_csv=pcaps_csv,
        output_path=CHARTS_DIR / "network_activity.png",
        max_rows=15
    )

    generate_readme()

    print("[+] Outputs finalized")
