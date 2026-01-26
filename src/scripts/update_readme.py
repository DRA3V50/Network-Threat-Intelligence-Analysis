from pathlib import Path
import pandas as pd
from datetime import datetime

README = Path("README.md")

IOCS = Path("build/iocs/osint_iocs.csv")
VULNS = Path("build/vulnerabilities/vuln_scan_sample.csv")
CHART = "build/charts/top_source_ips.csv"

START = "<!-- AUTO-GENERATED-START -->"
END = "<!-- AUTO-GENERATED-END -->"

def table(df):
    return df.to_markdown(index=False)

def generate_readme():
    iocs_df = pd.read_csv(IOCS)
    vulns_df = pd.read_csv(VULNS)

    block = f"""
{START}

## 📌 Daily Threat Intelligence Snapshot
**Generated (UTC):** {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

{table(iocs_df)}

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

{table(vulns_df)}

### 📊 Network Activity Overview
![Top Source IPs]({CHART})

{END}
"""

    text = README.read_text() if README.exists() else ""
    if START in text and END in text:
        text = text.split(START)[0] + block + text.split(END)[1]
    else:
        text += "\n" + block

    README.write_text(text)

if __name__ == "__main__":
    generate_readme()
