import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# ----------------------
# CONFIGURATION
# ----------------------
MAX_ROWS = 10  # Max number of rows to include from CSVs
IOCS_CSV = Path("build/iocs/osint_iocs.csv")
VULN_CSV = Path("build/vulnerabilities/vuln_scan_sample.csv")
TOP_IPS_CSV = Path("build/top_source_ips.csv")
CHART_FILE = Path("outputs/charts/top_source_ips.png")
README_FILE = Path("README.md")

# Ensure outputs folder exists
CHART_FILE.parent.mkdir(parents=True, exist_ok=True)

# ----------------------
# HELPER FUNCTIONS
# ----------------------
def read_and_trim_csv(csv_path, sort_col=None, ascending=False):
    """Read CSV and trim to top MAX_ROWS, optionally sorted by column."""
    df = pd.read_csv(csv_path)
    if sort_col and sort_col in df.columns:
        df = df.sort_values(by=sort_col, ascending=ascending)
    return df.head(MAX_ROWS)

def generate_chart(csv_path, chart_path):
    """Generate bar chart for top IPs colored by severity/risk."""
    df = pd.read_csv(csv_path)
    if "count" not in df.columns or "ip" not in df.columns:
        print(f"CSV {csv_path} missing required columns 'ip' and 'count'. Skipping chart.")
        return

    # Normalize counts for color intensity
    counts = df["count"]
    norm = (counts - counts.min()) / (counts.max() - counts.min() + 1e-5)
    colors = [(1, 0, 0, alpha) for alpha in norm]  # red with alpha for severity

    plt.figure(figsize=(8, 5))
    plt.bar(df["ip"], df["count"], color=colors, edgecolor="black")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Connection Count")
    plt.title("Top Source IPs by Activity")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

def format_csv_to_md(df):
    """Convert DataFrame to Markdown table."""
    return df.to_markdown(index=False)

# ----------------------
# MAIN README GENERATION
# ----------------------
def generate_readme():
    # Read and trim CSVs
    iocs_df = read_and_trim_csv(IOCS_CSV, sort_col="confidence")
    vuln_df = read_and_trim_csv(VULN_CSV, sort_col="risk_score")
    top_ips_df = read_and_trim_csv(TOP_IPS_CSV, sort_col="count")

    # Generate chart
    generate_chart(TOP_IPS_CSV, CHART_FILE)

    # Prepare README content
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    readme_content = f"""
# Network Threat Intelligence Analysis

🛡️ Automated defensive network analysis with OSINT enrichment and threat correlation

---

## Overview
This repository demonstrates a Blue Team–oriented approach to analyzing network traffic, open-source threat intelligence, and vulnerabilities. Outputs are **actionable intelligence artifacts**, including correlated indicators and network summaries.

---

## Daily Automated Threat Intelligence Update

**Timestamp (UTC):** {timestamp}

### 🛡️ Top Threat Indicators (OSINT)
This table summarizes the highest-confidence indicators collected from OSINT feeds.

{format_csv_to_md(iocs_df)}

### 🔴 High-Risk Vulnerabilities
This table lists the most critical vulnerabilities identified in the network, sorted by risk score.

{format_csv_to_md(vuln_df)}

### 📈 Network Activity Chart
Top Source IPs by Activity:

![Top Source IPs Chart]({CHART_FILE})

*This summary is auto-generated.*
"""

    # Write README
    with open(README_FILE, "w") as f:
        f.write(readme_content)
    print("README.md updated successfully!")

# ----------------------
# RUN
# ----------------------
if __name__ == "__main__":
    generate_readme()
