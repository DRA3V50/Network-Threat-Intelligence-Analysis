from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------
CHART_DIR = Path("build/charts")
CHART_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_CHART = CHART_DIR / "network_activity.png"


# -------------------------------------------------------------------
# Unified Network Activity Chart
# -------------------------------------------------------------------
def generate_unified_network_chart(
    network_csv: Path = None,
    pcaps_csv: Path = None,
    iocs_csv: Path = None,
    vulns_csv: Path = None,
):
    """
    Generates a SOC-grade network activity visualization.

    Accepts multiple CSV argument names to remain pipeline-compatible.
    """

    # ---------------------------
    # Resolve input source
    # ---------------------------
    csv_path = network_csv or pcaps_csv

    if csv_path is None:
        raise ValueError("No network/pcap CSV provided to chart generator")

    # ---------------------------
    # Load network data
    # ---------------------------
    df = pd.read_csv(csv_path)

    # Defensive typing
    df["count"] = pd.to_numeric(df["count"], errors="coerce").fillna(0)
    df = df.sort_values("count", ascending=False).head(10)

    # ---------------------------
    # Styling (serious, restrained)
    # ---------------------------
    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor("#0e0e0e")
    ax.set_facecolor("#121212")

    # ---------------------------
    # Bar chart
    # ---------------------------
    bars = ax.bar(
        df["source_ip"],
        df["count"],
        color="#b11226",      # restrained Umbrella red
        edgecolor="#7a0c19",
        linewidth=0.8
    )

    # ---------------------------
    # Titles & labels
    # ---------------------------
    ax.set_title(
        "Network Threat Activity Overview",
        fontsize=14,
        color="#e6e6e6",
        pad=14
    )

    ax.set_xlabel(
        "Source IP Address",
        fontsize=10,
        color="#cfcfcf",
        labelpad=8
    )

    ax.set_ylabel(
        "Observed Connection Volume",
        fontsize=10,
        color="#cfcfcf",
        labelpad=8
    )

    # ---------------------------
    # Grid & ticks
    # ---------------------------
    ax.tick_params(axis="x", colors="#cfcfcf", rotation=30)
    ax.tick_params(axis="y", colors="#cfcfcf")

    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.4,
        color="#2a2a2a",
        alpha=0.6
    )

    # ---------------------------
    # Value labels
    # ---------------------------
    max_val = df["count"].max()

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + max_val * 0.02,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=9,
            color="#d9d9d9"
        )

    # ---------------------------
    # Save chart
    # ---------------------------
    plt.tight_layout()
    plt.savefig(OUTPUT_CHART, dpi=150)
    plt.close()

    print(f"[+] Network activity chart written to {OUTPUT_CHART}")


