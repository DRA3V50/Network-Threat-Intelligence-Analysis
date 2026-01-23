#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import random
from datetime import datetime

# ---------------------------
# CONFIG
# ---------------------------
README_PATH = Path(__file__).parent.parent / "README.md"
BUILD_DIR = Path(__file__).parent.parent / "build"
OUTPUTS_DIR = Path(__file__).parent.parent / "outputs"
CHARTS_DIR = OUTPUTS_DIR / "charts"

IOCS_CSV = BUILD_DIR / "iocs/osint_iocs.csv"
VULNS_CSV = BUILD_DIR / "vulnerabilities/vuln_scan_sample.csv"

SECTION_START = "<!-- AUTO-GENERATED-SECTION:START -->"
SECTION_END = "<!-- AUTO-GENERATED-SECTION:END -->"

# Number of rows to show in README tables
MIN_ROWS = 3
MAX_ROWS = 8

# Chart settings
CHART_FILE = CHARTS_DIR / "top_source_ips.png"
CHART_WIDTH = 8
CHART_HEIGHT = 4
CHART_BG_COLOR = "#111111"  # dark background
BAR_COLOR = "#FF0000"       # red bars
EDGE_COLOR = "white"

# ---------------------------
# HELPER FUNCTIONS
# ---------------------------
def limit_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Return a random selection of 3-8 rows for display in README"""
    n = random.randint(MIN_ROWS, min(MAX_ROWS, len(df)))
    return df.sample(n=n, random_state=42)

def generate_chart(csv_file: Path, output_file: Path):
    """Generate a bar chart for top source IPs"""
    if not csv_file.exists():
        print(f"Chart CSV {csv_file} does not exist. Skipping chart.")
        return

    df = pd.read_csv(csv_file)
    # If the CSV has 'ip' and 'count' columns
    if "ip" not in df.columns or "count" not in df.columns:
        print(f"CSV {csv_file} missing required columns 'ip' and 'count'. Skipping chart.")
        return

    top = df.sort_values("count", ascending=False).head(10)

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(CHART_WIDTH, CHART_HEIGHT))
    fig.patch.set_facecolor(CHART_BG_COLOR)
    ax.set_facecolor(CHART_BG_COLOR)
    ax.bar(top["ip"], top["count"], color=BAR_COLOR, edgecolor=EDGE_COLOR)
    ax.set_title("Top Source IPs", color="white")
    ax.set_ylabel("Connections", color="white")
    ax.set_xticklabels(top["ip"], rotation=45, ha="right", color="white")
    ax.tick_params(axis="y", colors="white")
    plt.tight_layout()
    output_file.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_file, dpi=120)
    plt.close()
    print(f"Chart saved to {output_file}")

def df_to_markdown(df: pd.DataFrame) -> str:
    """Convert a DataFrame to a Markdown table string"""
    return df.to_markdown(index=False)

# ---------------------------
# MAIN
# ---------------------------

# Load CSVs
iocs_df = pd.read_csv(IOCS_CSV)
vulns_df = pd.read_csv(VULNS_CSV)

# Limit rows for README display
iocs_limited = limit_rows(iocs_df)
vulns_limited = limit_rows(vulns_df)

# Generate chart
TOP_IPS_CSV = CHARTS_DIR / "top_source_ips.csv"
generate_chart(TOP_IPS_CSV, CHART_FILE)

# Prepare Markdown section
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
auto_generated_section = f"""
{SECTION_START}

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** {timestamp}

#### 🧪 Top OSINT IOCs
{iocs_limited.to_markdown(index=False)}

#### 🔴 High-Risk Vulnerabilities
{vulns_limited.to_markdown(index=False)}

#### 📈 Network Activity Chart
![Top Source IPs Chart]({CHART_FILE})

*This summary is auto-generated.*

{SECTION_END}
"""

# Read README
readme_content = README_PATH.read_text(encoding="utf-8")

# Remove old auto-generated section
if SECTION_START in readme_content and SECTION_END in readme_content:
    before = readme_content.split(SECTION_START)[0]
    after = readme_content.split(SECTION_END)[1]
    readme_content = before + after

# Append new auto-generated section at the end
readme_content += "\n\n" + auto_generated_section

# Write updated README
README_PATH.write_text(readme_content, encoding="utf-8")
print("README.md updated successfully.")
