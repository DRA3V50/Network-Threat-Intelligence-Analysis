import csv
import random
from pathlib import Path


def generate_vulnerabilities(output_dir: Path, count: int = 50):
    """
    Generate simulated vulnerability scan results
    """

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "vuln_scan_sample.csv"

    severities = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "vuln_id",
            "cve",
            "severity",
            "risk_score",
            "affected_host"
        ])

        for i in range(count):
            severity = random.choice(severities)
            risk_score = round(random.uniform(1, 10), 1)

            writer.writerow([
                f"VULN-{1000+i}",
                f"CVE-2024-{random.randint(1000,9999)}",
                severity,
                risk_score,
                f"192.168.1.{random.randint(1,254)}"
            ])

    print(f"[+] Vulnerability report written to {output_file}")
