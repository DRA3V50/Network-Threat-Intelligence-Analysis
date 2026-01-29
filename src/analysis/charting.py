import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def generate_top_source_ips_chart(csv_path, output_path):
    csv_path = Path(csv_path)
    output_path = Path(output_path)

    if not csv_path.exists():
        print(f"[!] CSV not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)

    if df.empty or "count" not in df.columns:
        print("[!] Invalid or empty CSV")
        return

    # 🔽 CRITICAL FIX: sort so heights differ visibly
    df = df.sort_values("count", ascending=False).head(7)

    # Dynamic color intensity (higher = darker red)
    max_count = df["count"].max()
    colors = [
        (0.6 + (c / max_count) * 0.4, 0, 0) for c in df["count"]
    ]

    plt.style.use("dark_background")
    plt.figure(figsize=(8, 4))
    plt.bar(df["source_ip"], df["count"], color=colors, edgecolor="white")

    plt.title("Top Source IPs by Connection Volume")
    plt.xlabel("Source IP")
    plt.ylabel("Connection Count")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=140)
    plt.close()

    print(f"[+] Chart generated: {output_path}")
