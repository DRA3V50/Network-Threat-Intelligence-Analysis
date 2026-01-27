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
**Generated (UTC):** 2026-01-27 03:07

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| URL        | http://bad549.example/path       |           94 | Open-Source Intelligence |
| DOMAIN     | malicious625.com                 |           92 | Open-Source Intelligence |
| IP         | 185.210.170.99                   |           91 | Open-Source Intelligence |
| IP         | 185.62.113.159                   |           90 | Open-Source Intelligence |
| HASH       | 140231605e374f894b4d1fc26126ba00 |           90 | Open-Source Intelligence |
| DOMAIN     | malicious790.com                 |           90 | Open-Source Intelligence |
| URL        | http://bad522.example/path       |           89 | Open-Source Intelligence |
| DOMAIN     | malicious234.com                 |           88 | Open-Source Intelligence |
| IP         | 185.254.39.35                    |           88 | Open-Source Intelligence |
| URL        | http://bad798.example/path       |           88 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1049 | CVE-2024-5708 | MEDIUM     |          9.7 | 192.168.1.204   |
| VULN-1025 | CVE-2024-9985 | LOW        |          9.7 | 192.168.1.124   |
| VULN-1027 | CVE-2024-6891 | MEDIUM     |          9.5 | 192.168.1.237   |
| VULN-1028 | CVE-2024-7008 | LOW        |          9.4 | 192.168.1.197   |
| VULN-1036 | CVE-2024-3254 | CRITICAL   |          9.4 | 192.168.1.185   |
| VULN-1032 | CVE-2024-5344 | CRITICAL   |          9.3 | 192.168.1.199   |
| VULN-1042 | CVE-2024-3851 | MEDIUM     |          8.5 | 192.168.1.44    |
| VULN-1004 | CVE-2024-3512 | HIGH       |          8.3 | 192.168.1.26    |
| VULN-1030 | CVE-2024-1329 | MEDIUM     |          8.2 | 192.168.1.29    |
| VULN-1019 | CVE-2024-1047 | LOW        |          8.2 | 192.168.1.237   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.csv)

<!-- AUTO-GENERATED-END -->







---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
