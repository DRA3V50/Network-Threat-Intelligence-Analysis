from datetime import datetime
from pathlib import Path
import pandas as pd

README_PATH = Path("README.md")

IOC_PATH = Path("build/iocs/osint_iocs.csv")
VULN_PATH = Path("build/vulnerabilities/vuln_scan_sample.csv")
HIGH_RISK_PATH = Path("outputs/logs/high_risk_vulns.csv")
CHART_PATH = "outputs/charts/top_source_ips.png"

START_MARKER = "<!-- AUTO-GENERATED-SECTION:START -->"
END_MARKER = "<!-- AUTO-GENERATED-SECTION:END -->"


def load_csv(path):
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()


def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    iocs_df = load_csv(IOC_PATH)
    vulns_df = load_csv(VULN_PATH)
    high_risk_df = load_csv(HIGH_RISK_PATH)

    # 🔒 LIMIT ROWS (THIS IS THE KEY)
    if not iocs_df.empty:
        iocs_df = (
            iocs_df.sort_values("confidence", ascending=False)
            .head(8)
        )

    if not vulns_df.empty:
        vulns_df = (
            vulns_df.sort_values("risk_score", ascending=False)
            .head(6)
        )

    if not high_risk_df.empty:
        high_risk_df = high_risk_df.head(4)

    iocs_table = iocs_df.to_markdown(index=False)
    vulns_table = vulns_df.to_markdown(index=False)
    high_risk_table = high_risk_df.to_markdown(index=False)

    auto_section = f"""
### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** {timestamp}

<table>
<tr>
<td width="50%">

#### 🔴 High-Risk Vulnerabilities
{high_risk_table}

</td>
<td width="50%">

#### 🧪 Top OSINT IOCs
{iocs_table}

</td>
</tr>
<tr>
<td colspan="2" align="center">

#### 📈 Network Activity Chart
<img src="{CHART_PATH}" alt="Top Source IPs Chart" width="500">

</td>
</tr>
</table>

*This summary is auto-generated.*
"""

    readme = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in readme or END_MARKER not in readme:
        raise RuntimeError("README markers not found")

    new_readme = (
        readme.split(START_MARKER)[0]
        + START_MARKER
        + auto_section
        + "\n"
        + END_MARKER
        + readme.split(END_MARKER)[1]
    )

    README_PATH.write_text(new_readme, encoding="utf-8")
    print("[+] README updated successfully")


if __name__ == "__main__":
    main()
