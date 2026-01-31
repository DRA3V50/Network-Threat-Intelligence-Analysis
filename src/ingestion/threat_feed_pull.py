import pandas as pd
from pathlib import Path
import random


def pull_osint_iocs(output_dir: Path, max_rows: int = 15):
    """
    Pulls OSINT threat indicators and writes a capped CSV.
    """

    print("[*] Pulling OSINT threat indicators")

    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "osint_iocs.csv"

    # ---- SAMPLE OSINT DATA (replace with real feeds later) ----
    iocs = []
    for i in range(1, 51):
        iocs.append({
            "ioc": f"malicious{i}.com",
            "type": "domain",
            "confidence": random.randint(60, 95),
            "source": "OSINT-Feed"
        })

    df = pd.DataFrame(iocs)

    # ---- FIX: CAP ROWS FOR PRESENTATION ----
    df = (
        df.sort_values("confidence", ascending=False)
          .head(max_rows)
          .reset_index(drop=True)
    )

    df.to_csv(output_path, index=False)

    print(f"[+] OSINT IOCs written to {output_path}")
