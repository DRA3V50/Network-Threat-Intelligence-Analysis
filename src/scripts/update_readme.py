import csv
from pathlib import Path

# ------------------------------
# Paths to files and folders
# ------------------------------
readme_file = Path("README.md")

iocs_file = Path("build/iocs/osint_iocs.csv")
vulns_file = Path("build/vulnerabilities/vuln_scan_sample.csv")
pcaps_file = Path("build/pcaps/sample_traffic.pcap")
top_ips_file = Path("build/pcaps/top_source_ips.csv")
chart_file = Path("outputs/charts/top_source_ips.png")
logs_dir = Path("outputs/logs")

# ------------------------------
# Helper functions
# ------------------------------
def csv_row_count(file_path: Path):
    if file_path.exists():
        with open(file_path, newline='') as f:
            return sum(1 for _ in csv.reader(f)) - 1  # subtract header
    return 0

# ------------------------------
# Gather dynamic data
# ------------------------------
iocs_count = csv_row_count(iocs_file)
vulns_count = csv_row_count(vulns_file)
top_ips_count = csv_row_count(top_ips_file)
pcap_generated = pcaps_file.exists()
chart_exists = chart_file.exists()
logs_files = list(logs_dir.glob("*.csv")) if logs_dir.exists() else []

# ------------------------------
# Build README content
# ------------------------------
readme_content = f"""# Network-Threat-Intelligence-Analysis

📊 Automated defensive network analysis with OSINT enrichment and threat correlation

---

📡 Defensive network intelligence research and automation for security operations and analytic environments.

---

## 🗂 Overview

This repository demonstrates a Blue Team–focused approach to analyzing network activity,  
open-source threat intelligence, and vulnerability data in support of defensive cyber operations.  
The emphasis is on **analytical reasoning, correlation of intelligence, and repeatable workflows**,  
reflecting how network-centric threat intelligence informs operational decision-making.

---

## 🔍 Analytical Focus

Designed to support:

- Understanding network behavior and traffic patterns  
- Applying OSINT to contextualize observed activity  
- Correlating indicators of compromise with network-derived insights  
- Prioritizing risk to support informed defensive actions  

The goal is **clarity, attribution context, and defensibility**, not detection for its own sake.

---

## 📈 Operational Outcomes

Execution produces:

- Analyst-ready intelligence artifacts  
- Correlated threat indicators to guide mitigation  
- High-level visualizations summarizing network activity trends  
- Written summaries aligned with reporting and briefing standards  

Outputs are designed to provide **actionable insight for analysts and decision-makers**.

---

## ⚙️ Automation & Design

Analysis workflows are automated for consistency and repeatability while keeping final conclusions analyst-driven.  
Workflows mirror operational environments where **traceability, documentation, and discipline** are required.

---

## 🛡️ Intended Use

This repository is designed for:

- Defensive cybersecurity professionals  
- Threat intelligence analysts  
- Security operations teams in government, federal, or mission-driven organizations  

It demonstrates workflows, analysis methods, and outputs that **enable informed decision-making, operational awareness, and risk-based defense**.

---

## 📊 Daily Analysis Snapshot

> This section is dynamically updated by automated workflows.

### **Daily Automated Threat Intelligence Update**

- **Vulnerabilities loaded:** {vulns_count}
- **OSINT IOCs loaded:** {iocs_count}
- **Sample PCAP generated:** {"Yes" if pcap_generated else "No"}
- **Top Source IPs:** {top_ips_count}

![Top Source IPs Chart]({chart_file if chart_exists else ""})

*This summary is auto-generated.*

---

### **Generated Files and Outputs**

#### **Reports:**
- **[{iocs_file.name}]({iocs_file})**
- **[{vulns_file.name}]({vulns_file})**

#### **Chart:**
{"![Top Source IPs Chart](" + str(chart_file) + ")" if chart_exists else "No chart generated yet."}

#### **Logs:**"""
for log_file in logs_files:
    readme_content += f"\n- **[{log_file.name}]({log_file})**"

# ------------------------------
# Legal notice
# ------------------------------
readme_content += """

---

## ⚠️ Legal & Ethical Notice

This project is strictly defensive:

- No exploitation, intrusion, or active scanning  
- Data is sanitized, simulated, or derived from public sources  
- Usage is limited to education, research, and lawful defensive analysis

---

## 🚨 Status

This repository is actively maintained and updated as part of an ongoing **network threat intelligence workflow**.  
Analysis artifacts, correlated indicators, and visual summaries are refreshed on a regular basis to reflect the latest defensive insights.  
The project demonstrates **repeatable, analyst-driven processes** consistent with operational security and intelligence standards.
"""

# ------------------------------
# Write README
# ------------------------------
readme_file.write_text(readme_content)
print("[+] README.md updated successfully.")
