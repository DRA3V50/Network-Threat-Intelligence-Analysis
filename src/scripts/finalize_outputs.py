from pathlib import Path
from src.analysis.charting import generate_unified_network_chart


def finalize_outputs():
    print("[*] Finalizing outputs (charts + README)")

    build_dir = Path("build")

    generate_unified_network_chart(
        iocs_csv=build_dir / "iocs" / "osint_iocs.csv",
        pcaps_csv=build_dir / "pcaps" / "top_source_ips.csv",
        vulns_csv=build_dir / "vulnerabilities" / "vuln_scan_sample.csv",
        output_path=build_dir / "charts" / "network_activity.png",
    )

    print("[+] Outputs finalized")
