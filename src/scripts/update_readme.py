from datetime import datetime
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Paths
BUILD_DIR = Path("build")
OUTPUT_DIR = Path("outputs/logs")
CHARTS_DIR = Path("outputs/charts")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

# Auto-generated section markers in README
AUTO_START = "<!-- AUTO-GENERATED-SECTION:START -->"
AUTO_END = "<!-- AUTO-GENERATED-SECTION:END -->"

# Limit for inline tables
TOP_N = 5

# Read data
vulns_df = pd.read_csv(BUILD_DIR / "vulnerabilities" / "vuln_scan_sample.csv").head(TOP_N)
iocs_df = pd.read_csv(BUILD_DIR / "iocs" / "osint_iocs.csv").head(TOP_N)
logs_df = pd.read_csv(OUTPUT_DIR / "high_risk_vulns.csv").head(TOP_N)

# Generate Resident Evil style chart (dark background, red bars)
top_ips_df = pd.read_csv(CHARTS_DIR / "top_source_ips.csv")  # assuming this exists
plt.style.use('dark_background')
plt.figure(figsize=(6, 4))
plt.bar(top_ips_df['source_ip'], top_ips_df['count'], color='red', edgecolor='white')
plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(color='white')
plt.ylabel("Connections", color='white')
plt.title("Top Source IPs", color='white')
plt.tight_layout()
chart_file = CHARTS_DIR / "top_source_ips.png"
plt.savefig(chart_file, dpi=100)
plt.close()

# Generate Markdown for auto-section
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

md_vulns = vulns_df.to_markdown(index=False)
md_iocs = iocs_df.to_markdown(index=False)
md_logs = logs_df.to_markdown(index=False)

auto_section = f"""
{AUTO_START}

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** {timestamp}

<table>
<tr>
<td width="50%">

#### 🔴 High-Risk Vulnerabilities
{md_vulns}

</td>
<td width="50%">

#### 🧪 Top OSINT IOCs
{md_iocs}

</td>
</tr>
<tr>
<td colspan="2" align="center">

#### 📈 Network Activity Chart
<img src="outputs/charts/top_source_ips.png" alt="Top Source IPs Chart" width="600">

</td>
</tr>
</table>

*This summary is auto-generated.*

{AUTO_END}
"""

# Read current README
readme_file = Path("README.md")
readme_text = readme_file.read_text()

# Replace old auto-generated section
import re
pattern = re.compile(f"{AUTO_START}.*?{AUTO_END}", re.DOTALL)
if pattern.search(readme_text):
    readme_text = pattern.sub(auto_section, readme_text)
else:
    # Append if missing
    readme_text += "\n" + auto_section

# Save updated README
readme_file.write_text(readme_text)
print(f"[+] README.md updated successfully at {timestamp}")
