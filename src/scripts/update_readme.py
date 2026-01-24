import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

# --- Config Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent
BUILD_DIR = BASE_DIR / "build"
IOCS_CSV = BUILD_DIR / "iocs" / "osint_iocs.csv"
VULN_CSV = BUILD_DIR / "vulnerabilities" / "vuln_scan_sample.csv"
CHARTS_DIR = BASE_DIR / "outputs" / "charts"
README_FILE = BASE_DIR / "README.md"

CHARTS_DIR.mkdir(parents=True, exist_ok=True)

# --- Parameters ---
MAX_ROWS = 10  # max rows to show in files & README

# --- Helper: Generate Bar Chart ---
def generate_chart(df, col_label, value_label, chart_file, title, color="red"):
    # Aggregate if necessary
    chart_data = df.groupby(col_label)[value_label].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    chart_data.plot(kind="bar", color=color, edgecolor="white")
    plt.title(title)
    plt.ylabel(value_label)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(chart_file)
    plt.close()

# --- Read CSVs ---
iocs_df = pd.read_csv(IOCS_CSV)
vulns_df = pd.read_csv(VULN_CSV)

# --- Limit to MAX_ROWS sorted by severity/risk ---
severity_order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
vulns_df["severity_rank"] = vulns_df["severity"].map(severity_order)
vulns_df = vulns_df.sort_values(by="severity_rank", ascending=False).head(MAX_ROWS)

iocs_df = iocs_df.sort_values(by="confidence", ascending=False).head(MAX_ROWS)

# --- Add emojis to IOC types ---
emoji_map = {"IP": "🌐", "DOMAIN": "🔗", "HASH": "🔒", "URL": "🔗"}
iocs_df["emoji"] = iocs_df["ioc_type"].map(emoji_map)

# --- Write trimmed CSVs back to build folders ---
iocs_df.to_csv(IOCS_CSV, index=False)
vulns_df.to_csv(VULN_CSV, index=False)

# --- Generate Network Activity Chart (example: top IPs by confidence) ---
top_ips_df = iocs_df[iocs_df["ioc_type"] == "IP"].copy()
top_ips_df["count"] = 1  # simple count per IP
chart_file = CHARTS_DIR / "top_source_ips.png"
generate_chart(top_ips_df, "ioc_value", "count", chart_file, "Top Source IPs Chart")

# --- Generate Markdown tables ---
def df_to_md_table(df, columns):
    md = "| " + " | ".join(columns) + " |\n"
    md += "| " + " | ".join([":---:" for _ in columns]) + " |\n"
    for _, row in df.iterrows():
        md += "| " + " | ".join(str(row[col]) for col in columns) + " |\n"
    return md

# IOC table with emoji
iocs_md = df_to_md_table(iocs_df, ["emoji", "ioc_type", "ioc_value", "confidence", "source"])

# Vulnerabilities table
vulns_md = df_to_md_table(vulns_df, ["vuln_id", "cve", "severity", "risk_score", "affected_host"])

# --- Update README ---
with open(README_FILE, "r") as f:
    readme = f.read()

auto_section = f"""
<!-- AUTO-GENERATED-SECTION:START -->

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}

#### 🧪 Top OSINT IOCs
{iocs_md}

#### 🔴 High-Risk Vulnerabilities
{vulns_md}

#### 📈 Network Activity Chart
![Top Source IPs Chart](outputs/charts/top_source_ips.png)

*This summary is auto-generated.*

<!-- AUTO-GENERATED-SECTION:END -->
"""

# Replace previous auto section or append if missing
if "<!-- AUTO-GENERATED-SECTION:START -->" in readme:
    readme = readme.split("<!-- AUTO-GENERATED-SECTION:START -->")[0] + auto_section
else:
    readme += "\n" + auto_section

with open(README_FILE, "w") as f:
    f.write(readme)

print("README and build files updated successfully!")
