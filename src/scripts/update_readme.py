from datetime import datetime
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import random
import re

# Paths
README_PATH = Path("README.md")
BUILD_DIR = Path("build")
OUTPUT_DIR = Path("outputs")
CHARTS_DIR = OUTPUT_DIR / "charts"

# Ensure dirs exist
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

# Settings
TRUNCATE_MIN, TRUNCATE_MAX = 3, 8  # rows for README display

# --- Helper functions --- #
def sample_rows(df):
    """Return a random sample of rows (between 3–8) for README display."""
    n = random.randint(TRUNCATE_MIN, min(TRUNCATE_MAX, len(df)))
    return df.sample(n=n)

def df_to_md(df):
    """Convert DataFrame to Markdown table."""
    return df.to_markdown(index=False)

def generate_chart(top_ips_csv, chart_path):
    """Generate dark Resident Evil style chart from top source IPs CSV."""
    df = pd.read_csv(top_ips_csv)
    top = df.head(10)
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(top["ip"], top["count"], color="red", edgecolor="white")
    ax.set_title("Top Source IPs", color="white")
    ax.set_xlabel("IP Address", color="white")
    ax.set_ylabel("Count", color="white")
    ax.tick_params(colors="white")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    fig.savefig(chart_path, dpi=150)
    plt.close(fig)

# --- Read CSVs --- #
iocs_df = pd.read_csv(BUILD_DIR / "iocs/osint_iocs.csv")
vulns_df = pd.read_csv(BUILD_DIR / "vulnerabilities/vuln_scan_sample.csv")
top_ips_csv = BUILD_DIR / "pcaps/top_source_ips.csv"

# --- Truncate for README --- #
iocs_md = df_to_md(sample_rows(iocs_df))
vulns_md = df_to_md(sample_rows(vulns_df))

# --- Generate chart --- #
chart_file = CHARTS_DIR / "top_source_ips.png"
if top_ips_csv.exists():
    generate_chart(top_ips_csv, chart_file)

# --- Auto-generated block --- #
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
auto_block = f"""
<!-- AUTO-GENERATED-SECTION:START -->

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** {timestamp}

#### 🔴 High-Risk Vulnerabilities (Sample)
{vulns_md}

#### 🧪 Top OSINT IOCs (Sample)
{iocs_md}

#### 📈 Network Activity Chart
<img src="{chart_file}" alt="Top Source IPs Chart" width="600">

*This summary is auto-generated.*

<!-- AUTO-GENERATED-SECTION:END -->
"""

# --- Update README --- #
if README_PATH.exists():
    readme_text = README_PATH.read_text()
    # Remove any old auto-generated blocks
    new_readme = re.sub(
        r'<!-- AUTO-GENERATED-SECTION:START -->.*?<!-- AUTO-GENERATED-SECTION:END -->',
        auto_block,
        readme_text,
        flags=re.DOTALL
    )
    README_PATH.write_text(new_readme)
    print("[*] README.md updated successfully.")
else:
    print("[!] README.md not found.")

