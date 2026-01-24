import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

# Paths
IOCS_CSV = Path("iocs/osint_iocs.csv")
VULN_CSV = Path("vulnerabilities/vuln_scan_sample.csv")
CHART_FILE = Path("charts/top_source_ips.png")
README_FILE = Path("README.md")

# Settings
MAX_ROWS = 10  # Max rows for tables
SEVERITY_COLORS = {
    "CRITICAL": "#B22222",  # FireBrick
    "HIGH": "#FF4500",      # OrangeRed
    "MEDIUM": "#FFA500",    # Orange
    "LOW": "#FFD700"        # Gold
}

def read_and_trim_csv(csv_path, max_rows=MAX_ROWS, severity_col="severity"):
    df = pd.read_csv(csv_path)
    if severity_col in df.columns:
        # Sort by severity: CRITICAL > HIGH > MEDIUM > LOW
        severity_order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
        df["severity_rank"] = df[severity_col].map(severity_order).fillna(0)
        df = df.sort_values("severity_rank", ascending=False)
        df = df.head(max_rows)
        df.drop(columns=["severity_rank"], inplace=True)
    else:
        df = df.head(max_rows)
    return df

def generate_chart(csv_path, chart_file):
    if not csv_path.exists():
        print(f"CSV for chart not found: {csv_path}")
        return
    df = pd.read_csv(csv_path)
    if "ip" not in df.columns or "count" not in df.columns:
        print(f"CSV missing 'ip' or 'count' columns: {csv_path}")
        return

    # Map color by count for severity-style effect
    df_sorted = df.sort_values("count", ascending=False)
    colors = plt.cm.Reds(df_sorted["count"] / df_sorted["count"].max())

    plt.figure(figsize=(8, 4))
    plt.bar(df_sorted["ip"], df_sorted["count"], color=colors, edgecolor="black")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Count")
    plt.title("Top Source IP Activity")
    plt.tight_layout()
    chart_file.parent.mkdir(exist_ok=True, parents=True)
    plt.savefig(chart_file)
    plt.close()

def dataframe_to_markdown(df):
    return df.to_markdown(index=False)

def generate_readme():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # Load data
    iocs_df = read_and_trim_csv(IOCS_CSV)
    vuln_df = read_and_trim_csv(VULN_CSV)

    # Generate chart
    generate_chart(Path("iocs/top_source_ips.csv"), CHART_FILE)

    # Markdown sections
    readme_md = f"""# Network Threat Intelligence Analysis

📊 **Automated Defensive Network Analysis with OSINT Enrichment and Threat Correlation**

---

## 🗂 Overview
This repository demonstrates a **Blue Team–focused** approach to analyzing network activity,  
open-source threat intelligence, and vulnerability data in support of defensive operations.

---

## 🔍 Analytical Focus
- Understand network behavior and traffic patterns
- Contextualize activity using OSINT
- Correlate indicators with observed network insights
- Prioritize risk for informed defensive actions

---

## 📈 Operational Outputs
- Analyst-ready intelligence artifacts
- Correlated threat indicators
- Visual summaries of network activity
- Written summaries for briefings

---

## ⚙️ Automation & Design
Automated workflows for consistency and repeatability, keeping final conclusions **analyst-driven**.

---

## 🛡️ Daily Analysis Snapshot
> This section is dynamically updated.  

**Timestamp (UTC):** {timestamp}

### 🔎 Observed Threat Indicators (OSINT)
These are external intelligence indicators collected from open sources relevant to network defense.
{dataframe_to_markdown(iocs_df)}

### ⚠️ High-Risk Vulnerabilities
These are vulnerabilities detected on monitored hosts, sorted from most critical to least.
{dataframe_to_markdown(vuln_df)}

### 📊 Network Activity Chart
![Top Source IPs Activity]({CHART_FILE})

*Chart shows top source IPs by activity count.*
"""

    with open(README_FILE, "w") as f:
        f.write(readme_md)
    print(f"README updated: {README_FILE}")

if __name__ == "__main__":
    generate_readme()
