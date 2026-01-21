import csv
from pathlib import Path

# Paths
matched_iocs_path = Path("outputs/reports/matched_iocs.csv")
high_risk_vulns_path = Path("outputs/reports/high_risk_vulns.csv")
top_source_ips_path = Path("outputs/logs/top_source_ips.csv")
readme_path = Path("README.md")

# Count entries dynamically
vuln_count = sum(1 for _ in open("build/vulnerabilities/vuln_scan_sample.csv")) - 1
ioc_count = sum(1 for _ in open("build/iocs/osint_iocs.csv")) - 1
pcap_generated = Path("build/pcaps/sample_traffic.pcap").exists()
top_ips_count = sum(1 for _ in open(top_source_ips_path)) - 1 if top_source_ips_path.exists() else 0
high_risk_count = sum(1 for _ in open(high_risk_vulns_path)) - 1 if high_risk_vulns_path.exists() else 0

# Read README template up to marker
template_lines = []
with open(readme_path) as f:
    for line in f:
        template_lines.append(line)
        if "## 📊 Daily Analysis Snapshot" in line:
            break

# Build dynamic summary
dynamic_summary = f"""
### **Daily Automated Threat Intelligence Update**

- **Vulnerabilities loaded:** {vuln_count}
- **OSINT IOCs loaded:** {ioc_count}
- **Sample PCAP generated:** {"Yes" if pcap_generated else "No"}
- **Top Source IPs:** {top_ips_count}
- **High-Risk Vulnerabilities:** {high_risk_count}

*This summary is auto-generated.*
"""

# Read remaining static content after previous snapshot (if any)
remaining_lines = []
skip = True
with open(readme_path) as f:
    for line in f:
        if skip:
            if "## 📊 Daily Analysis Snapshot" in line:
                skip = False
        else:
            remaining_lines.append(line)

# Write back README
with open(readme_path, "w") as f:
    f.writelines(template_lines)
    f.write(dynamic_summary)
    f.writelines(remaining_lines)
