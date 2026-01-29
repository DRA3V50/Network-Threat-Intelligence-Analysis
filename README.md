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
**Generated (UTC):** 2026-01-29 03:58

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| DOMAIN     | malicious532.com                 |           95 | Open-Source Intelligence |
| URL        | http://bad533.example/path       |           95 | Open-Source Intelligence |
| HASH       | c653c2c3637fc17ed7f602b17678c56e |           94 | Open-Source Intelligence |
| HASH       | 1bffff5cce1eb716f3469fec298e91f7 |           94 | Open-Source Intelligence |
| URL        | http://bad329.example/path       |           93 | Open-Source Intelligence |
| URL        | http://bad732.example/path       |           92 | Open-Source Intelligence |
| HASH       | b67bc19d32255111d869a6f2b2a457b4 |           90 | Open-Source Intelligence |
| HASH       | 0c65e30cc4e135ad57a28e636458b2af |           90 | Open-Source Intelligence |
| IP         | 185.69.23.194                    |           89 | Open-Source Intelligence |
| IP         | 185.188.222.89                   |           89 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1011 | CVE-2024-1335 | HIGH       |          9.7 | 192.168.1.34    |
| VULN-1024 | CVE-2024-3600 | CRITICAL   |          9.7 | 192.168.1.57    |
| VULN-1032 | CVE-2024-3750 | LOW        |          9.4 | 192.168.1.1     |
| VULN-1006 | CVE-2024-3008 | LOW        |          9.3 | 192.168.1.29    |
| VULN-1013 | CVE-2024-2401 | CRITICAL   |          8.9 | 192.168.1.78    |
| VULN-1014 | CVE-2024-7233 | MEDIUM     |          8.9 | 192.168.1.25    |
| VULN-1031 | CVE-2024-1664 | HIGH       |          8.6 | 192.168.1.213   |
| VULN-1016 | CVE-2024-9288 | MEDIUM     |          8.5 | 192.168.1.231   |
| VULN-1022 | CVE-2024-7707 | LOW        |          8.4 | 192.168.1.212   |
| VULN-1036 | CVE-2024-6364 | CRITICAL   |          8.4 | 192.168.1.136   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.csv)

<!-- AUTO-GENERATED-END -->











---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
