import csv
from pathlib import Path
import random

IOC_TYPES = ["ip", "domain", "hash"]

SAMPLE_IOCS = [
    "185.81.68.90",
    "185.82.113.99",
    "malicious.com",
    "badactor.net",
    "2ddbdd712c056f34bd0aa2cc",
    "193.42.157.198",
    "malwaredrop.org",
    "185.83.60.186",
]


def pull_osint_iocs(output_dir: Path, limit: int = 12):
    print("[*] Pulling OSINT threat indicators")

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "osint_iocs.csv"

    rows = []
    for value in SAMPLE_IOCS[:limit]:
        rows.append(
            {
                "ioc_value": value,
                "ioc_type": random.choice(IOC_TYPES),
                "confidence": random.randint(70, 95),
            }
        )

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["ioc_value", "ioc_type", "confidence"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"[+] OSINT IOCs written to {output_file}")
