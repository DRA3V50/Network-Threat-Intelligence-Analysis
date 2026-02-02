from pathlib import Path
import pandas as pd
from datetime import datetime

README = Path("README.md")

IOCS = Path("build/iocs/osint_iocs.csv")
VULNS = Path("build/vulnerabilities/vuln_scan_sample.csv")
CHART = Path("build/charts/network_activity.png")

START = "<!-- AUTO-GENERATED-START -->"
END = "<!-- AUTO-GENERATED-END -->"

IOC_ROWS = 10
VULN_ROWS = 10


def render_table(df, sort_col, rows):
    df = df.sort_values(sort_col, ascending=False)
    df = df.head(rows)
    return df.to_markdown(index=False)


def update_readme():
    iocs_df = pd.read_csv(IOCS)
    vulns_df = pd.read_csv(VULNS)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    block = f"""
{START}

## 📌 Daily Threat Intelligence Snapshot

**Generated:** {timestamp}  
**Execution:** Automated CI pipeline (multiple daily runs)

This section is regenerated automatically from pipeline outputs.  
Displayed tables are **curated summaries** — full datasets are preserved
in build artifacts for analysis and auditing.

---

### 🛰️ High-Confidence Threat Indicators (Top {IOC_ROWS})

Ranked by confidence score.

{render_table(iocs_df, "confidence", IOC_ROWS)}

---

### 🔥 Highest-Risk Vulnerabilities (Top {VULN_ROWS})

Ranked by calculated risk score.

{render_table(vulns_df, "risk_score", VULN_ROWS)}

---

### 📊 Correlated Network Threat Activity

The visualization below correlates:
- Network source activity
- Vulnerability severity distribution
- High-confidence IOC prevalence

![Unified Network Threat Activity]({CHART.as_posix()})

{END}
"""

    text = README.read_text()

    if START in text and END in text:
        text = text.split(START)[0] + block + text.split(END)[1]
    else:
        text += "\n\n" + block

    README.write_text(text)


if __name__ == "__main__":
    update_readme()
