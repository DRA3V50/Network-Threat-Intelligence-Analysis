# Network Threat Intelligence Analysis

⚠️ **Automated Network Threat Intelligence, OSINT Correlation, and Risk Prioritization**

This repository implements an **automated defensive threat-intelligence pipeline** designed to simulate how a SOC ingests, enriches, correlates, and prioritizes security data from multiple sources.

It focuses on **actionable intelligence**, not raw data.

---

## 🎯 Project Purpose & Scope

The primary objective of this project is to:

- Correlate **network activity**, **OSINT threat indicators**, and **vulnerability data**
- Identify **high-risk assets and behaviors**
- Produce **repeatable, automated intelligence reports**
- Demonstrate real-world **SOC and Blue Team workflows**

This is **not** a scanner or IDS replacement.  
It is an **intelligence aggregation and prioritization layer**.

---

## 🔄 Automation & Update Frequency

⏱️ **Update Frequency:**  
- Runs automatically via **GitHub Actions**
- Executes **multiple times per day** (scheduled and trigger-based)

Each execution:
- Regenerates intelligence datasets
- Recalculates risk prioritization
- Updates charts and summaries
- Rewrites the README snapshot section automatically

All timestamps are recorded in **UTC**.

---

## 📡 Intelligence Sources & Analysis Layers

### 🛰️ Open-Source Threat Intelligence (OSINT)
- Simulated high-confidence Indicators of Compromise (IOCs)
- Includes IPs, domains, URLs, and file hashes
- Ranked by **confidence score**
- Models curated threat feeds (CERTs, ISACs, vendor intelligence)

### 🔥 Vulnerability Risk Analysis
- Simulated vulnerability scan results
- CVEs prioritized using a calculated **risk score**
- Reflects exploitability and operational impact
- Mirrors remediation-driven SOC workflows

### 🌐 Network Traffic Analysis
- PCAP-derived network activity analysis
- Identifies **top source IPs by connection volume**
- Highlights anomalous or suspicious traffic patterns
- Visualized for rapid analyst triage

---

## 📊 Network Activity Visualization

🚨 **Top Source IPs by Connection Volume**

![Top Source IPs Chart](outputs/charts/top_source_ips.png)

This chart highlights the most active source IPs observed in the analyzed traffic.  
Elevated activity may indicate:
- Reconnaissance or scanning behavior
- Misconfigured systems
- Potential malicious activity

---




<!-- AUTO-GENERATED-START -->

## 📌 Daily Threat Intelligence Snapshot
**Generated (UTC):** 2026-01-26 03:33

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| IP         | 185.88.38.119                    |           95 | Open-Source Intelligence |
| IP         | 185.230.226.156                  |           95 | Open-Source Intelligence |
| URL        | http://bad277.example/path       |           94 | Open-Source Intelligence |
| IP         | 185.231.24.55                    |           94 | Open-Source Intelligence |
| IP         | 185.225.231.160                  |           92 | Open-Source Intelligence |
| IP         | 185.142.123.143                  |           91 | Open-Source Intelligence |
| IP         | 185.95.35.234                    |           90 | Open-Source Intelligence |
| HASH       | de165d8001be50f27053c53f487d2cd8 |           88 | Open-Source Intelligence |
| DOMAIN     | malicious193.com                 |           85 | Open-Source Intelligence |
| IP         | 185.61.1.74                      |           85 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1030 | CVE-2024-6197 | MEDIUM     |          9.7 | 192.168.1.198   |
| VULN-1039 | CVE-2024-1511 | CRITICAL   |          9.3 | 192.168.1.100   |
| VULN-1015 | CVE-2024-1468 | HIGH       |          9   | 192.168.1.117   |
| VULN-1040 | CVE-2024-7283 | CRITICAL   |          8.8 | 192.168.1.159   |
| VULN-1007 | CVE-2024-3255 | MEDIUM     |          8.8 | 192.168.1.226   |
| VULN-1004 | CVE-2024-9671 | MEDIUM     |          8.8 | 192.168.1.168   |
| VULN-1009 | CVE-2024-9708 | MEDIUM     |          8.6 | 192.168.1.167   |
| VULN-1027 | CVE-2024-2523 | HIGH       |          8.1 | 192.168.1.138   |
| VULN-1005 | CVE-2024-7787 | HIGH       |          8.1 | 192.168.1.91    |
| VULN-1033 | CVE-2024-4307 | LOW        |          8   | 192.168.1.169   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.png)

<!-- AUTO-GENERATED-END -->




---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
