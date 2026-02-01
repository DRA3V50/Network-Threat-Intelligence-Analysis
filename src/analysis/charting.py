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
    # LOAD DATA SAFELY
    # =========================
    df_iocs = pd.read_csv(iocs_csv)
    df_pcaps = pd.read_csv(pcaps_csv)
    df_vulns = pd.read_csv(vulns_csv)

    # =========================
    # NORMALIZE IOC DATA
    # =========================
    # Detect usable columns automatically
    ioc_value_col = next(
        (c for c in df_iocs.columns if "ioc" in c.lower() or "indicator" in c.lower()),
        df_iocs.columns[0],
    )

    df_iocs_agg = (
        df_iocs[ioc_value_col]
        .value_counts()
        .head(10)
        .reset_index()
        .rename(columns={"index": "label", ioc_value_col: "count"})
    )

    # =========================
    # NORMALIZE PCAP DATA
    # =========================
    src_col = next(
        (c for c in df_pcaps.columns if "source" in c.lower()),
        df_pcaps.columns[0],
    )

    df_pcaps_agg = (
        df_pcaps[src_col]
        .value_counts()
        .head(10)
        .reset_index()
        .rename(columns={"index": "label", src_col: "count"})
    )

    # =========================
    # NORMALIZE VULN DATA
    # =========================
    sev_col = next(
        (c for c in df_vulns.columns if "severity" in c.lower()),
        df_vulns.columns[0],
    )

    df_vulns_agg = (
        df_vulns[sev_col]
        .value_counts()
        .reset_index()
        .rename(columns={"index": "label", sev_col: "count"})
    )

    # =========================
    # PLOT (RESIDENT EVIL STYLE)
    # =========================
    plt.figure(figsize=(14, 8))
    plt.style.use("dark_background")

    x_offset = 0

    def plot_block(df, color, title):
        nonlocal x_offset
        xs = range(x_offset, x_offset + len(df))
        plt.bar(xs, df["count"], color=color, label=title)
        plt.xticks(xs, df["label"], rotation=45, ha="right", fontsize=8)
        x_offset += len(df) + 1

    plot_block(df_iocs_agg, "#ff2b2b", "Top IOCs")
    plot_block(df_pcaps_agg, "#ff6b6b", "Top Source IPs")
    plot_block(df_vulns_agg, "#ffffff", "Vulnerabilities")

    plt.title("Unified Network Threat Activity", fontsize=16, color="white")
    plt.ylabel("Observed Count", color="white")
    plt.legend()
    plt.tight_layout()

    plt.savefig(output_path, dpi=200)
    plt.close()

    print(f"[+] Unified network chart written to {output_path}")

