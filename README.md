# Network-Threat-Intelligence-Analysis

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
> **Do not edit content between the markers below.**




<!-- AUTO-GENERATED-SECTION:START -->

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** 2026-01-23 13:39 UTC

#### 🧪 Top OSINT IOCs
| ioc_type   | ioc_value                        |   confidence | source    |
|:-----------|:---------------------------------|-------------:|:----------|
| IP         | 185.32.164.40                    |           76 | OSINT-SIM |
| DOMAIN     | malicious322.com                 |           75 | OSINT-SIM |
| HASH       | 5aa47bc6cfa0234c6fb7bcbd86074644 |           78 | OSINT-SIM |
| IP         | 185.176.139.45                   |           64 | OSINT-SIM |
| URL        | http://bad807.example/path       |           95 | OSINT-SIM |
| DOMAIN     | malicious791.com                 |           73 | OSINT-SIM |
| DOMAIN     | malicious999.com                 |           65 | OSINT-SIM |
| DOMAIN     | malicious335.com                 |           67 | OSINT-SIM |

#### 🔴 High-Risk Vulnerabilities
| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1000 | CVE-2024-9679 | MEDIUM     |          5.9 | 192.168.1.9     |
| VULN-1001 | CVE-2024-3669 | LOW        |          8.2 | 192.168.1.65    |
| VULN-1002 | CVE-2024-4062 | LOW        |          6.1 | 192.168.1.232   |
| VULN-1003 | CVE-2024-9168 | MEDIUM     |          1.3 | 192.168.1.208   |
| VULN-1004 | CVE-2024-8862 | HIGH       |          3.9 | 192.168.1.191   |
| VULN-1005 | CVE-2024-7122 | LOW        |          5   | 192.168.1.93    |
| VULN-1006 | CVE-2024-8380 | MEDIUM     |          2.5 | 192.168.1.223   |
| VULN-1007 | CVE-2024-6742 | HIGH       |          5.5 | 192.168.1.162   |

#### 📈 Network Activity Chart
![Top Source IPs Chart](outputs/charts/top_source_ips.png)

*This summary is auto-generated.*

<!-- AUTO-GENERATED-SECTION:END -->






---

## 📁 Generated Files

### Reports
- **[OSINT IOCs](build/iocs/osint_iocs.csv)**
- **[Vulnerability Scan](build/vulnerabilities/vuln_scan_sample.csv)**

### Logs
- **[High Risk Vulnerabilities](outputs/logs/high_risk_vulns.csv)**

---

## ⚠️ Legal & Ethical Notice

This project is strictly defensive:

- No exploitation, intrusion, or active scanning  
- Data is sanitized, simulated, or derived from public sources  
- Usage is limited to education, research, and lawful defensive analysis

---

## 🚨 Status

This repository is actively maintained and updated as part of an ongoing  
**network threat intelligence workflow**.  
Analysis artifacts, correlated indicators, and visual summaries are refreshed automatically.





<!-- AUTO-GENERATED-SECTION:START -->

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** 2026-01-23 02:01 UTC

<table>
<tr>
<td width="50%">

#### 🔴 High-Risk Vulnerabilities
| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1000 | CVE-2024-6201 | HIGH       |          7.6 | 192.168.1.167   |
| VULN-1001 | CVE-2024-7804 | HIGH       |          5.9 | 192.168.1.229   |
| VULN-1002 | CVE-2024-8205 | MEDIUM     |          2.6 | 192.168.1.120   |
| VULN-1003 | CVE-2024-3628 | HIGH       |          1.1 | 192.168.1.189   |
| VULN-1004 | CVE-2024-1284 | CRITICAL   |          8.7 | 192.168.1.87    |
| VULN-1005 | CVE-2024-5426 | LOW        |          3   | 192.168.1.36    |
| VULN-1006 | CVE-2024-9932 | MEDIUM     |          2.8 | 192.168.1.103   |
| VULN-1007 | CVE-2024-1362 | LOW        |          6.2 | 192.168.1.187   |
| VULN-1008 | CVE-2024-2777 | LOW        |          8.8 | 192.168.1.13    |
| VULN-1009 | CVE-2024-5323 | CRITICAL   |          6   | 192.168.1.158   |

</td>
<td width="50%">

#### 🧪 Top OSINT IOCs
| ioc_type   | ioc_value                        |   confidence | source    |
|:-----------|:---------------------------------|-------------:|:----------|
| IP         | 185.70.61.236                    |           73 | OSINT-SIM |
| IP         | 185.3.224.145                    |           73 | OSINT-SIM |
| DOMAIN     | malicious177.com                 |           92 | OSINT-SIM |
| IP         | 185.119.107.144                  |           66 | OSINT-SIM |
| IP         | 185.112.31.202                   |           86 | OSINT-SIM |
| HASH       | 2e03b46f272c23db278e44484a6f3384 |           76 | OSINT-SIM |
| HASH       | 97e3525141ea737ddeb479cc2e1243d1 |           66 | OSINT-SIM |
| DOMAIN     | malicious568.com                 |           81 | OSINT-SIM |
| DOMAIN     | malicious290.com                 |           74 | OSINT-SIM |
| HASH       | 84a9f881cd866bd22fa85235ea1d6d55 |           93 | OSINT-SIM |

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

