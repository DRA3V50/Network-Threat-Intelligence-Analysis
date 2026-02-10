from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------------------------------------------
# Defaults
# -------------------------------------------------------------------
DEFAULT_CHART_DIR = Path("build/charts")
DEFAULT_CHART_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_OUTPUT = DEFAULT_CHART_DIR / "network_activity.png"


# -------------------------------------------------------------------
# Unified Network Activity Chart
# -------------------------------------------------------------------
def generate_unified_network_chart(
    network_csv: Path = None,
    pcaps_csv: Path = None,
    iocs_csv: Path = None,
    vulns_csv: Path = None,
    output_path: Path = None,
    **kwargs,   # <-- absorbs any future args safely
):
    """
    SOC-grade network activity visualization.

    This function is intentionally signature-flexible to prevent
    pipeline breakage as orchestration evolves.
    """

    # ---------------------------
    # Resolve CSV input
    # ---------------------------
    csv_path = network_csv or pcaps_csv
    if csv_path is None:
        raise ValueError("No network / PCAP CSV provided")

    # ---------------------------
    # Resolve output path
    # ---------------------------
    output = output_path or DEFAULT_OUTPUT
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    # ---------------------------
    # Load & sanitize data
    # ---------------------------
    df = pd.read_csv(csv_path)

    if "count" not in df.columns or "source_ip" not in df.columns:
        raise ValueError("Expected columns: source_ip, count")

    df["count"] = pd.to_numeric(df["count"], errors="coerce").fillna(0)
    df = df.sort_values("count", ascending=False).head(10)

    # ---------------------------
    # Styling — restrained, clinical
    # ---------------------------
    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor("#0d0d0d")
    ax.set_facecolor("#111111")

    bars = ax.bar(
        df["source_ip"],
        df["count"],
        color="#b11226",        # Umbrella red (subtle)
        edgecolor="#7a0c19",
        linewidth=0.9
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
    plt.savefig(output, dpi=150)
    plt.close()

    print(f"[+] Network activity chart written to {output}")
