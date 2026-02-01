import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def generate_unified_network_chart(
    iocs_csv: Path,
    pcaps_csv: Path,
    vulns_csv: Path,
    output_path: Path,
):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # =========================
    # LOAD DATA
    # =========================
    df_iocs = pd.read_csv(iocs_csv)
    df_pcaps = pd.read_csv(pcaps_csv)
    df_vulns = pd.read_csv(vulns_csv)

    # =========================
    # IOC AGGREGATION
    # =========================
    ioc_col = next(
        (c for c in df_iocs.columns if "ioc" in c.lower() or "indicator" in c.lower()),
        df_iocs.columns[0],
    )

    df_iocs_agg = (
        df_iocs[ioc_col]
        .astype(str)
        .value_counts()
        .head(10)
        .reset_index()
    )
    df_iocs_agg.columns = ["label", "count"]

    # =========================
    # PCAP AGGREGATION
    # =========================
    src_col = next(
        (c for c in df_pcaps.columns if "source" in c.lower()),
        df_pcaps.columns[0],
    )

    df_pcaps_agg = (
        df_pcaps[src_col]
        .astype(str)
        .value_counts()
        .head(10)
        .reset_index()
    )
    df_pcaps_agg.columns = ["label", "count"]

    # =========================
    # VULNERABILITY AGGREGATION
    # =========================
    sev_col = next(
        (c for c in df_vulns.columns if "severity" in c.lower()),
        df_vulns.columns[0],
    )

    df_vulns_agg = (
        df_vulns[sev_col]
        .astype(str)
        .value_counts()
        .reset_index()
    )
    df_vulns_agg.columns = ["label", "count"]

    # =========================
    # PLOTTING
    # =========================
    plt.figure(figsize=(16, 8))
    plt.style.use("dark_background")

    current_x = 0
    xtick_positions = []
    xtick_labels = []

    def plot_block(df, color, title):
        nonlocal current_x
        xs = list(range(current_x, current_x + len(df)))
        ys = df["count"].values.tolist()

        plt.bar(xs, ys, color=color, label=title)

        xtick_positions.extend(xs)
        xtick_labels.extend(df["label"].tolist())

        current_x += len(df) + 1  # spacing gap

    plot_block(df_iocs_agg, "#ff2b2b", "Top IOCs")
    plot_block(df_pcaps_agg, "#ff6b6b", "Top Source IPs")
    plot_block(df_vulns_agg, "#ffffff", "Vulnerabilities")

    plt.xticks(xtick_positions, xtick_labels, rotation=45, ha="right", fontsize=8)
    plt.ylabel("Observed Count")
    plt.title("Unified Network Threat Activity")
    plt.legend()
    plt.tight_layout()

    plt.savefig(output_path, dpi=200)
    plt.close()

    print(f"[+] Unified network chart written to {output_path}")
