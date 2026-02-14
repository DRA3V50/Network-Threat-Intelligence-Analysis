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

![Network Threat Activity](build/charts/network_activity.png)

This chart highlights the most active source IPs observed in the analyzed traffic.  
Elevated activity may indicate:
- Reconnaissance or scanning behavior
- Misconfigured systems
- Potential malicious activity

---

























<!-- AUTO-GENERATED-START -->

## 📌 Daily Threat Intelligence Snapshot
**Generated (UTC):** 2026-02-14 19:23

### 🛰️ High-Confidence Threat Indicators
| ioc_value                | ioc_type   |   confidence |
|:-------------------------|:-----------|-------------:|
| 185.82.113.99            | ip         |           87 |
| malwaredrop.org          | ip         |           82 |
| 2ddbdd712c056f34bd0aa2cc | ip         |           79 |
| 193.42.157.198           | hash       |           79 |
| 185.83.60.186            | domain     |           76 |
| malicious.com            | hash       |           74 |
| badactor.net             | hash       |           72 |
| 185.81.68.90             | ip         |           70 |

### 🔥 Highest-Risk Vulnerabilities
| vulnerability   | severity   |   severity_score |   risk_score |
|:----------------|:-----------|-----------------:|-------------:|
| CVE-2024-3011   | Critical   |                9 |          100 |
| CVE-2023-2198   | High       |                7 |           75 |
| CVE-2022-4421   | Medium     |                5 |           50 |
| CVE-2020-1195   | Medium     |                5 |           50 |
| CVE-2021-3375   | Low        |                3 |           25 |

### 📊 Composite Network Threat Posture

![Network Threat Activity](build/charts/network_activity.png)

**Weighting Model**
- Threat Intelligence (IOCs): 90%
- Vulnerability Exposure: 5%
- Network Activity: 5%

<!-- AUTO-GENERATED-END -->








