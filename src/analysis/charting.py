import pandas as pd
import matplotlib.pyplot as plt


def generate_unified_network_chart(
    iocs_csv,
    vulns_csv,
    pcaps_csv,
    output_path,
):
    df_iocs = pd.read_csv(iocs_csv).head(10)
    df_vulns = pd.read_csv(vulns_csv).head(10)
    df_pcaps = pd.read_csv(pcaps_csv).head(10)

    fig, ax = plt.subplots(figsize=(14, 6))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # --- IOC CONFIDENCE ---
    ax.bar(
        df_iocs["type"] + ":" + df_iocs["value"],
        df_iocs["confidence"],
        color="darkred",
        label="IOC Confidence",
    )

    # --- VULNERABILITY SEVERITY ---
    ax.bar(
        df_vulns["vulnerability"],
        df_vulns["severity_score"],
        color="crimson",
        alpha=0.8,
        label="Vulnerability Severity",
    )

    # --- PCAP SOURCE IP COUNTS ---
    ax.bar(
        df_pcaps["src_ip"],
        df_pcaps["count"],
        color="red",
        alpha=0.7,
        label="Source IP Frequency",
    )

    ax.set_title(
        "Unified Network Threat Activity",
        color="red",
        fontsize=14,
    )

    ax.tick_params(axis="x", rotation=45, labelsize=8, colors="white")
    ax.tick_params(axis="y", colors="white")

    for spine in ax.spines.values():
        spine.set_color("red")

    ax.legend(facecolor="black", edgecolor="red", labelcolor="white")

    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()

