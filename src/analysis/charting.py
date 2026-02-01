from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def generate_unified_network_chart(
    iocs_csv: Path,
    vulns_csv: Path,
    pcaps_csv: Path,
    output_path: Path,
    top_n: int = 10,
):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # -------------------------
    # Load data safely
    # -------------------------
    df_iocs = pd.read_csv(iocs_csv)
    df_vulns = pd.read_csv(vulns_csv)
    df_pcaps = pd.read_csv(pcaps_csv)

    # -------------------------
    # Normalize schemas (DEFENSIVE)
    # -------------------------
    # IOCs
    ioc_value_col = next(c for c in df_iocs.columns if "value" in c.lower())
    ioc_conf_col = next(c for c in df_iocs.columns if "confidence" in c.lower())

    df_iocs = (
        df_iocs[[ioc_value_col, ioc_conf_col]]
        .rename(columns={ioc_value_col: "label", ioc_conf_col: "score"})
        .sort_values("score", ascending=False)
        .head(top_n)
    )

    # Vulnerabilities
    vuln_name_col = next(c for c in df_vulns.columns if "vuln" in c.lower() or "cve" in c.lower())
    vuln_sev_col = next(c for c in df_vulns.columns if "severity" in c.lower())

    df_vulns = (
        df_vulns[[vuln_name_col, vuln_sev_col]]
        .rename(columns={vuln_name_col: "label", vuln_sev_col: "score"})
        .sort_values("score", ascending=False)
        .head(top_n)
    )

    # PCAP Source IPs
    src_ip_col = next(c for c in df_pcaps.columns if "ip" in c.lower())
    count_col = next(c for c in df_pcaps.columns if "count" in c.lower())

    df_pcaps = (
        df_pcaps[[src_ip_col, count_col]]
        .rename(columns={src_ip_col: "label", count_col: "score"})
        .sort_values("score", ascending=False)
        .head(top_n)
    )

    # -------------------------
    # Plot layout logic
    # -------------------------
    fig, ax = plt.subplots(figsize=(20, 9))
    fig.patch.set_facecolor("#121212")
    ax.set_facecolor("#121212")

    x_cursor = 0
    gap = 2

    def plot_block(df, color, title):
        nonlocal x_cursor

        x_vals = np.arange(len(df)) + x_cursor
        ax.bar(x_vals, df["score"], color=color, alpha=0.9)

        ax.text(
            x_vals.mean(),
            max(df["score"]) * 1.08,
            title,
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold",
            color="white",
        )

        for x, label in zip(x_vals, df["label"]):
            ax.text(
                x,
                -max(df["score"]) * 0.05,
                str(label),
                rotation=45,
                ha="right",
                va="top",
                fontsize=8,
                color="white",
            )

        x_cursor = x_vals[-1] + gap + 1

    # -------------------------
    # Draw blocks (ORIGINAL STYLE)
    # -------------------------
    plot_block(df_pcaps, "#ff4d4d", "Top Source IPs")
    plot_block(df_vulns, "#ff9933", "Top Vulnerabilities")
    plot_block(df_iocs, "#b84cff", "High-Confidence IOCs")

    # -------------------------
    # Final styling
    # -------------------------
    ax.set_title(
        "Comprehensive Network Threat Activity Overview",
        fontsize=16,
        fontweight="bold",
        color="white",
        pad=20,
    )

    ax.set_ylabel("Event Count / Severity / Confidence", color="white")
    ax.set_xticks([])

    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("#444")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())
    plt.close()

    print(f"[+] Unified network chart written to {output_path}")
