import pandas as pd
import matplotlib.pyplot as plt
import random
from pathlib import Path
import re
from datetime import datetime

# ----------------------------
# Configuration
# ----------------------------
BUILD_DIR = Path("build")
IOCS_CSV = BUILD_DIR / "iocs/osint_iocs.csv"
VULNS_CSV = BUILD_DIR / "vulnerabilities/vuln_scan_sample.csv"
CHARTS_DIR = Path("outputs/charts")
README_FILE = Path("README.md")

# Ensure chart directory exists
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------
# Functions
# ----------------------------
def limit_rows(df, min_rows=3, max_rows=10, sort_column=None):
    """Sort by column descending and limit to random rows between min_rows and max_rows."""
    if sort_column:
        df = df.sort_values(by=sort_column, ascending=False)
    n_rows = random.randint(min_rows, max_rows)
    return df.head(n_rows)

def generate_bar_chart(df, x_col, y_col, chart_file, title):
    plt.figure(figsize=(6, 4))
    plt.bar(df[x_col], df[y_col], color="red", edgecolor="white")
    plt.xticks(rotation=45, ha="right")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(chart_file)
    plt.close()

def dataframe_to_markdown(df):
    """Convert a DataFrame to a markdown table string."""
    return df.to_markdown(index=False)

# ----------------------------
# Load & process CSVs
# ----------------------------
# Load OSINT IOCs
iocs_df = pd.read_csv(IOCS_CSV)
iocs_df = limit_rows(iocs_df, min_rows=3, max_rows=10, sort_column="confidence")
iocs_df.to_csv(IOCS_CSV, index=False)  # overwrite with limited rows

# Load Vulnerabilities
vulns_df = pd.read_csv(VULNS_CSV)
vulns_df = limit_rows(vulns_df, min_rows=3, max_rows=10, sort_column="risk_score")
vulns_df.to_csv(VULNS_CSV, index=False)  # overwrite with limited rows

# ----------------------------
# Generate chart
# ----------------------------
top_ips_csv = BUILD_DIR / "top_source_ips.csv"
if top_ips_csv.exists():
    top_ips_df = pd.read_csv(top_ips_csv)
    top_ips_df = limit_rows(top_ips_df, min_rows=3, max_rows=10, sort_column="count")
    chart_file = CHARTS_DIR / "top_source_ips.png"
    generate_bar_chart(top_ips_df, "ip", "count", chart_file, "Top Source IPs Chart")
else:
    chart_file = None

# ----------------------------
# Prepare README content
# ----------------------------
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# Markdown tables
iocs_table = dataframe_to_markdown(iocs_df)
vulns_table = dataframe_to_markdown(vulns_df)

chart_markdown = f"![Top Source IPs Chart]({chart_file})" if chart_file else "No chart available"

new_section = f"""<!-- AUTO-GENERATED-SECTION:START -->

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** {timestamp}

#### 🌐 Top OSINT IOCs
{iocs_table}

#### 🔴 High-Risk Vulnerabilities
{vulns_table}

#### 📈 Network Activity Chart
{chart_markdown}

*This summary is auto-generated.*

<!-- AUTO-GENERATED-SECTION:END -->
"""

# ----------------------------
# Update README
# ----------------------------
if README_FILE.exists():
    readme_content = README_FILE.read_text()
    # Replace existing section or append if not found
    if "<!-- AUTO-GENERATED-SECTION:START -->" in readme_content:
        updated_content = re.sub(
            r"<!-- AUTO-GENERATED-SECTION:START -->.*?<!-- AUTO-GENERATED-SECTION:END -->",
            new_section,
            readme_content,
            flags=re.DOTALL
        )
    else:
        updated_content = readme_content + "\n" + new_section

    README_FILE.write_text(updated_content)
    print("README updated successfully.")
else:
    print("README.md not found.")
