import os
import pandas as pd

# --- Paths ---
README_PATH = "README.md"
IOC_PATH = "build/iocs/osint_iocs.csv"
PCAP_PATH = "build/pcaps/sample_traffic.pcap"
VULN_PATH = "build/vulnerabilities/vuln_scan_sample.csv"
TOP_IPS_CSV = "outputs/logs/top_source_ips.csv"
TOP_IPS_CHART = "outputs/charts/top_source_ips.png"

# --- Load data safely ---
def safe_count_csv(path):
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            return len(df)
        except Exception:
            return 0
    return 0

vuln_count = safe_count_csv(VULN_PATH)
ioc_count = safe_count_csv(IOC_PATH)
top_ip_count = safe_count_csv(TOP_IPS_CSV)

# High-risk vulnerabilities (example: assume score column exists)
high_risk_count = 0
if os.path.exists(VULN_PATH):
    try:
        df_vuln = pd.read_csv(VULN_PATH)
        if "risk_score" in df_vuln.columns:
            high_risk_count = len(df_vuln[df_vuln["risk_score"] > 7])
    except Exception:
        high_risk_count = 0

# --- Update README ---
if os.path.exists(README_PATH):
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    # Dynamic daily snapshot section
    snapshot_md = f"""
## 📊 Daily Analysis Snapshot

> This section is dynamically updated by automated workflows.

### **Daily Automated Threat Intelligence Update**

- **Vulnerabilities loaded:** {vuln_count}
- **OSINT IOCs loaded:** {ioc_count}
- **Sample PCAP generated:** {"Yes" if os.path.exists(PCAP_PATH) else "No"}
- **Top Source IPs:** {top_ip_count}
- **High-Risk Vulnerabilities:** {high_risk_count}

*This summary is auto-generated.*
"""

    # Replace existing snapshot or append if not present
    import re
    pattern = r"## 📊 Daily Analysis Snapshot(.|\n)*?\*This summary is auto-generated.\*"
    if re.search(pattern, readme):
        readme = re.sub(pattern, snapshot_md, readme)
    else:
        readme += "\n" + snapshot_md

    # Optionally, update chart path in README if needed
    chart_md = f"![Top Source IPs Chart]({TOP_IPS_CHART})"
    if "![Top Source IPs Chart]" in readme:
        readme = re.sub(r"!\[Top Source IPs Chart\]\(.*?\)", chart_md, readme)
    else:
        readme += "\n" + chart_md

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)

    print("[+] README.md updated with latest outputs")
else:
    print("[!] README.md not found")
