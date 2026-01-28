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
**Generated (UTC):** 2026-01-28 03:26

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| URL        | http://bad667.example/path       |           92 | Open-Source Intelligence |
| URL        | http://bad957.example/path       |           92 | Open-Source Intelligence |
| DOMAIN     | malicious221.com                 |           90 | Open-Source Intelligence |
| HASH       | 45cb3ff98299acaeaa131a59e012c310 |           90 | Open-Source Intelligence |
| URL        | http://bad404.example/path       |           90 | Open-Source Intelligence |
| IP         | 185.66.59.203                    |           90 | Open-Source Intelligence |
| URL        | http://bad125.example/path       |           88 | Open-Source Intelligence |
| IP         | 185.69.180.57                    |           88 | Open-Source Intelligence |
| IP         | 185.142.173.238                  |           88 | Open-Source Intelligence |
| HASH       | 66f4393ab218a5c73e55cfcadd2723d4 |           86 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1021 | CVE-2024-2434 | CRITICAL   |          9.9 | 192.168.1.123   |
| VULN-1015 | CVE-2024-4065 | HIGH       |          9.7 | 192.168.1.108   |
| VULN-1017 | CVE-2024-3898 | CRITICAL   |          9.6 | 192.168.1.38    |
| VULN-1002 | CVE-2024-6006 | HIGH       |          9.6 | 192.168.1.95    |
| VULN-1001 | CVE-2024-4093 | HIGH       |          9.5 | 192.168.1.80    |
| VULN-1020 | CVE-2024-3286 | HIGH       |          9.4 | 192.168.1.26    |
| VULN-1003 | CVE-2024-7700 | CRITICAL   |          9.3 | 192.168.1.222   |
| VULN-1030 | CVE-2024-5202 | CRITICAL   |          9.2 | 192.168.1.166   |
| VULN-1025 | CVE-2024-7811 | LOW        |          9   | 192.168.1.69    |
| VULN-1037 | CVE-2024-8345 | CRITICAL   |          8.9 | 192.168.1.151   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.csv)

<!-- AUTO-GENERATED-END -->









---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
