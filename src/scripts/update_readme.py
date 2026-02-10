from pathlib import Path
import pandas as pd
from datetime import datetime

README = Path("README.md")

IOCS = Path("build/iocs/osint_iocs.csv")
VULNS = Path("build/vulnerabilities/vuln_scan_sample.csv")
CHART = "build/charts/network_activity.png"

START = "<!-- AUTO-GENERATED-START -->"
END = "<!-- AUTO-GENERATED-END -->"


def table(df):
    return df.to_markdown(index=False)


def generate_readme():
    iocs_df = pd.read_csv(IOCS)
    vulns_df = pd.read_csv(VULNS)

    # 🔽 Curated SOC-style views (CSV stays full)
    top_iocs = (
        iocs_df
        .sort_values("confidence", ascending=False)
        .head(12)
    )

    top_vulns = (
        vulns_df
        .sort_values("risk_score", ascending=False)
        .head(10)
    )

    block = f"""
{START}

## 📌 Daily Threat Intelligence Snapshot
**Generated (UTC):** {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}

### 🛰️ High-Confidence Threat Indicators
Curated indicators prioritized by confidence and relevance.
This view highlights the most actionable threats observed during this cycle.

{table(top_iocs)}

### 🔥 Highest-Risk Vulnerabilities
Vulnerabilities prioritized by calculated risk score, reflecting exploitability
and potential operational impact.

{table(top_vulns)}

### 📊 Network Activity Overview
![Network Threat Activity]({CHART})

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
