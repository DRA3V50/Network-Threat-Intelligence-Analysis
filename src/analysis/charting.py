import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def generate_top_source_ips_chart(csv_path, output_path, max_rows=7):
    csv_path = Path(csv_path)
    output_path = Path(output_path)

    if not csv_path.exists():
        print(f"[!] CSV not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)

    if df.empty:
        print("[!] CSV empty, skipping chart")
        return

    # -----------------------------
    # 🔒 DATA SANITY (CRITICAL FIX)
    # -----------------------------
    if "source_ip" not in df.columns:
        print("[!] Missing source_ip column")
        return

    # If count exists → force numeric
    if "count" in df.columns:
        df["count"] = pd.to_numeric(df["count"], errors="coerce").fillna(0)
        grouped = df.groupby("source_ip", as_index=False)["count"].sum()
    else:
        # Fallback: count occurrences
        grouped = df.groupby("source_ip").size().reset_index(name="count")

    grouped = (
        grouped
        .sort_values("count", ascending=False)
        .head(max_rows)
    )

    if grouped.empty:
        print("[!] No data after aggregation")
        return

    # -----------------------------
    # 🎨 VISUAL STYLE (Resident Evil)
    # -----------------------------
    plt.style.use("dark_background")
    plt.rcParams.update({
        "figure.figsize": (8, 4),
        "axes.facecolor": "#0b0b0b",
        "figure.facecolor": "#0b0b0b",
        "axes.edgecolor": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "text.color": "white",
    })

    bars = plt.bar(
        grouped["source_ip"],
        grouped["count"],
        edgecolor="white"
    )

    # 🔴 Severity gradient (light → dark red)
    max_count = grouped["count"].max()
    for bar, value in zip(bars, grouped["count"]):
        intensity = value / max_count
        bar.set_color((0.7 + 0.3 * intensity, 0, 0))

    plt.title("Top Source IPs by Observed Network Activity", fontsize=11)
    plt.xlabel("Source IP", fontsize=9)
    plt.ylabel("Connection Count", fontsize=9)

    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.yticks(fontsize=8)

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=130)
    plt.close()

    print(f"[+] Chart written to {output_path}")
