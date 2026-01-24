import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path("build/vulnerabilities")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "vuln_scan_sample.csv"

def generate_vulnerabilities():
    data = [
        ("VULN-1001", "CVE-2024-7454", "CRITICAL", 9.6, "192.168.1.211"),
        ("VULN-1002", "CVE-2024-8975", "HIGH", 9.2, "192.168.1.225"),
        ("VULN-1003", "CVE-2024-9229", "CRITICAL", 8.9, "192.168.1.41"),
        ("VULN-1004", "CVE-2024-3153", "MEDIUM", 6.4, "192.168.1.242"),
        ("VULN-1005", "CVE-2024-4382", "MEDIUM", 5.8, "192.168.1.29"),
        ("VULN-1006", "CVE-2024-9204", "LOW", 4.2, "192.168.1.214"),
        ("VULN-1007", "CVE-2024-1362", "LOW", 3.1, "192.168.1.187"),
    ]

    df = pd.DataFrame(
        data,
        columns=["vuln_id", "cve", "severity", "risk_score", "affected_host"]
    )

    df = df.sort_values("risk_score", ascending=False).head(7)

    df.to_csv(OUTPUT_FILE, index=False)

if __name__ == "__main__":
    generate_vulnerabilities()
