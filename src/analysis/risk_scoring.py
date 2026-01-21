import csv
import os

def score_vulnerabilities(matches, vuln_path="build/vulnerabilities/vuln_scan_sample.csv"):
    """
    Simple risk scoring function.
    Writes high-risk vulnerabilities CSV in outputs/logs
    """
    os.makedirs("outputs/logs", exist_ok=True)

    high_risk = []

    with open(vuln_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            severity = int(row.get("Severity", 0))
            vuln_name = row.get("Vulnerability", "Unknown")
            if severity >= 7 or any(vuln_name in m for m in matches):
                high_risk.append(row)

    with open("outputs/logs/high_risk_vulns.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(high_risk)

    print(f"[+] Risk scoring complete: {len(high_risk)} high-risk items")
