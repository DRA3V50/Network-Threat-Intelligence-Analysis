import csv
import random
from pathlib import Path

df = df.sort_values("confidence", ascending=False).head(7)

def pull_osint_iocs(output_dir: Path, count: int = 50):
    """
    Generate simulated OSINT Indicators of Compromise
    """

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "osint_iocs.csv"

    ioc_types = ["IP", "DOMAIN", "URL", "HASH"]

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "ioc_type",
            "ioc_value",
            "confidence",
            "source"
        ])

        for _ in range(count):
            ioc_type = random.choice(ioc_types)

            if ioc_type == "IP":
                value = f"185.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
            elif ioc_type == "DOMAIN":
                value = f"malicious{random.randint(100,999)}.com"
            elif ioc_type == "URL":
                value = f"http://bad{random.randint(100,999)}.example/path"
            else:
                value = f"{random.getrandbits(128):032x}"

            writer.writerow([
                ioc_type,
                value,
                random.randint(60, 95),
                "OSINT-SIM"
            ])

    print(f"[+] OSINT IOCs written to {output_file}")
