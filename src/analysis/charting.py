from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------
BUILD_DIR = Path("build/charts")
BUILD_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_CHART = BUILD_DIR / "network_activity.png"


# -------------------------------------------------------------------
# Unified Network Activity Chart
# -------------------------------------------------------------------
def generate_unified_network_chart(df_network, df_iocs=None, df_vulns=None):
    """
    Generates a SOC-grade network activity visualization.
    Theme: Dark, clinical, high-contrast (Umbrella / RE-inspired).
    """

    # ---------------------------
    # Defensive casting (CRITICAL)
    # ---------------------------
    df = df_network.copy()
    df["count"] = pd.to_numeric(df["count"], errors="coerce").fillna(0)

    df = df.sort_values("count", ascending=False).head(10)

    # ---------------------------
    # Style configuration
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
        color="#b11226",        # Umbrella red (muted)
        edgecolor="#7a0c19",
        linewidth=0.8
    )

    # ---------------------------
    # Labels & title
    # ---------------------------
    ax.set_title(
        "Network Threat Activity Overview",
        fontsize=14,
        color="#e6e6e6",
        pad=14
    )

    ax.set_xlabel("Source IP Address", fontsize=10, color="#cfcfcf", labelpad=8)
    ax.set_ylabel("Observed Connection Volume", fontsize=10, color="#cfcfcf", labelpad=8)

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
    # Subtle data labels (not noisy)
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
    # Layout & save
    # ---------------------------
    plt.tight_layout()
    plt.savefig(OUTPUT_CHART, dpi=150)
    plt.close()

    print(f"[+] Network activity chart written to {OUTPUT_CHART}")
