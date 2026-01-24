
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
**Generated (UTC):** 2026-01-24 13:28

### 🛰️ High-Confidence Threat Indicators
Indicators correlated from curated open-source intelligence feeds.

| ioc_type   | ioc_value                        |   confidence | source                   |
|:-----------|:---------------------------------|-------------:|:-------------------------|
| URL        | http://bad387.example/path       |           95 | Open-Source Intelligence |
| HASH       | 62380784e36989f83c0b380a6fe5d0a5 |           91 | Open-Source Intelligence |
| DOMAIN     | malicious931.com                 |           90 | Open-Source Intelligence |
| HASH       | bc0c0a1fcd77b39cafd1e26721023971 |           90 | Open-Source Intelligence |
| HASH       | ddcf9040e42e9e6273118b9b3047f653 |           90 | Open-Source Intelligence |
| IP         | 185.151.181.142                  |           89 | Open-Source Intelligence |
| HASH       | 5b45d5c95b9d43147f8480dd134e6d54 |           88 | Open-Source Intelligence |
| DOMAIN     | malicious554.com                 |           88 | Open-Source Intelligence |
| IP         | 185.35.10.156                    |           88 | Open-Source Intelligence |
| IP         | 185.173.26.69                    |           88 | Open-Source Intelligence |

### 🔥 Highest-Risk Vulnerabilities
Prioritized based on exploitability and potential operational impact.

| vuln_id   | cve           | severity   |   risk_score | affected_host   |
|:----------|:--------------|:-----------|-------------:|:----------------|
| VULN-1000 | CVE-2024-6163 | HIGH       |          7.9 | 192.168.1.90    |
| VULN-1001 | CVE-2024-5476 | MEDIUM     |          1.2 | 192.168.1.104   |
| VULN-1002 | CVE-2024-8329 | LOW        |          5.8 | 192.168.1.14    |
| VULN-1003 | CVE-2024-6233 | HIGH       |          7.8 | 192.168.1.152   |
| VULN-1004 | CVE-2024-1756 | HIGH       |          8.1 | 192.168.1.97    |
| VULN-1005 | CVE-2024-9095 | CRITICAL   |         10   | 192.168.1.234   |
| VULN-1006 | CVE-2024-4208 | LOW        |          4.6 | 192.168.1.52    |
| VULN-1007 | CVE-2024-4954 | HIGH       |          4.9 | 192.168.1.178   |
| VULN-1008 | CVE-2024-7219 | HIGH       |          1.2 | 192.168.1.184   |
| VULN-1009 | CVE-2024-3106 | LOW        |          8.6 | 192.168.1.189   |
| VULN-1010 | CVE-2024-1404 | MEDIUM     |          7   | 192.168.1.127   |
| VULN-1011 | CVE-2024-9136 | MEDIUM     |          5.2 | 192.168.1.158   |
| VULN-1012 | CVE-2024-5914 | LOW        |          5.7 | 192.168.1.243   |
| VULN-1013 | CVE-2024-7899 | CRITICAL   |          2.2 | 192.168.1.76    |
| VULN-1014 | CVE-2024-9458 | LOW        |          5.5 | 192.168.1.205   |
| VULN-1015 | CVE-2024-3856 | LOW        |          3.3 | 192.168.1.38    |
| VULN-1016 | CVE-2024-5059 | HIGH       |          8.6 | 192.168.1.214   |
| VULN-1017 | CVE-2024-5682 | MEDIUM     |          8.6 | 192.168.1.132   |
| VULN-1018 | CVE-2024-9620 | MEDIUM     |          4.8 | 192.168.1.230   |
| VULN-1019 | CVE-2024-4432 | MEDIUM     |          7.2 | 192.168.1.50    |
| VULN-1020 | CVE-2024-6019 | CRITICAL   |          8.2 | 192.168.1.108   |
| VULN-1021 | CVE-2024-8770 | HIGH       |          6.9 | 192.168.1.54    |
| VULN-1022 | CVE-2024-9031 | LOW        |          9.9 | 192.168.1.95    |
| VULN-1023 | CVE-2024-7100 | LOW        |          8.9 | 192.168.1.251   |
| VULN-1024 | CVE-2024-2718 | HIGH       |          6.7 | 192.168.1.148   |
| VULN-1025 | CVE-2024-9548 | HIGH       |          1.6 | 192.168.1.37    |
| VULN-1026 | CVE-2024-4530 | LOW        |          1   | 192.168.1.69    |
| VULN-1027 | CVE-2024-6399 | LOW        |          1.1 | 192.168.1.116   |
| VULN-1028 | CVE-2024-6499 | CRITICAL   |          9.9 | 192.168.1.152   |
| VULN-1029 | CVE-2024-9902 | CRITICAL   |          5   | 192.168.1.40    |
| VULN-1030 | CVE-2024-5388 | CRITICAL   |          3.8 | 192.168.1.193   |
| VULN-1031 | CVE-2024-6850 | MEDIUM     |          2.2 | 192.168.1.203   |
| VULN-1032 | CVE-2024-3984 | HIGH       |          8.7 | 192.168.1.62    |
| VULN-1033 | CVE-2024-2216 | HIGH       |          5   | 192.168.1.173   |
| VULN-1034 | CVE-2024-1083 | HIGH       |         10   | 192.168.1.196   |
| VULN-1035 | CVE-2024-8431 | CRITICAL   |          5.8 | 192.168.1.174   |
| VULN-1036 | CVE-2024-2038 | HIGH       |          7.3 | 192.168.1.67    |
| VULN-1037 | CVE-2024-4447 | MEDIUM     |          4.3 | 192.168.1.213   |
| VULN-1038 | CVE-2024-3453 | LOW        |          9.9 | 192.168.1.1     |
| VULN-1039 | CVE-2024-1178 | CRITICAL   |          8.8 | 192.168.1.238   |
| VULN-1040 | CVE-2024-7082 | CRITICAL   |          8.3 | 192.168.1.189   |
| VULN-1041 | CVE-2024-7485 | CRITICAL   |          3.5 | 192.168.1.137   |
| VULN-1042 | CVE-2024-2839 | MEDIUM     |          3.1 | 192.168.1.70    |
| VULN-1043 | CVE-2024-6112 | CRITICAL   |          7.5 | 192.168.1.195   |
| VULN-1044 | CVE-2024-6853 | HIGH       |          6.8 | 192.168.1.164   |
| VULN-1045 | CVE-2024-7425 | LOW        |          5   | 192.168.1.48    |
| VULN-1046 | CVE-2024-1331 | HIGH       |          7.8 | 192.168.1.186   |
| VULN-1047 | CVE-2024-6771 | LOW        |          9.9 | 192.168.1.182   |
| VULN-1048 | CVE-2024-7644 | MEDIUM     |          9.8 | 192.168.1.247   |
| VULN-1049 | CVE-2024-1528 | LOW        |          6.6 | 192.168.1.1     |

### 📊 Network Activity Overview
![Top Source IPs](build/charts/top_source_ips.png)

<!-- AUTO-GENERATED-END -->

