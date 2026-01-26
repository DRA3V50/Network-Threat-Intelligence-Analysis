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
        print("[!] Invalid or empty CSV, skipping chart")
        return

    # Sort so bars are meaningful
    df = df.sort_values("count", ascending=False)

    # Normalize counts for color intensity
    max_count = df["count"].max()
    colors = [
        (0.7, 0.0, 0.0, min(1.0, 0.3 + (c / max_count)))
        for c in df["count"]
    ]

    # ---- HARD STYLE RESET (no matplotlib surprises) ----
    plt.rcParams.update(plt.rcParamsDefault)

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor("#0b0b0b")
    ax.set_facecolor("#0b0b0b")

    ax.bar(
        df["source_ip"],
        df["count"],
        color=colors,
        edgecolor="white",
        linewidth=0.8
    )

    ax.set_title(
        "Top Source IPs by Connection Volume",
        color="white",
        fontsize=11,
        pad=10
    )
    ax.set_xlabel("Source IP", color="white", fontsize=9)
    ax.set_ylabel("Connection Count", color="white", fontsize=9)

    ax.tick_params(axis="x", colors="white", labelrotation=45, labelsize=8)
    ax.tick_params(axis="y", colors="white", labelsize=8)

    for spine in ax.spines.values():
        spine.set_color("white")

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=140, facecolor=fig.get_facecolor())
    plt.close()

    print(f"[+] Chart written to {output_path}")
