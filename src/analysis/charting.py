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

    # ---- COLUMN SAFETY ----
    # Supports either "source_ip" or "ip"
    if "source_ip" in df.columns:
        ip_col = "source_ip"
    elif "ip" in df.columns:
        ip_col = "ip"
    else:
        raise ValueError("CSV must contain 'source_ip' or 'ip' column")

    if "count" not in df.columns:
        raise ValueError("CSV must contain 'count' column")

    # ---- SORT (MOST ACTIVE FIRST) ----
    df = df.sort_values("count", ascending=False)

    # ---- STYLE (Dark, serious, analyst-grade) ----
    plt.style.use("dark_background")
    plt.rcParams.update({
        "figure.figsize": (7, 4),
        "axes.facecolor": "#0b0b0b",
        "figure.facecolor": "#0b0b0b",
        "axes.edgecolor": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "text.color": "white",
    })

    # ---- COLOR GRADIENT (INTENSITY-BASED RED) ----
    norm = plt.Normalize(df["count"].min(), df["count"].max())
    colors = plt.cm.Reds(norm(df["count"]))

    plt.bar(
        df[ip_col],
        df["count"],
        color=colors,
        edgecolor="white",
        linewidth=0.6
    )

    # ---- LOG SCALE (CRITICAL FIX FOR FLAT BARS) ----
    plt.yscale("log")

    plt.title("Top Source IPs by Observed Network Activity", fontsize=11)
    plt.xlabel("Source IP", fontsize=9)
    plt.ylabel("Connection Count (log scale)", fontsize=9)

    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.yticks(fontsize=8)

    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=130)
    plt.close()

    print(f"[+] Chart written to {output_path}")

