import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def generate_top_source_ips_chart(csv_path, output_path):
    csv_path = Path(csv_path)
    output_path = Path(output_path)

    if not csv_path.exists():
        print(f"[!] CSV not found: {csv_path}")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_path)

    if df.empty:
        print("[!] CSV is empty — skipping chart")
        return

    plt.figure(figsize=(10, 6))
    plt.bar(df["source_ip"], df["count"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Top Source IPs")
    plt.xlabel("Source IP")
    plt.ylabel("Connection Count")
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()

    print(f"[+] Chart written to {output_path}")
