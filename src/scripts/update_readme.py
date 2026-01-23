from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import random

# Paths
BUILD_DIR = Path("build")
OUTPUTS_DIR = Path("outputs")
CHARTS_DIR = OUTPUTS_DIR / "charts"
README_PATH = Path("README.md")

CHARTS_DIR.mkdir(parents=True, exist_ok=True)

# Max/min rows to show in README
MAX_ROWS = 8
MIN_ROWS = 3

def sample_rows(df: pd.DataFrame, min_rows=MIN_ROWS, max_rows=MAX_ROWS):
    """Return a random sample between min_rows and max_rows."""
    n_rows = random.randint(min_rows, max_rows)
    return df.head(n_rows)  # or random.sample if you prefer shuffle

# 1️⃣ Top Source IPs Chart
top_ips_csv = BUILD_DIR / "pcaps" / "top_source_ips.csv"
if not top_ips_csv.exists():
    raise FileNotFoundError(f"{top_ips_csv} not found. Make sure the workflow generates it.")

top_ips_df = pd.read_csv(top_ips_csv)
top_ips_display = sample_rows(top_ips_df)

# Generate chart with dark / red-white theme
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(top_ips_display['source_ip'], top_ips_display['count'], color=['red', 'white'])
ax.set_xlabel("Source IP")
ax.set_ylabel("Count")
ax.set_title("Top Source IPs")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
chart_path = CHARTS_DIR / "top_source_ips.png"
plt.savefig(chart_path)
plt.close(fig)

# 2️⃣ OSINT IOCs Table
iocs_csv = BUILD_DIR / "iocs" / "osint_iocs.csv"
iocs_df = pd.read_csv(iocs_csv)
iocs_display = sample_rows(iocs_df)

# 3️⃣ Vulnerabilities Table
vulns_csv = BUILD_DIR / "vulnerabilities" / "vuln_scan_sample.csv"
vulns_df = pd.read_csv(vulns_csv)
vulns_display = sample_rows(vulns_df)

# Convert to Markdown
def df_to_md_table(df: pd.DataFrame) -> str:
    return df.to_markdown(index=False)

iocs_md = df_to_md_table(iocs_display)
vulns_md = df_to_md_table(vulns_display)

# Timestamp
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# Auto-generated block
auto_block = f"""
<!-- AUTO-GENERATED-SECTION:START -->

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** {timestamp}

<table>
<tr>
<td width="50%">

#### 🔴 High-Risk Vulnerabilities
{vulns_md}

</td>
<td width="50%">

#### 🧪 Top OSINT IOCs
{iocs_md}

</td>
</tr>
<tr>
<td colspan="2" align="center">

#### 📈 Network Activity Chart
<img src="{chart_path.as_posix()}" alt="Top Source IPs Chart" width="600">

</td>
</tr>
</table>

*This summary is auto-generated.*

<!-- AUTO-GENERATED-SECTION:END -->
"""

# Update README.md between markers
readme_text = README_PATH.read_text()
start_marker = "<!-- AUTO-GENERATED-SECTION:START -->"
end_marker = "<!-- AUTO-GENERATED-SECTION:END -->"

if start_marker in readme_text and end_marker in readme_text:
    pre = readme_text.split(start_marker)[0]
    post = readme_text.split(end_marker)[1]
    new_readme = f"{pre}{auto_block}{post}"
else:
    new_readme = readme_text + "\n" + auto_block

README_PATH.write_text(new_readme)
print(f"[+] README.md updated successfully at {timestamp}")
