from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ----------------------------
# Setup paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Go to repo root
BUILD_DIR = BASE_DIR / "build"
IOCS_DIR = BUILD_DIR / "iocs"
VULN_DIR = BUILD_DIR / "vulnerabilities"
CHARTS_DIR = BUILD_DIR / "charts"

# Ensure directories exist
IOCS_DIR.mkdir(parents=True, exist_ok=True)
VULN_DIR.mkdir(parents=True, exist_ok=True)
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

# CSV files
IOCS_CSV = IOCS_DIR / "osint_iocs.csv"
VULN_CSV = VULN_DIR / "vuln_scan_sample.csv"

# README path
README_PATH = BASE_DIR / "README.md"

# ----------------------------
# Function to read and trim CSVs
# ----------------------------
def trim_top(df: pd.DataFrame, sort_col: str, min_rows=3, max_rows=10, ascending=False):
    """Sort by column and return between min_rows and max_rows"""
    df_sorted = df.sort_values(by=sort_col, ascending=ascending)
    row_count = min(max(len(df_sorted), min_rows), max_rows)
    return df_sorted.head(row_count)

# ----------------------------
# Generate chart
# ----------------------------
def generate_chart(df: pd.DataFrame, value_col: str, chart_file: Path):
    plt.figure(figsize=(6, 4))
    plt.bar(df.index.astype(str), df[value_col], color="#e63946", edgecolor="black")
    plt.xlabel("Source IP")
    plt.ylabel("Count")
    plt.title("Top Source IPs Chart")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(chart_file)
    plt.close()

# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    # Read CSVs
    iocs_df = pd.read_csv(IOCS_CSV)
    vulns_df = pd.read_csv(VULN_CSV)

    # Trim CSVs to top 3-10 rows and save back
    top_iocs = trim_top(iocs_df, sort_col="confidence", min_rows=3, max_rows=10, ascending=False)
    top_iocs.to_csv(IOCS_CSV, index=False)

    top_vulns = trim_top(vulns_df, sort_col="risk_score", min_rows=3, max_rows=10, ascending=False)
    top_vulns.to_csv(VULN_CSV, index=False)

    # ----------------------------
    # Generate top source IP chart
    # ----------------------------
    if "ip" in iocs_df.columns:
        ip_counts = iocs_df["ip"].value_counts()
        top_ips = ip_counts.head(10)
        chart_file = CHARTS_DIR / "top_source_ips.png"
        generate_chart(top_ips.to_frame(name="count"), value_col="count", chart_file=chart_file)

    # ----------------------------
    # Update README
    # ----------------------------
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # Build Markdown tables
    iocs_md = top_iocs.to_markdown(index=False)
    vulns_md = top_vulns.to_markdown(index=False)

    readme_content = f"""# Network-Threat-Intelligence-Analysis

📊 Automated defensive network analysis with OSINT enrichment and threat correlation

---

## 🗂 Overview

This repository demonstrates a Blue Team–focused approach to analyzing network activity, open-source threat intelligence, and vulnerability data.  

---

## 📊 Daily Analysis Snapshot

> This section is auto-generated. Do not edit manually.

### 🧪 Top OSINT IOCs
{ iocs_md }

### 🔴 High-Risk Vulnerabilities
{ vulns_md }

### 📈 Network Activity Chart
![Top Source IPs Chart]({CHARTS_DIR.name}/top_source_ips.png)

*Updated: {timestamp}*
"""

    # Write README
    README_PATH.write_text(readme_content, encoding="utf-8")

    print(f"README updated with {len(top_iocs)} IOC rows and {len(top_vulns)} vulnerability rows.")
    print(f"Chart saved to {CHARTS_DIR / 'top_source_ips.png'}")
