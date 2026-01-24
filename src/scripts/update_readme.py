import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# ================= CONFIG =================
MIN_ROWS = 3
MAX_ROWS = 8  # maximum rows for CSVs and README
IOCS_CSV = Path("iocs/osint_iocs.csv")
VULN_CSV = Path("vulnerabilities/vuln_scan_sample.csv")
TOP_IPS_CSV = Path("top_source_ips.csv")
CHART_FILE = Path("top_source_ips.png")
README_FILE = Path("README.md")
# ==========================================

def trim_and_save_csv(csv_path, sort_col=None):
    """
    Read a CSV, trim it to MAX_ROWS (but at least MIN_ROWS),
    sort by sort_col if given, then overwrite CSV.
    """
    df = pd.read_csv(csv_path)
    if sort_col:
        df = df.sort_values(by=sort_col, ascending=False)
    # Ensure at least MIN_ROWS if possible
    n_rows = min(MAX_ROWS, max(MIN_ROWS, len(df)))
    df_trimmed = df.head(n_rows)
    df_trimmed.to_csv(csv_path, index=False)
    return df_trimmed

def generate_chart(csv_path, chart_path):
    df = pd.read_csv(csv_path)
    df = df.sort_values(by="count", ascending=True).head(MAX_ROWS)

    plt.figure(figsize=(8, 5))
    colors = plt.cm.Reds(df["count"] / df["count"].max())
    plt.barh(df["ip"], df["count"], color=colors)
    plt.xlabel("Network Activity Count")
    plt.ylabel("Source IP")
    plt.title("📈 Top Source IPs by Network Activity")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

def format_table(df):
    return df.to_markdown(index=False)

def generate_readme():
    # --- Trim CSVs and overwrite them ---
    iocs_df = trim_and_save_csv(IOCS_CSV, sort_col="confidence")
    vuln_df = trim_and_save_csv(VULN_CSV, sort_col="risk_score")
    top_ips_df = trim_and_save_csv(TOP_IPS_CSV, sort_col="count")

    # --- Generate Chart ---
    generate_chart(TOP_IPS_CSV, CHART_FILE)

    # --- Current UTC timestamp ---
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # --- Readme content ---
    readme_content = f"""
# Network-Threat-Intelligence-Analysis

🛡️ Automated defensive network analysis with OSINT enrichment and threat correlation

---

## Overview
This repository demonstrates a Blue Team–focused approach to analyzing network activity,  
open-source threat intelligence, and vulnerability data in support of defensive cyber operations.

---

## Analytical Focus
- Understanding network behavior and traffic patterns  
- Applying threat intelligence to contextualize observed activity  
- Correlating indicators of compromise with network-derived insights  
- Prioritizing risk to support informed defensive actions

---

## Daily Analysis Snapshot
> This section is dynamically updated by automated workflows.  
> **Do not edit content between the markers below.**

<!-- AUTO-GENERATED-SECTION:START -->

### 🛡️ Threat Indicators (Indicators of Compromise)
📊 Timestamp (UTC): {timestamp}

{format_table(iocs_df)}

### ⚠️ High-Risk Vulnerabilities
{format_table(vuln_df)}

### 📈 Top Source IPs by Network Activity
![Top Source IPs Chart]({CHART_FILE})

*This summary is auto-generated.*

<!-- AUTO-GENERATED-SECTION:END -->

---

## Generated Files
- Reports:
  - **[OSINT Threat Indicators]({IOCS_CSV})**
  - **[Vulnerability Scan]({VULN_CSV})**
- Charts:
  - **[Top Source IPs Chart]({CHART_FILE})**

---

## Legal & Ethical Notice
- No exploitation, intrusion, or active scanning  
- Data is sanitized, simulated, or derived from public sources  
- Usage is limited to education, research, and lawful defensive analysis
"""

    # --- Write README ---
    with open(README_FILE, "w") as f:
        f.write(readme_content)

if __name__ == "__main__":
    generate_readme()
