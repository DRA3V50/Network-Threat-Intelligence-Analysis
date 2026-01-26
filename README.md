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
**Generated (UTC):** 2026-01-26 03:35

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| IP         | 185.236.230.32                   |           94 | Open-Source Intelligence |
| HASH       | 8ae86535a0207546451ec8fa1c3f4806 |           93 | Open-Source Intelligence |
| DOMAIN     | malicious687.com                 |           92 | Open-Source Intelligence |
| DOMAIN     | malicious586.com                 |           92 | Open-Source Intelligence |
| IP         | 185.14.77.87                     |           90 | Open-Source Intelligence |
| DOMAIN     | malicious266.com                 |           90 | Open-Source Intelligence |
| URL        | http://bad935.example/path       |           87 | Open-Source Intelligence |
| DOMAIN     | malicious310.com                 |           85 | Open-Source Intelligence |
| URL        | http://bad973.example/path       |           84 | Open-Source Intelligence |
| IP         | 185.105.226.40                   |           84 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1020 | CVE-2024-8143 | HIGH       |          9.8 | 192.168.1.58    |
| VULN-1022 | CVE-2024-9981 | CRITICAL   |          9.6 | 192.168.1.59    |
| VULN-1012 | CVE-2024-6201 | LOW        |          9.5 | 192.168.1.39    |
| VULN-1042 | CVE-2024-2042 | MEDIUM     |          9.2 | 192.168.1.63    |
| VULN-1001 | CVE-2024-7650 | CRITICAL   |          9.1 | 192.168.1.111   |
| VULN-1043 | CVE-2024-5107 | HIGH       |          9   | 192.168.1.211   |
| VULN-1047 | CVE-2024-7203 | HIGH       |          8.5 | 192.168.1.211   |
| VULN-1044 | CVE-2024-3569 | LOW        |          8.5 | 192.168.1.15    |
| VULN-1040 | CVE-2024-4701 | CRITICAL   |          8.2 | 192.168.1.29    |
| VULN-1025 | CVE-2024-7557 | LOW        |          8.1 | 192.168.1.216   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.csv)

<!-- AUTO-GENERATED-END -->





---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
