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
**Generated (UTC):** 2026-01-27 14:30

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| URL        | http://bad953.example/path       |           95 | Open-Source Intelligence |
| DOMAIN     | malicious683.com                 |           94 | Open-Source Intelligence |
| IP         | 185.219.232.228                  |           93 | Open-Source Intelligence |
| HASH       | a8cedc3c5485cde69ddbad6736b5a554 |           93 | Open-Source Intelligence |
| HASH       | a3991d20da4cb9a6cc600918a41b9b06 |           92 | Open-Source Intelligence |
| HASH       | 8eccdf2c62d610c4ae92bf8b9e3ada6a |           91 | Open-Source Intelligence |
| DOMAIN     | malicious315.com                 |           90 | Open-Source Intelligence |
| DOMAIN     | malicious719.com                 |           88 | Open-Source Intelligence |
| IP         | 185.206.252.98                   |           87 | Open-Source Intelligence |
| URL        | http://bad372.example/path       |           87 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1035 | CVE-2024-8730 | LOW        |          9.9 | 192.168.1.30    |
| VULN-1014 | CVE-2024-4254 | MEDIUM     |          9.6 | 192.168.1.251   |
| VULN-1033 | CVE-2024-2540 | LOW        |          9.6 | 192.168.1.43    |
| VULN-1029 | CVE-2024-7500 | CRITICAL   |          9.1 | 192.168.1.99    |
| VULN-1037 | CVE-2024-2421 | MEDIUM     |          8.6 | 192.168.1.95    |
| VULN-1047 | CVE-2024-2478 | MEDIUM     |          8.6 | 192.168.1.249   |
| VULN-1031 | CVE-2024-9392 | CRITICAL   |          8.5 | 192.168.1.143   |
| VULN-1039 | CVE-2024-1720 | CRITICAL   |          8.1 | 192.168.1.207   |
| VULN-1045 | CVE-2024-2785 | MEDIUM     |          8   | 192.168.1.28    |
| VULN-1038 | CVE-2024-4707 | MEDIUM     |          8   | 192.168.1.250   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.csv)

<!-- AUTO-GENERATED-END -->








---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
