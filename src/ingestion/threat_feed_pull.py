import csv
import random
from pathlib import Path


def pull_osint_iocs(output_dir: Path, max_rows: int = 10):
    """
    Generate simulated OSINT-derived Threat Indicators
    (trimmed to highest-confidence entries for analyst relevance)
    """

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "osint_iocs.csv"

    ioc_types = ["IP", "DOMAIN", "URL", "HASH"]
    rows = []

    # ---- GENERATE RAW DATA ----
    for _ in range(30):  # generate extra, then trim
        ioc_type = random.choice(ioc_types)

        if ioc_type == "IP":
            value = f"185.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
        elif ioc_type == "DOMAIN":
            value = f"malicious{random.randint(100,999)}.com"
        elif ioc_type == "URL":
            value = f"http://bad{random.randint(100,999)}.example/path"
        else:
            value = f"{random.getrandbits(128):032x}"

        rows.append({
            "ioc_type": ioc_type,
            "ioc_value": value,
            "confidence": random.randint(60, 95),
            "source": "Open-Source Intelligence"
        })

    # ---- SORT & TRIM (CRITICAL FIX) ----
    rows = sorted(rows, key=lambda x: x["confidence"], reverse=True)
    rows = rows[:max_rows]

    # ---- WRITE FINAL CSV ----
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["ioc_type", "ioc_value", "confidence", "source"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"[+] OSINT Threat Indicators written to {output_file} ({len(rows)} rows)")
