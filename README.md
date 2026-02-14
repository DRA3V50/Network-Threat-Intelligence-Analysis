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
**Generated (UTC):** 2026-01-31 02:41

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| DOMAIN     | malicious313.com                 |           93 | Open-Source Intelligence |
| HASH       | 85696c3f56094c029ce4eaf944c50b92 |           65 | Open-Source Intelligence |
| DOMAIN     | malicious148.com                 |           66 | Open-Source Intelligence |
| URL        | http://bad295.example/path       |           62 | Open-Source Intelligence |
| URL        | http://bad916.example/path       |           62 | Open-Source Intelligence |
| IP         | 185.189.11.153                   |           92 | Open-Source Intelligence |
| URL        | http://bad220.example/path       |           76 | Open-Source Intelligence |
| URL        | http://bad740.example/path       |           86 | Open-Source Intelligence |
| IP         | 185.81.164.252                   |           67 | Open-Source Intelligence |
| DOMAIN     | malicious140.com                 |           61 | Open-Source Intelligence |
| DOMAIN     | malicious823.com                 |           87 | Open-Source Intelligence |
| HASH       | 2c1dbdde172c6fd5184da0a16e22cacc |           94 | Open-Source Intelligence |
| DOMAIN     | malicious714.com                 |           80 | Open-Source Intelligence |
| DOMAIN     | malicious686.com                 |           92 | Open-Source Intelligence |
| URL        | http://bad844.example/path       |           65 | Open-Source Intelligence |
| HASH       | 77b64136b9317353e1b11d5f51db7726 |           88 | Open-Source Intelligence |
| URL        | http://bad993.example/path       |           67 | Open-Source Intelligence |
| URL        | http://bad172.example/path       |           84 | Open-Source Intelligence |
| URL        | http://bad830.example/path       |           93 | Open-Source Intelligence |
| IP         | 185.120.176.160                  |           70 | Open-Source Intelligence |
| DOMAIN     | malicious404.com                 |           60 | Open-Source Intelligence |
| URL        | http://bad358.example/path       |           79 | Open-Source Intelligence |
| HASH       | faeef99c12f69a98215584b1c3dabd03 |           70 | Open-Source Intelligence |
| URL        | http://bad221.example/path       |           88 | Open-Source Intelligence |
| IP         | 185.146.156.4                    |           77 | Open-Source Intelligence |
| HASH       | f19853244fd1d61cbe9eb5723b6e7e18 |           88 | Open-Source Intelligence |
| URL        | http://bad323.example/path       |           82 | Open-Source Intelligence |
| DOMAIN     | malicious814.com                 |           89 | Open-Source Intelligence |
| IP         | 185.41.132.190                   |           60 | Open-Source Intelligence |
| HASH       | 9dc873fd6b16d584a76b878fe8f74c74 |           63 | Open-Source Intelligence |
| IP         | 185.20.116.110                   |           71 | Open-Source Intelligence |
| DOMAIN     | malicious215.com                 |           94 | Open-Source Intelligence |
| HASH       | 8a6141764e178f97945e0ba406044fe6 |           77 | Open-Source Intelligence |
| URL        | http://bad222.example/path       |           72 | Open-Source Intelligence |
| DOMAIN     | malicious235.com                 |           61 | Open-Source Intelligence |
| URL        | http://bad914.example/path       |           73 | Open-Source Intelligence |
| HASH       | 8b6d9442a5767e8fe9feb7824e82b220 |           84 | Open-Source Intelligence |
| HASH       | 282019a6d043c80a6c492b0cc635f8ed |           65 | Open-Source Intelligence |
| IP         | 185.48.127.215                   |           94 | Open-Source Intelligence |
| URL        | http://bad809.example/path       |           67 | Open-Source Intelligence |
| DOMAIN     | malicious703.com                 |           87 | Open-Source Intelligence |
| DOMAIN     | malicious617.com                 |           67 | Open-Source Intelligence |
| URL        | http://bad196.example/path       |           64 | Open-Source Intelligence |
| URL        | http://bad723.example/path       |           84 | Open-Source Intelligence |
| IP         | 185.165.94.173                   |           60 | Open-Source Intelligence |
| DOMAIN     | malicious268.com                 |           79 | Open-Source Intelligence |
| IP         | 185.244.157.199                  |           89 | Open-Source Intelligence |
| IP         | 185.19.189.113                   |           91 | Open-Source Intelligence |
| IP         | 185.18.185.230                   |           88 | Open-Source Intelligence |
| HASH       | e02cbd22153bd3578a8b41aaf7fb7e63 |           80 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1000 | CVE-2024-1990 | LOW        |          5.6 | 192.168.1.234   |
| VULN-1001 | CVE-2024-8089 | LOW        |          9.2 | 192.168.1.112   |
| VULN-1002 | CVE-2024-4909 | MEDIUM     |          1.4 | 192.168.1.162   |
| VULN-1003 | CVE-2024-4307 | MEDIUM     |          3.2 | 192.168.1.49    |
| VULN-1004 | CVE-2024-1313 | MEDIUM     |          4.8 | 192.168.1.52    |
| VULN-1005 | CVE-2024-7512 | LOW        |          6.9 | 192.168.1.132   |
| VULN-1006 | CVE-2024-8736 | LOW        |          1.6 | 192.168.1.246   |
| VULN-1007 | CVE-2024-1245 | HIGH       |          9.8 | 192.168.1.47    |
| VULN-1008 | CVE-2024-9081 | HIGH       |          6.5 | 192.168.1.117   |
| VULN-1009 | CVE-2024-2708 | HIGH       |          7.4 | 192.168.1.215   |
| VULN-1010 | CVE-2024-5512 | CRITICAL   |          1.5 | 192.168.1.226   |
| VULN-1011 | CVE-2024-8703 | CRITICAL   |          2.6 | 192.168.1.99    |
| VULN-1012 | CVE-2024-7053 | MEDIUM     |          1.8 | 192.168.1.163   |
| VULN-1013 | CVE-2024-6186 | MEDIUM     |          8.3 | 192.168.1.71    |
| VULN-1014 | CVE-2024-3809 | MEDIUM     |          6.2 | 192.168.1.69    |
| VULN-1015 | CVE-2024-2631 | HIGH       |          8.1 | 192.168.1.10    |
| VULN-1016 | CVE-2024-6121 | MEDIUM     |          4.3 | 192.168.1.121   |
| VULN-1017 | CVE-2024-9825 | HIGH       |          2.7 | 192.168.1.77    |
| VULN-1018 | CVE-2024-1515 | HIGH       |          5.8 | 192.168.1.199   |
| VULN-1019 | CVE-2024-8345 | CRITICAL   |          2.3 | 192.168.1.82    |
| VULN-1020 | CVE-2024-4605 | MEDIUM     |          1.3 | 192.168.1.185   |
| VULN-1021 | CVE-2024-6600 | HIGH       |          7.4 | 192.168.1.218   |
| VULN-1022 | CVE-2024-9422 | CRITICAL   |          3.8 | 192.168.1.56    |
| VULN-1023 | CVE-2024-2482 | HIGH       |          3.9 | 192.168.1.191   |
| VULN-1024 | CVE-2024-4295 | LOW        |          6.4 | 192.168.1.47    |
| VULN-1025 | CVE-2024-6084 | MEDIUM     |          8.9 | 192.168.1.239   |
| VULN-1026 | CVE-2024-5872 | LOW        |          3.4 | 192.168.1.120   |
| VULN-1027 | CVE-2024-7321 | HIGH       |          5.5 | 192.168.1.89    |
| VULN-1028 | CVE-2024-3272 | MEDIUM     |          8.5 | 192.168.1.38    |
| VULN-1029 | CVE-2024-6656 | LOW        |          2.4 | 192.168.1.105   |
| VULN-1030 | CVE-2024-1494 | CRITICAL   |          5.3 | 192.168.1.79    |
| VULN-1031 | CVE-2024-3906 | CRITICAL   |          9.1 | 192.168.1.216   |
| VULN-1032 | CVE-2024-2656 | LOW        |          8.7 | 192.168.1.86    |
| VULN-1033 | CVE-2024-6464 | HIGH       |          7.1 | 192.168.1.191   |
| VULN-1034 | CVE-2024-2800 | LOW        |          9.6 | 192.168.1.11    |
| VULN-1035 | CVE-2024-8277 | MEDIUM     |          4.3 | 192.168.1.218   |
| VULN-1036 | CVE-2024-4753 | CRITICAL   |          4.6 | 192.168.1.120   |
| VULN-1037 | CVE-2024-6845 | LOW        |          2.4 | 192.168.1.181   |
| VULN-1038 | CVE-2024-6956 | MEDIUM     |          5.7 | 192.168.1.83    |
| VULN-1039 | CVE-2024-8927 | CRITICAL   |          9   | 192.168.1.138   |
| VULN-1040 | CVE-2024-9655 | CRITICAL   |          9.6 | 192.168.1.170   |
| VULN-1041 | CVE-2024-4610 | MEDIUM     |          3.9 | 192.168.1.145   |
| VULN-1042 | CVE-2024-9644 | HIGH       |          9.9 | 192.168.1.3     |
| VULN-1043 | CVE-2024-3876 | LOW        |          8.9 | 192.168.1.155   |
| VULN-1044 | CVE-2024-1852 | CRITICAL   |          6.3 | 192.168.1.18    |
| VULN-1045 | CVE-2024-2182 | HIGH       |          4.7 | 192.168.1.41    |
| VULN-1046 | CVE-2024-2202 | HIGH       |          8.4 | 192.168.1.174   |
| VULN-1047 | CVE-2024-5938 | HIGH       |          2.1 | 192.168.1.229   |
| VULN-1048 | CVE-2024-5851 | MEDIUM     |          3.5 | 192.168.1.47    |
| VULN-1049 | CVE-2024-5617 | CRITICAL   |          2.3 | 192.168.1.79    |


## ⚠️ Important Notes

- All data is **simulated for research, demonstration purposes, education, and portfolio projects**
- No live production environments are monitored


<!-- AUTO-GENERATED-START -->

## 📌 Daily Threat Intelligence Snapshot
**Generated (UTC):** 2026-02-14 02:35

### 🛰️ High-Confidence Threat Indicators
| ioc_value                | ioc_type   |   confidence |
|:-------------------------|:-----------|-------------:|
| malicious.com            | hash       |           94 |
| badactor.net             | domain     |           90 |
| 2ddbdd712c056f34bd0aa2cc | ip         |           89 |
| 193.42.157.198           | ip         |           85 |
| malwaredrop.org          | ip         |           82 |
| 185.82.113.99            | ip         |           77 |
| 185.81.68.90             | ip         |           74 |
| 185.83.60.186            | domain     |           72 |

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
