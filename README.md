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

![Top Source IPs](outputs/charts/top_source_ips.png)

This chart highlights the most active source IPs observed in the analyzed traffic.  
Elevated activity may indicate:
- Reconnaissance or scanning behavior
- Misconfigured systems
- Potential malicious activity

---













<!-- AUTO-GENERATED-START -->

## 📌 Daily Threat Intelligence Snapshot
**Generated (UTC):** 2026-01-29 22:52

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| IP         | 185.110.170.234                  |           95 | Open-Source Intelligence |
| URL        | http://bad320.example/path       |           95 | Open-Source Intelligence |
| IP         | 185.52.215.58                    |           94 | Open-Source Intelligence |
| HASH       | a5e8df7401e0cb22f683dff1bc05e595 |           94 | Open-Source Intelligence |
| URL        | http://bad177.example/path       |           94 | Open-Source Intelligence |
| DOMAIN     | malicious334.com                 |           94 | Open-Source Intelligence |
| DOMAIN     | malicious777.com                 |           93 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1002 | CVE-2024-3350 | CRITICAL   |         10   | 192.168.1.174   |
| VULN-1011 | CVE-2024-9796 | MEDIUM     |          9.7 | 192.168.1.115   |
| VULN-1008 | CVE-2024-2529 | HIGH       |          9.6 | 192.168.1.129   |
| VULN-1025 | CVE-2024-4532 | CRITICAL   |          9.4 | 192.168.1.111   |
| VULN-1021 | CVE-2024-2373 | MEDIUM     |          9   | 192.168.1.50    |
| VULN-1000 | CVE-2024-7168 | CRITICAL   |          8.6 | 192.168.1.162   |
| VULN-1035 | CVE-2024-7805 | CRITICAL   |          8.6 | 192.168.1.72    |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.csv)

<!-- AUTO-GENERATED-END -->













---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
