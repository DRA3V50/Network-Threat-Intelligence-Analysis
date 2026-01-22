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
    if df.empty:
        print("[!] CSV empty, skipping chart")
        return

    # ---- STYLE (Resident Evil theme) ----
    plt.style.use("dark_background")
    plt.rcParams.update({
        "figure.figsize": (7, 4),     # SMALLER
        "axes.facecolor": "#0b0b0b",
        "figure.facecolor": "#0b0b0b",
        "axes.edgecolor": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "text.color": "white",
    })

    plt.bar(
        df["source_ip"],
        df["count"],
        color="#b30000",              # Umbrella red
        edgecolor="white"
    )

    plt.title("Top Source IPs (Observed Network Activity)", fontsize=11)
    plt.xlabel("Source IP", fontsize=9)
    plt.ylabel("Connection Count", fontsize=9)

    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.yticks(fontsize=8)

    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120)   # DPI keeps it crisp but not huge
    plt.close()

    print(f"[+] Chart written to {output_path}")
