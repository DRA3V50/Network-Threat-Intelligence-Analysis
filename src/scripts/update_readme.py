#!/usr/bin/env python3
# update_readme.py
# Updates README.md with latest threat intelligence snapshot

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# -------------------------------
# Paths
# -------------------------------
REPO_ROOT = Path(__file__).parent.parent.parent  # go up to repo root
BUILD_DIR = REPO_ROOT / "build"
IOCS_CSV = BUILD_DIR / "iocs/osint_iocs.csv"
VULNS_CSV = BUILD_DIR / "vulnerabilities/vuln_scan_sample.csv"
OUTPUTS_DIR = REPO_ROOT / "outputs"
CHARTS_DIR = OUTPUTS_DIR / "charts"
README_PATH = REPO_ROOT / "README.md"

# -------------------------------
# Parameters
# -------------------------------
MAX_ROWS = 8  # max rows to show in README for tables

# -------------------------------
# Functions
# -------------------------------
def generate_chart(csv_file, chart_file):
    df = pd.read_csv(csv_file)
    if "ip" not in df.columns or "count" not in df.columns:
        print("CSV missing 'ip' or 'count' columns, skipping chart.")
        return

    top = df.head(MAX_ROWS)

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(top["ip"], top["count"], color="red", edgecolor="white")
    ax.set_xlabel("Source IP")
    ax.set_ylabel("Count")
    ax.set_title("Top Source IPs")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    chart_file.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(chart_file, dpi=150)
    plt.close()

def format_table(df):
    df = df.head(MAX_ROWS)
    return df.to_markdown(index=False)

# -------------------------------
# Load Data
# -------------------------------
try:
    iocs_df = pd.read_csv(IOCS_CSV)
except FileNotFoundError:
    iocs_df = pd.DataFrame(columns=["ioc_type", "ioc_value", "confidence", "source"])
    print(f"Warning: {IOCS_CSV} not found. Empty IOC table used.")

try:
    vulns_df = pd.read_csv(VULNS_CSV)
except FileNotFoundError:
    vulns_df = pd.DataFrame(columns=["vuln_id", "cve", "severity", "risk_score", "affected_host"])
    print(f"Warning: {VULNS_CSV} not found. Empty vulnerabilities table used.")

# Generate chart for top source IPs
top_ips_csv = BUILD_DIR / "charts/top_source_ips.csv"  # keep CSV source
chart_file = CHARTS_DIR / "top_source_ips.png"
if top_ips_csv.exists():
    generate_chart(top_ips_csv, chart_file)
else:
    print(f"Warning: {top_ips_csv} not found. Skipping chart.")

# -------------------------------
# Build auto-generated section
# -------------------------------
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

auto_section = f"""<!-- AUTO-GENERATED-SECTION:START -->

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** {timestamp}

#### 🧪 Top OSINT IOCs
{format_table(iocs_df)}

#### 🔴 High-Risk Vulnerabilities
{format_table(vulns_df)}

#### 📈 Network Activity Chart
![Top Source IPs Chart](outputs/charts/top_source_ips.png)

*This summary is auto-generated.*

<!-- AUTO-GENERATED-SECTION:END -->
"""

# -------------------------------
# Update README
# -------------------------------
if README_PATH.exists():
    readme_text = README_PATH.read_text()
    if "<!-- AUTO-GENERATED-SECTION:START -->" in readme_text:
        start = readme_text.index("<!-- AUTO-GENERATED-SECTION:START -->")
        end = readme_text.index("<!-- AUTO-GENERATED-SECTION:END -->") + len("<!-- AUTO-GENERATED-SECTION:END -->")
        readme_text = readme_text[:start] + auto_section + readme_text[end:]
    else:
        # append at the end if not present
        readme_text += "\n\n" + auto_section
    README_PATH.write_text(readme_text)
    print("README.md updated successfully.")
else:
    print(f"README.md not found at {README_PATH}")
