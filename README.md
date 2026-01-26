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

## ⚠️ Automated Threat Intelligence Snapshot
**Generated (UTC):** 2026-01-26 02:49

### 🚨 High-Confidence Threat Indicators
Curated and ranked Indicators of Compromise derived from open-source intelligence.

| ioc_type | ioc_value | confidence | source |
|---------|-----------|-----------:|--------|
| HASH | 43a4b0c7891d26df4dafe94b0222b99b | 95 | Open-Source Intelligence |
| HASH | 3148a6416abf446b11843e591902e559 | 95 | Open-Source Intelligence |
| DOMAIN | malicious670.com | 94 | Open-Source Intelligence |
| HASH | 567e82fa825ce93b79ce614929ddd543 | 92 | Open-Source Intelligence |
| DOMAIN | malicious737.com | 92 | Open-Source Intelligence |
| IP | 185.195.175.137 | 91 | Open-Source Intelligence |
| IP | 185.16.181.184 | 90 | Open-Source Intelligence |
| IP | 185.248.126.108 | 90 | Open-Source Intelligence |
| URL | http://bad559.example/path | 87 | Open-Source Intelligence |
| DOMAIN | malicious447.com | 87 | Open-Source Intelligence |

---

### 🔥 Highest-Risk Vulnerabilities
Vulnerabilities prioritized by exploitability and operational impact.

| vuln_id | cve | severity | risk_score | affected_host |
|--------|-----|----------|-----------:|---------------|
| VULN-1021 | CVE-2024-2464 | LOW | 9.1 | 192.168.1.160 |
| VULN-1038 | CVE-2024-7573 | CRITICAL | 8.8 | 192.168.1.24 |
| VULN-1045 | CVE-2024-8190 | CRITICAL | 8.7 | 192.168.1.136 |
| VULN-1049 | CVE-2024-8443 | MEDIUM | 8.6 | 192.168.1.204 |
| VULN-1004 | CVE-2024-2640 | HIGH | 8.6 | 192.168.1.2 |
| VULN-1010 | CVE-2024-3485 | MEDIUM | 8.4 | 192.168.1.233 |
| VULN-1036 | CVE-2024-3206 | HIGH | 7.8 | 192.168.1.42 |
| VULN-1020 | CVE-2024-4733 | MEDIUM | 7.7 | 192.168.1.4 |
| VULN-1023 | CVE-2024-4941 | LOW | 7.7 | 192.168.1.66 |
| VULN-1041 | CVE-2024-4742 | HIGH | 7.5 | 192.168.1.182 |

---

### 📈 Network Activity Summary
![Top Source IPs](build/charts/top_source_ips.png)

<!-- AUTO-GENERATED-END -->

---

## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored
