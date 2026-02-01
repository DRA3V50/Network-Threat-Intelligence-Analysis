from pathlib import Path

from src.analysis.charting import generate_unified_network_chart

BUILD_DIR = Path("build")
CHARTS_DIR = BUILD_DIR / "charts"


def finalize_outputs():
    print("[*] Finalizing outputs (charts + README)")

    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    chart_path = CHARTS_DIR / "network_activity.png"

    generate_unified_network_chart(
        iocs_csv=BUILD_DIR / "iocs" / "osint_iocs.csv",
        vulns_csv=BUILD_DIR / "vulnerabilities" / "vuln_scan_sample.csv",
        pcaps_csv=BUILD_DIR / "pcaps" / "top_source_ips.csv",
        output_path=chart_path,
    )

    _update_readme(chart_path)

    print("[+] Outputs finalized")


def _update_readme(chart_path: Path):
    readme = Path("README.md")

    chart_md = f"""
## 📊 Network Activity Overview

![Network Activity]({chart_path.as_posix()})

⚠️ **Important Notes**
- All data is simulated for research, education, and portfolio demonstration
- No production environments are monitored
"""

    if readme.exists():
        content = readme.read_text()
        if "## 📊 Network Activity Overview" in content:
            content = content.split("## 📊 Network Activity Overview")[0]
        readme.write_text(content + chart_md)
    else:
        readme.write_text("# Network Threat Intelligence Analysis\n" + chart_md)
