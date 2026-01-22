import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generate_top_source_ips_chart(csv_path, output_path):
    df = pd.read_csv(csv_path)

    if df.empty or "source_ip" not in df.columns:
        return False

    counts = df["source_ip"].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    counts.plot(kind="bar")
    plt.title("Top Source IPs")
    plt.xlabel("Source IP")
    plt.ylabel("Count")
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

    return True
