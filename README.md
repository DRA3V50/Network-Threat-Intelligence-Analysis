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
**Generated (UTC):** 2026-01-26 03:21

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| DOMAIN     | malicious394.com                 |           95 | Open-Source Intelligence |
| HASH       | d6bc3362199868a578276477d9977bb0 |           93 | Open-Source Intelligence |
| DOMAIN     | malicious928.com                 |           93 | Open-Source Intelligence |
| HASH       | 7730ff8499fb6f9801ebf87dbf0c40c9 |           92 | Open-Source Intelligence |
| HASH       | 6564e3a908280a359cac5b454d110576 |           90 | Open-Source Intelligence |
| IP         | 185.195.42.28                    |           90 | Open-Source Intelligence |
| HASH       | 1ccd2cd47ae8bfedbd66eaa6278b9b42 |           90 | Open-Source Intelligence |
| IP         | 185.224.140.229                  |           85 | Open-Source Intelligence |
| HASH       | d6e16d4666429a54216b3f1057b706a0 |           84 | Open-Source Intelligence |
| URL        | http://bad888.example/path       |           84 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1008 | CVE-2024-5576 | MEDIUM     |          9.9 | 192.168.1.147   |
| VULN-1016 | CVE-2024-1403 | LOW        |          9.4 | 192.168.1.55    |
| VULN-1013 | CVE-2024-8337 | HIGH       |          9.3 | 192.168.1.225   |
| VULN-1044 | CVE-2024-3327 | MEDIUM     |          9.2 | 192.168.1.146   |
| VULN-1046 | CVE-2024-4340 | CRITICAL   |          9.2 | 192.168.1.21    |
| VULN-1002 | CVE-2024-8942 | HIGH       |          8.9 | 192.168.1.91    |
| VULN-1014 | CVE-2024-4962 | HIGH       |          8.7 | 192.168.1.242   |
| VULN-1041 | CVE-2024-9863 | MEDIUM     |          8.7 | 192.168.1.230   |
| VULN-1000 | CVE-2024-3910 | CRITICAL   |          8.5 | 192.168.1.187   |
| VULN-1038 | CVE-2024-7846 | HIGH       |          8.4 | 192.168.1.83    |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.png)

<!-- AUTO-GENERATED-END -->



---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
