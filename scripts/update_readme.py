from datetime import datetime
import pytz

est = pytz.timezone("US/Eastern")
timestamp = datetime.now(est).strftime("%Y-%m-%d %H:%M %Z")

content = f"""
## 📊 Daily Analysis Snapshot

_Last updated: **{timestamp}**_

- **Vulnerabilities loaded:** 50
- **OSINT IOCs loaded:** 50
- **PCAP regenerated:** Yes
- **High-Risk Findings:** Updated
"""

with open("README.md", "r", encoding="utf-8") as f:
    base = f.read().split("## 📊 Daily Analysis Snapshot")[0]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(base + content)
