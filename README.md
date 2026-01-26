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
**Generated (UTC):** 2026-01-26 03:17

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| URL        | http://bad588.example/path       |           95 | Open-Source Intelligence |
| HASH       | 131c8e83eb56294657c41a9d508b41a1 |           93 | Open-Source Intelligence |
| HASH       | 1d022f190ad0e70e1cd4671783d89493 |           91 | Open-Source Intelligence |
| DOMAIN     | malicious643.com                 |           90 | Open-Source Intelligence |
| HASH       | 324adf4849849b1cc10aef5dd94939c5 |           84 | Open-Source Intelligence |
| IP         | 185.138.225.30                   |           84 | Open-Source Intelligence |
| DOMAIN     | malicious638.com                 |           84 | Open-Source Intelligence |
| DOMAIN     | malicious959.com                 |           82 | Open-Source Intelligence |
| HASH       | a4569f68a2885780db4d7dd3c8e605f3 |           81 | Open-Source Intelligence |
| DOMAIN     | malicious229.com                 |           80 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1005 | CVE-2024-2777 | HIGH       |          9.9 | 192.168.1.184   |
| VULN-1012 | CVE-2024-1491 | MEDIUM     |          9.5 | 192.168.1.201   |
| VULN-1041 | CVE-2024-2049 | HIGH       |          9.5 | 192.168.1.48    |
| VULN-1039 | CVE-2024-8769 | HIGH       |          9.4 | 192.168.1.187   |
| VULN-1007 | CVE-2024-6810 | HIGH       |          9.1 | 192.168.1.172   |
| VULN-1037 | CVE-2024-6908 | MEDIUM     |          8.7 | 192.168.1.182   |
| VULN-1046 | CVE-2024-6221 | HIGH       |          8.6 | 192.168.1.132   |
| VULN-1021 | CVE-2024-2059 | HIGH       |          8.5 | 192.168.1.188   |
| VULN-1032 | CVE-2024-8546 | HIGH       |          8.5 | 192.168.1.223   |
| VULN-1031 | CVE-2024-9368 | LOW        |          8.3 | 192.168.1.110   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.png)

<!-- AUTO-GENERATED-END -->


---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
