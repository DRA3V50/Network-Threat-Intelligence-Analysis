import pandas as pd
from pathlib import Path
import random


def generate_vulnerabilities(output_dir: Path, max_rows: int = 15):
    """
    Generates vulnerability findings and writes a capped CSV.
    """

    print("[*] Generating vulnerability findings")

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "vuln_scan_sample.csv"

    # ---- SAMPLE VULNERABILITY DATA ----
    vulns = []
    for i in range(1, 51):
        vulns.append({
            "vuln_id": f"VULN-{1000 + i}",
            "service": random.choice(["SSH", "HTTP", "HTTPS", "FTP"]),
            "severity": random.randint(1, 10),
            "description": "Sample vulnerability finding"
        })

    df = pd.DataFrame(vulns)

    # ---- FIX: SORT BY SEVERITY + CAP ROWS ----
    df = (
        df.sort_values("severity", ascending=False)
          .head(max_rows)
          .reset_index(drop=True)
    )

    df.to_csv(output_path, index=False)

    print(f"[+] Vulnerability report written to {output_path}")
