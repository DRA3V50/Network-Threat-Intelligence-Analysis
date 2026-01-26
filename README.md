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
**Generated (UTC):** 2026-01-26 13:41

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| URL        | http://bad601.example/path       |           94 | Open-Source Intelligence |
| HASH       | 4491165a2b0e815e3b7f387abe27014d |           94 | Open-Source Intelligence |
| URL        | http://bad511.example/path       |           94 | Open-Source Intelligence |
| URL        | http://bad770.example/path       |           94 | Open-Source Intelligence |
| DOMAIN     | malicious256.com                 |           94 | Open-Source Intelligence |
| IP         | 185.211.250.123                  |           93 | Open-Source Intelligence |
| IP         | 185.83.186.1                     |           93 | Open-Source Intelligence |
| HASH       | c7f12ddb0256c89135164fe4cd501aae |           92 | Open-Source Intelligence |
| URL        | http://bad533.example/path       |           92 | Open-Source Intelligence |
| DOMAIN     | malicious580.com                 |           91 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1017 | CVE-2024-5949 | CRITICAL   |          9.8 | 192.168.1.251   |
| VULN-1034 | CVE-2024-9153 | LOW        |          9.7 | 192.168.1.168   |
| VULN-1037 | CVE-2024-7760 | HIGH       |          9.6 | 192.168.1.240   |
| VULN-1035 | CVE-2024-9265 | HIGH       |          9.4 | 192.168.1.82    |
| VULN-1038 | CVE-2024-9276 | HIGH       |          9.2 | 192.168.1.27    |
| VULN-1029 | CVE-2024-7563 | MEDIUM     |          9.1 | 192.168.1.239   |
| VULN-1023 | CVE-2024-7911 | LOW        |          9   | 192.168.1.156   |
| VULN-1031 | CVE-2024-7278 | LOW        |          9   | 192.168.1.193   |
| VULN-1013 | CVE-2024-8280 | HIGH       |          9   | 192.168.1.40    |
| VULN-1032 | CVE-2024-7652 | LOW        |          8.7 | 192.168.1.145   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.csv)

<!-- AUTO-GENERATED-END -->






---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
