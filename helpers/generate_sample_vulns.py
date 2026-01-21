import csv
import os

os.makedirs("build/vulnerabilities", exist_ok=True)

with open("build/vulnerabilities/vuln_scan_sample.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Vulnerability", "Severity"])
    writer.writeheader()
    writer.writerow({"Vulnerability": "CVE-2025-1234", "Severity": 9})

print("[+] Sample vulnerability CSV generated in build/vulnerabilities/vuln_scan_sample.csv")
