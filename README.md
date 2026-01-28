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
**Generated (UTC):** 2026-01-28 14:31

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| HASH       | 9abf01e8c0e5b7a20ee3d415c6ea61bb |           95 | Open-Source Intelligence |
| HASH       | fbf73eb275fcdf843422530aa31d3b47 |           94 | Open-Source Intelligence |
| IP         | 185.105.208.104                  |           92 | Open-Source Intelligence |
| URL        | http://bad592.example/path       |           91 | Open-Source Intelligence |
| DOMAIN     | malicious278.com                 |           89 | Open-Source Intelligence |
| HASH       | 5abfb7d92a1b4045035c57d26ade0374 |           86 | Open-Source Intelligence |
| HASH       | b87e6e0e133ad90b87f43c75c9037cb4 |           85 | Open-Source Intelligence |
| URL        | http://bad848.example/path       |           84 | Open-Source Intelligence |
| HASH       | 96cca75dd1e9bd93577eb17db5347847 |           84 | Open-Source Intelligence |
| URL        | http://bad727.example/path       |           83 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1021 | CVE-2024-4852 | HIGH       |         10   | 192.168.1.137   |
| VULN-1037 | CVE-2024-8347 | LOW        |          9.5 | 192.168.1.203   |
| VULN-1016 | CVE-2024-9129 | CRITICAL   |          9.4 | 192.168.1.211   |
| VULN-1038 | CVE-2024-9516 | CRITICAL   |          9.4 | 192.168.1.100   |
| VULN-1033 | CVE-2024-9642 | MEDIUM     |          8.9 | 192.168.1.67    |
| VULN-1001 | CVE-2024-4559 | CRITICAL   |          8.8 | 192.168.1.122   |
| VULN-1004 | CVE-2024-3193 | HIGH       |          8.8 | 192.168.1.196   |
| VULN-1011 | CVE-2024-4770 | CRITICAL   |          8.7 | 192.168.1.12    |
| VULN-1022 | CVE-2024-4704 | LOW        |          8.6 | 192.168.1.240   |
| VULN-1000 | CVE-2024-5551 | HIGH       |          8.3 | 192.168.1.77    |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.csv)

<!-- AUTO-GENERATED-END -->










---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
