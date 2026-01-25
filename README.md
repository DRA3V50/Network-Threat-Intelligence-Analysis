
# Network Threat Intelligence Analysis

🛡️ Automated defensive network analysis with OSINT enrichment and threat correlation

---

## Daily Automated Threat Intelligence Update

**Timestamp (UTC):** 2026-01-24 03:36 UTC

### 📊 Network Activity Chart
Top Source IPs by connection count:

![Top Source IPs Chart](outputs/charts/top_source_ips.png)

*This chart visualizes the network activity, highlighting the most active source IPs.*




<!-- AUTO-GENERATED-START -->

## 📌 Daily Threat Intelligence Snapshot
**Generated (UTC):** 2026-01-25 03:12

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| IP         | 185.246.128.219                  |           95 | Open-Source Intelligence |
| URL        | http://bad716.example/path       |           94 | Open-Source Intelligence |
| URL        | http://bad343.example/path       |           93 | Open-Source Intelligence |
| HASH       | d241a358999d69f9853ff364c8727cdc |           93 | Open-Source Intelligence |
| URL        | http://bad138.example/path       |           88 | Open-Source Intelligence |
| DOMAIN     | malicious325.com                 |           87 | Open-Source Intelligence |
| HASH       | 4759ccad328421a277250a0c2929ab8e |           86 | Open-Source Intelligence |
| URL        | http://bad558.example/path       |           86 | Open-Source Intelligence |
| URL        | http://bad948.example/path       |           85 | Open-Source Intelligence |
| DOMAIN     | malicious581.com                 |           84 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1000 | CVE-2024-4585 | MEDIUM     |          6.8 | 192.168.1.82    |
| VULN-1001 | CVE-2024-4625 | LOW        |          4.6 | 192.168.1.74    |
| VULN-1002 | CVE-2024-6229 | LOW        |          2.7 | 192.168.1.202   |
| VULN-1003 | CVE-2024-8320 | MEDIUM     |          9.7 | 192.168.1.162   |
| VULN-1004 | CVE-2024-7994 | CRITICAL   |          2   | 192.168.1.200   |
| VULN-1005 | CVE-2024-5349 | LOW        |          8.8 | 192.168.1.201   |
| VULN-1006 | CVE-2024-5967 | MEDIUM     |          3.4 | 192.168.1.55    |
| VULN-1007 | CVE-2024-7538 | CRITICAL   |          9.8 | 192.168.1.223   |
| VULN-1008 | CVE-2024-8584 | LOW        |          5.8 | 192.168.1.45    |
| VULN-1009 | CVE-2024-6641 | HIGH       |          2.5 | 192.168.1.251   |
| VULN-1010 | CVE-2024-7781 | LOW        |          1.9 | 192.168.1.133   |
| VULN-1011 | CVE-2024-7672 | MEDIUM     |          2.9 | 192.168.1.23    |
| VULN-1012 | CVE-2024-2475 | HIGH       |          9.7 | 192.168.1.135   |
| VULN-1013 | CVE-2024-7066 | MEDIUM     |          7.5 | 192.168.1.175   |
| VULN-1014 | CVE-2024-3551 | HIGH       |          5.2 | 192.168.1.47    |
| VULN-1015 | CVE-2024-1991 | HIGH       |          3.2 | 192.168.1.141   |
| VULN-1016 | CVE-2024-8641 | LOW        |          8.6 | 192.168.1.68    |
| VULN-1017 | CVE-2024-4688 | LOW        |          1.5 | 192.168.1.52    |
| VULN-1018 | CVE-2024-3218 | HIGH       |          6.9 | 192.168.1.108   |
| VULN-1019 | CVE-2024-4439 | CRITICAL   |          9.3 | 192.168.1.61    |
| VULN-1020 | CVE-2024-6311 | HIGH       |          8.7 | 192.168.1.85    |
| VULN-1021 | CVE-2024-1361 | HIGH       |          7.4 | 192.168.1.196   |
| VULN-1022 | CVE-2024-2940 | LOW        |          9   | 192.168.1.217   |
| VULN-1023 | CVE-2024-9674 | HIGH       |          6.6 | 192.168.1.17    |
| VULN-1024 | CVE-2024-8654 | HIGH       |          9.8 | 192.168.1.6     |
| VULN-1025 | CVE-2024-4766 | MEDIUM     |          4.9 | 192.168.1.113   |
| VULN-1026 | CVE-2024-5251 | LOW        |          1.9 | 192.168.1.111   |
| VULN-1027 | CVE-2024-3558 | HIGH       |          3.3 | 192.168.1.212   |
| VULN-1028 | CVE-2024-5741 | CRITICAL   |          4.7 | 192.168.1.239   |
| VULN-1029 | CVE-2024-5122 | MEDIUM     |          8.3 | 192.168.1.185   |
| VULN-1030 | CVE-2024-7323 | CRITICAL   |          5.8 | 192.168.1.10    |
| VULN-1031 | CVE-2024-8029 | HIGH       |          8.9 | 192.168.1.218   |
| VULN-1032 | CVE-2024-9205 | CRITICAL   |          3.6 | 192.168.1.40    |
| VULN-1033 | CVE-2024-1876 | HIGH       |          9.3 | 192.168.1.247   |
| VULN-1034 | CVE-2024-5654 | CRITICAL   |          9   | 192.168.1.69    |
| VULN-1035 | CVE-2024-4844 | LOW        |          7.7 | 192.168.1.214   |
| VULN-1036 | CVE-2024-2011 | MEDIUM     |          8.5 | 192.168.1.164   |
| VULN-1037 | CVE-2024-1285 | CRITICAL   |          3.3 | 192.168.1.221   |
| VULN-1038 | CVE-2024-6669 | MEDIUM     |          9.3 | 192.168.1.233   |
| VULN-1039 | CVE-2024-2695 | HIGH       |          8.7 | 192.168.1.209   |
| VULN-1040 | CVE-2024-9865 | HIGH       |          2.8 | 192.168.1.115   |
| VULN-1041 | CVE-2024-1114 | MEDIUM     |          7.8 | 192.168.1.84    |
| VULN-1042 | CVE-2024-4824 | MEDIUM     |          6   | 192.168.1.205   |
| VULN-1043 | CVE-2024-8935 | LOW        |          4.9 | 192.168.1.144   |
| VULN-1044 | CVE-2024-9227 | CRITICAL   |          7.8 | 192.168.1.70    |
| VULN-1045 | CVE-2024-4097 | CRITICAL   |          5.5 | 192.168.1.244   |
| VULN-1046 | CVE-2024-4204 | LOW        |          8.2 | 192.168.1.126   |
| VULN-1047 | CVE-2024-2329 | CRITICAL   |          4.9 | 192.168.1.58    |
| VULN-1048 | CVE-2024-6517 | HIGH       |          2.4 | 192.168.1.191   |
| VULN-1049 | CVE-2024-1147 | LOW        |          5.6 | 192.168.1.138   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.png)

<!-- AUTO-GENERATED-END -->


