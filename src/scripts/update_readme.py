#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------
MAX_ROWS = 10  # max rows to display for both folder and README
IOCS_CSV = Path("iocs/osint_iocs.csv")
VULN_CSV = Path("vulnerabilities/vuln_scan_sample.csv")
TOP_IPS_CSV = Path("top_source_ips.csv")
CHART_FILE = Path("outputs/charts/top_source_ips.png")
README_FILE = Path("README.md")

# -----------------------------
# Helper functions
# -----------------------------
def read_and_trim_csv(csv_path, sort_col=None, ascending=False):
    """Read CSV and trim to top MAX_ROWS, optionally sorted by column."""
    if not csv_path.exists():
        print(f"Warning: CSV file {csv_path} not found. Skipping.")
        return pd.DataFrame()
    
    df = pd.read_csv(csv_path)

    # Sort by severity/risk/count if specified
    if sort_col and sort_col in df.columns:
        df = df.sort_values(by=sort_col, ascending=ascending)

    # Trim rows to MAX_ROWS
    df = df.head(MAX_ROWS)
    return df

def format_csv_to_md(df):
    """Convert a DataFrame to markdown table format."""
    if df.empty:
        return "No data available."
    return df.to_markdown(index=False)

def generate_chart(csv_path, chart_path):
    """Generate a bar chart for top source IPs with intensity based on count."""
    if not csv_path.exists():
        print(f"Warning: CSV {csv_path} not found. Chart not generated.")
        return

    df = pd.read_csv(csv_path)
    if df.empty or "ip" not in df.columns or "count" not in df.columns:
        print(f"Chart CSV missing required data. Skipping chart.")
        return

    counts = df["count"]
    # Normalize counts for color intensity
    norm = (counts - counts.min()) / (counts.max() - counts.min() + 1e-5)
    colors = [(1, 0, 0, alpha) for alpha in norm]  # varying red intensity

    plt.figure(figsize=(8, 5))
    plt.bar(df["ip"], df["count"], color=colors, edgecolor="black")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Connection Count")
    plt.title("Top Source IPs by Activity")
    plt.tight_layout()
    chart_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(chart_path)
    plt.close()

# -----------------------------
# Main README Generation
# -----------------------------
def generate_readme():
    # Read CSVs and trim
    iocs_df = read_and_trim_csv(IOCS_CSV, sort_col="confidence", ascending=False)
    vuln_df = read_and_trim_csv(VULN_CSV, sort_col="risk_score", ascending=False)
    top_ips_df = read_and_trim_csv(TOP_IPS_CSV, sort_col="count", ascending=False)

    # Generate chart
    generate_chart(TOP_IPS_CSV, CHART_FILE)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    readme_content = f"""
# Network Threat Intelligence Analysis

🛡️ Automated defensive network analysis with OSINT enrichment and threat correlation

---

## Daily Automated Threat Intelligence Update

**Timestamp (UTC):** {timestamp}
"""

    if not iocs_df.empty:
        readme_content += f"""
### 🛡️ Top Threat Indicators (Open-Source Intel)
This table summarizes the highest-confidence threat indicators (IPs, Domains, Hashes) collected from open-source intelligence sources.

{format_csv_to_md(iocs_df)}
"""

    if not vuln_df.empty:
        readme_content += f"""
### 🔴 High-Risk Vulnerabilities
This table lists the most critical vulnerabilities identified in the network, sorted by risk score.

{format_csv_to_md(vuln_df)}
"""

    if CHART_FILE.exists():
        readme_content += f"""
### 📊 Network Activity Chart
Top Source IPs by connection count:

![Top Source IPs Chart]({CHART_FILE})

*This chart visualizes the network activity, highlighting the most active source IPs.*
"""

    # Save README
    with open(README_FILE, "w") as f:
        f.write(readme_content)

    print(f"README updated: {README_FILE}")

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    generate_readme()
