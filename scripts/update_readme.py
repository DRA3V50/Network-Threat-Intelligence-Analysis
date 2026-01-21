import os
import pandas as pd
from datetime import datetime

# --- Paths ---
README_PATH = "README.md"
BUILD_IOCS = "build/iocs/osint_iocs.csv"
BUILD_VULNS = "build/vulnerabilities/vuln_scan_sample.csv"
BUILD_PCAP = "build/pcaps/sample_traffic.pcap"
TOP_IPS_CSV = "outputs/logs/top_source_ips.csv"
TOP_IPS_PNG = "outputs/charts/top_source_ips.png"

# --- Gather metrics ---
def count_csv_rows(csv_path):
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        return len(df)
    return 0

def sample_pcap_exists(pcap_path):
    return os.path.exists(pcap_path)

iocs_count = count_csv_rows(BUILD_IOCS)
vulns_count = count_csv_rows(BUILD_VULNS)
pcap_exists = sample_pcap_exists(BUILD_PCAP)

# High-risk vulnerabilities (example: risk score > 7)
high_risk_count = 0
if os.path.exists(BUILD_VULNS):
    df_vulns = pd.read_csv(BUILD_VULNS)
    if "risk_score" in df_vulns.columns:
        high_risk_count = (df_vulns["risk_score"] > 7).sum()

# Top source IPs
top_ips_count = 0
if os.path.exists(TOP_IPS_CSV):
    df_ips = pd.read_csv(TOP_IPS_CSV)
    top_ips_count = len(df_ips)

# Timestamp
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# --- Generate README snippet ---
snapshot_md = f"""
## 📊 Daily Analysis Snapshot

> This section is dynamically updated by automated workflows.

### **Daily Automated Threat Intelligence Update** ({timestamp})

- **Vulnerabilities loaded:** {vulns_count}
- **OSINT IOCs loaded:** {iocs_count}
- **Sample PCAP generated:** {"Yes" if pcap_exists else "No"}
- **Top Source IPs:** {top_ips_count}
- **High-Risk Vulnerabilities:** {high_risk_count}

*This summary is auto-generated.*

### **Generated Files and Outputs**

#### **Reports:**
- **[Matched IOCs CSV](outputs/reports/matched_iocs.csv)**
- **[High-Risk Vulnerabilities CSV](outputs/reports/high_risk_vulns.csv)**
- **[Analysis Summary MD](outputs/reports/analysis_summary.md)**

#### **Chart:**"""

if os.path.exists(TOP_IPS_PNG):
    snapshot_md += f"\n![Top Source IPs Chart]({TOP_IPS_PNG})"

snapshot_md += f"""

#### **Logs:**
- **[Top Source IPs CSV](outputs/logs/top_source_ips.csv)**
"""

# --- Insert / Update README section ---
def update_readme(readme_path, new_section):
    if not os.path.exists(readme_path):
        print(f"{readme_path} does not exist!")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Markers for dynamic section
    start_marker = "<!-- DAILY_ANALYSIS_START -->"
    end_marker = "<!-- DAILY_ANALYSIS_END -->"

    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = f"{before}{start_marker}\n{new_section}\n{end_marker}{after}"
    else:
        # If markers don't exist, append at the end
        new_content = f"{content}\n{start_marker}\n{new_section}\n{end_marker}"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

update_readme(README_PATH, snapshot_md)
print("[+] README.md updated with latest daily snapshot")
