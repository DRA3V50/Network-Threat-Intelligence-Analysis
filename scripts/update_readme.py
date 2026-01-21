# scripts/update_readme.py
from datetime import datetime

def update_readme(stats: dict):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    content = f"""# Network-Threat-Intelligence-Analysis

📊 Automated defensive network analysis with OSINT enrichment and threat correlation

---

## 📊 Daily Automated Threat Intelligence Update

**Last updated:** {timestamp}

- **OSINT IOCs loaded:** {stats["ioc_count"]}
- **Packets analyzed:** {stats["packet_count"]}
- **IOC Matches:** {stats["matches"]}
- **High-Risk Vulnerabilities:** {stats["high_risk"]}

---

## 📈 Top Source IPs

![Top Source IPs](outputs/charts/top_source_ips.png)

---

## ⚠️ Legal & Ethical Notice

This project is strictly defensive.  
All data is simulated or derived from public OSINT.
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
