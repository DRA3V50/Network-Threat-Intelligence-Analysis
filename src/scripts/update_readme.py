import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# -----------------------------
# Config Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
BUILD_DIR = BASE_DIR / "build"
IOCS_CSV = BUILD_DIR / "iocs/osint_iocs.csv"
VULNS_CSV = BUILD_DIR / "vulnerabilities/vuln_scan_sample.csv"
CHARTS_DIR = BASE_DIR / "outputs/charts"
CHARTS_DIR.mkdir(parents=True, exist_ok=True)
CHART_FILE = CHARTS_DIR / "top_source_ips.png"
README_FILE = BASE_DIR / "README.md"

# Max rows to show in both folder and README
MAX_ROWS = 10

# -----------------------------
# Read CSVs
# -----------------------------
iocs_df = pd.read_csv(IOCS_CSV)
vulns_df = pd.read_csv(VULNS_CSV)

# Keep only top N rows by severity / confidence
iocs_df = iocs_df.sort_values(by="confidence", ascending=False).head(MAX_ROWS)
vulns_df = vulns_df.sort_values(by="risk_score", ascending=False).head(MAX_ROWS)

# Save truncated CSVs back to build (folders and README match)
iocs_df.to_csv(IOCS_CSV, index=False)
vulns_df.to_csv(VULNS_CSV, index=False)

# -----------------------------
# Generate Network Chart
# -----------------------------
# Example: count top source IPs
if "ip" in iocs_df.columns:
    top_ips = iocs_df["ioc_value"].value_counts().head(MAX_ROWS)
    colors = []
    for i, row in iocs_df.iterrows():
        # Severity-based coloring for visualization
        if row["confidence"] >= 85:
            colors.append("#d32f2f")  # red = high
        elif row["confidence"] >= 70:
            colors.append("#f57c00")  # orange = medium
        else:
            colors.append("#fbc02d")  # yellow = low
    plt.figure(figsize=(8, 5))
    plt.bar(top_ips.index, top_ips.values, color=colors, edgecolor="black")
    plt.xticks(rotation=45, ha="right")
    plt.title("Network Traffic Summary by Top Source Indicators", fontsize=12)
    plt.ylabel("Occurrences")
    plt.tight_layout()
    plt.savefig(CHART_FILE)
    plt.close()

# -----------------------------
# Generate README Section
# -----------------------------
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

iocs_table_md = iocs_df.to_markdown(index=False)
vulns_table_md = vulns_df.to_markdown(index=False)

readme_content = f"""
# Network-Threat-Intelligence-Analysis

📊 Automated defensive network analysis with OSINT enrichment and threat correlation

---

## 🗂 Overview

This repository demonstrates a Blue Team–focused approach to analyzing network activity,  
open-source threat intelligence, and vulnerability data in support of defensive cyber operations.

---

## 📊 Daily Analysis Snapshot

> This section is dynamically updated by automated workflows.  
> **Do not edit content between the markers below.**

<!-- AUTO-GENERATED-SECTION:START -->

### Indicators of Compromise (OSINT) ⚠️
**Timestamp (UTC): {timestamp}**
{iocs_table_md}

### Critical & High-Risk Vulnerabilities 🛡️
**Timestamp (UTC): {timestamp}**
{vulns_table_md}

### Network Traffic Summary 🌐
![Network Traffic Summary](outputs/charts/top_source_ips.png)

*This summary is auto-generated.*

<!-- AUTO-GENERATED-SECTION:END -->
"""

# Write README
with open(README_FILE, "r") as f:
    existing = f.read()

# Replace old auto-generated section
import re
new_readme = re.sub(
    r"<!-- AUTO-GENERATED-SECTION:START -->.*<!-- AUTO-GENERATED-SECTION:END -->",
    readme_content,
    existing,
    flags=re.DOTALL,
)

with open(README_FILE, "w") as f:
    f.write(new_readme)

print("README and charts updated successfully.")
