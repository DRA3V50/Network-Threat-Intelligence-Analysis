import csv
from pathlib import Path
import random

VULNS = [
    ("CVE-2024-3011", "Critical"),
    ("CVE-2023-2198", "High"),
    ("CVE-2022-4421", "Medium"),
    ("CVE-2021-3375", "Low"),
    ("CVE-2020-1195", "Medium"),
]

SEVERITY_SCORE = {
    "Critical": 9,
    "High": 7,
    "Medium": 5,
    "Low": 3,
}


def generate_vulnerabilities(output_dir: Path, limit: int = 10):
    print("[*] Generating vulnerability findings")

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "vuln_scan_sample.csv"

    rows = []
    for cve, severity in VULNS[:limit]:
        rows.append(
            {
                "vulnerability": cve,
                "severity": severity,
                "severity_score": SEVERITY_SCORE[severity],
            }
        )

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["vulnerability", "severity", "severity_score"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"[+] Vulnerability report written to {output_file}")
