
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
**Generated (UTC):** 2026-01-25 13:29

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| DOMAIN     | malicious949.com                 |           94 | Open-Source Intelligence |
| IP         | 185.129.187.70                   |           93 | Open-Source Intelligence |
| IP         | 185.223.3.97                     |           93 | Open-Source Intelligence |
| HASH       | da5f8300abd27ab1afd0062f65c7ed77 |           92 | Open-Source Intelligence |
| HASH       | ad245ce34ee7175d8cb0f989b9003a47 |           92 | Open-Source Intelligence |
| HASH       | 15ebb0dec1a6cc3b5bc348de769dab38 |           92 | Open-Source Intelligence |
| IP         | 185.167.69.188                   |           91 | Open-Source Intelligence |
| HASH       | 63656beb48075babcdc9bb3d4d843a25 |           90 | Open-Source Intelligence |
| URL        | http://bad827.example/path       |           87 | Open-Source Intelligence |
| URL        | http://bad952.example/path       |           83 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1000 | CVE-2024-7077 | HIGH       |          2.1 | 192.168.1.208   |
| VULN-1001 | CVE-2024-9148 | HIGH       |          2.9 | 192.168.1.53    |
| VULN-1002 | CVE-2024-6584 | CRITICAL   |          3   | 192.168.1.167   |
| VULN-1003 | CVE-2024-2094 | MEDIUM     |          5.4 | 192.168.1.187   |
| VULN-1004 | CVE-2024-8756 | CRITICAL   |          9.5 | 192.168.1.13    |
| VULN-1005 | CVE-2024-8845 | MEDIUM     |          2.6 | 192.168.1.34    |
| VULN-1006 | CVE-2024-1222 | CRITICAL   |          3.7 | 192.168.1.215   |
| VULN-1007 | CVE-2024-6776 | HIGH       |          2.3 | 192.168.1.63    |
| VULN-1008 | CVE-2024-3040 | CRITICAL   |          2.6 | 192.168.1.181   |
| VULN-1009 | CVE-2024-4570 | MEDIUM     |          6   | 192.168.1.84    |
| VULN-1010 | CVE-2024-8972 | MEDIUM     |          7.7 | 192.168.1.66    |
| VULN-1011 | CVE-2024-8887 | LOW        |          8.5 | 192.168.1.202   |
| VULN-1012 | CVE-2024-2232 | HIGH       |          5.9 | 192.168.1.1     |
| VULN-1013 | CVE-2024-4948 | CRITICAL   |          7.6 | 192.168.1.199   |
| VULN-1014 | CVE-2024-3175 | MEDIUM     |          9.9 | 192.168.1.84    |
| VULN-1015 | CVE-2024-1958 | CRITICAL   |          5.2 | 192.168.1.167   |
| VULN-1016 | CVE-2024-4915 | MEDIUM     |          6.3 | 192.168.1.206   |
| VULN-1017 | CVE-2024-3335 | MEDIUM     |          4.4 | 192.168.1.124   |
| VULN-1018 | CVE-2024-9262 | CRITICAL   |          1.5 | 192.168.1.185   |
| VULN-1019 | CVE-2024-5144 | HIGH       |          6.9 | 192.168.1.212   |
| VULN-1020 | CVE-2024-2669 | CRITICAL   |          2.5 | 192.168.1.3     |
| VULN-1021 | CVE-2024-3605 | HIGH       |          3.9 | 192.168.1.147   |
| VULN-1022 | CVE-2024-7135 | MEDIUM     |          6.5 | 192.168.1.36    |
| VULN-1023 | CVE-2024-1305 | CRITICAL   |          2.2 | 192.168.1.59    |
| VULN-1024 | CVE-2024-2312 | MEDIUM     |          8.7 | 192.168.1.143   |
| VULN-1025 | CVE-2024-5438 | CRITICAL   |          9   | 192.168.1.101   |
| VULN-1026 | CVE-2024-1559 | CRITICAL   |          6.4 | 192.168.1.84    |
| VULN-1027 | CVE-2024-3612 | HIGH       |          4.8 | 192.168.1.45    |
| VULN-1028 | CVE-2024-7837 | HIGH       |          2   | 192.168.1.60    |
| VULN-1029 | CVE-2024-5706 | LOW        |          4.4 | 192.168.1.141   |
| VULN-1030 | CVE-2024-3190 | LOW        |          2.4 | 192.168.1.15    |
| VULN-1031 | CVE-2024-9262 | CRITICAL   |          2.7 | 192.168.1.6     |
| VULN-1032 | CVE-2024-1543 | HIGH       |          3.4 | 192.168.1.244   |
| VULN-1033 | CVE-2024-8005 | HIGH       |          2.4 | 192.168.1.225   |
| VULN-1034 | CVE-2024-4058 | LOW        |          4.9 | 192.168.1.221   |
| VULN-1035 | CVE-2024-8584 | HIGH       |          7   | 192.168.1.135   |
| VULN-1036 | CVE-2024-6264 | HIGH       |          6.6 | 192.168.1.20    |
| VULN-1037 | CVE-2024-5408 | HIGH       |          7.9 | 192.168.1.216   |
| VULN-1038 | CVE-2024-7857 | LOW        |          1.7 | 192.168.1.89    |
| VULN-1039 | CVE-2024-8463 | CRITICAL   |          4.3 | 192.168.1.144   |
| VULN-1040 | CVE-2024-1843 | LOW        |          1.7 | 192.168.1.128   |
| VULN-1041 | CVE-2024-9654 | LOW        |          2.6 | 192.168.1.41    |
| VULN-1042 | CVE-2024-5123 | MEDIUM     |          1.3 | 192.168.1.107   |
| VULN-1043 | CVE-2024-1609 | LOW        |          1.7 | 192.168.1.82    |
| VULN-1044 | CVE-2024-6548 | HIGH       |          7.1 | 192.168.1.154   |
| VULN-1045 | CVE-2024-2801 | MEDIUM     |          1.9 | 192.168.1.137   |
| VULN-1046 | CVE-2024-8928 | LOW        |          1.3 | 192.168.1.207   |
| VULN-1047 | CVE-2024-6165 | LOW        |          3.5 | 192.168.1.87    |
| VULN-1048 | CVE-2024-8044 | MEDIUM     |          4.4 | 192.168.1.53    |
| VULN-1049 | CVE-2024-7389 | HIGH       |          3.9 | 192.168.1.159   |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.png)

<!-- AUTO-GENERATED-END -->



