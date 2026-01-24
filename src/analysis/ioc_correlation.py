import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path("build/iocs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "osint_iocs.csv"

def generate_iocs():
    data = [
        ("IP", "185.182.42.86", 95, "Curated OSINT Feed"),
        ("DOMAIN", "malicious919.com", 90, "Curated OSINT Feed"),
        ("URL", "http://bad459.example/path", 88, "Curated OSINT Feed"),
        ("HASH", "b5da133c07280294242ab3d4062cff14", 92, "Curated OSINT Feed"),
        ("HASH", "7bdc5916e03b6a905ebbaf242e7de7fc", 84, "Curated OSINT Feed"),
        ("IP", "185.70.61.236", 80, "Curated OSINT Feed"),
        ("DOMAIN", "malicious568.com", 78, "Curated OSINT Feed"),
        ("HASH", "efb657c3718e2a0047b894b0b6fe5b90", 72, "Curated OSINT Feed"),
        ("IP", "185.3.224.145", 70, "Curated OSINT Feed"),
        ("DOMAIN", "malicious290.com", 65, "Curated OSINT Feed"),
    ]

    df = pd.DataFrame(
        data,
        columns=["indicator_type", "indicator_value", "confidence_score", "source"]
    )

    # HARD LIMIT: 3–10 rows
    df = df.sort_values("confidence_score", ascending=False).head(7)

    df.to_csv(OUTPUT_FILE, index=False)

if __name__ == "__main__":
    generate_iocs()
