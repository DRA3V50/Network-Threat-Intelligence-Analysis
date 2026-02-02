from pathlib import Path
import pandas as pd
from datetime import datetime

README = Path("README.md")

IOCS = Path("build/iocs/osint_iocs.csv")
VULNS = Path("build/vulnerabilities/vuln_scan_sample.csv")
CHART = Path("build/charts/network_activity.png")

START = "<!-- AUTO-GENERATED-START -->"
END = "<!-- AUTO-GENERATED-END -->"


def table(df, max_rows=15):
    """
    Limit table size for readability in README while
    preserving full datasets in build artifacts.
    """
    if len(df) > max_rows:
        df = df.head(max_rows)
    return df.to_markdown(index=False)


def generate_readme():
    iocs_df = pd.read_csv(IOCS)
    vulns_df = pd.read_csv(VULNS)

    generated_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    block = f"""
{START}

## 📌 Automated Threat Intelligence Snapshot

**Last Generated:** {generated_time}  
**Update Cadence:** Automated (multiple daily executions via CI pipeline)

This section is automatically generated from the latest pipeline outputs.
All data is derived from simulated sources and is intended for research,
demonstration, and portfolio purposes only.

---

### 🛰️ High-Confidence Threat Indicators (IOCs)

Curated indicators aggregated from open-source intelligence feeds and
confidence-scored during ingestion.

> Displaying most recent indicators (truncated for readability)

{table(iocs_df)}

---

### 🔥 Highest-Risk Vulnerabilities

Vulnerabilities prioritized based on relative severity, exploitability,
and potential operational impact.

> Displaying highest-severity findings (truncated for readability)

{table(vulns_df)}

---

### 📊 Unified Network Activity Visualization

This visualization correlates:
- Observed network source activity (PCAP analysis)
- Vulnerability severity distribution
- High-confidence IOC prevalence

The chart is regenerated automatically from the tables above.

![Unified Network Activity Overview]({CHART.as_posix()})

{END}
"""

    existing = README.read_text() if README.exists() else ""

    if START in existing and END in existing:
        updated = (
            existing.split(START)[0]
            + block
            + existing.split(END)[1]
        )
    else:
        updated = existing + "\n\n" + block

    README.write_text(updated)


if __name__ == "__main__":
    generate_readme()
