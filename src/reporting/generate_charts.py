import matplotlib.pyplot as plt
import os


CHART_DIR = "charts"
os.makedirs(CHART_DIR, exist_ok=True)


def generate_threat_posture_chart(scores):
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor("#0D1117")
    ax.set_facecolor("#0D1117")

    categories = [
        "IOC Pressure",
        "Vulnerability Surface",
        "Suspicious Traffic"
    ]

    values = [
        scores["ioc_score"],
        scores["vuln_score"],
        scores["network_score"]
    ]

    bars = ax.bar(categories, values)

    ax.set_title(
        "Operational Threat Exposure Index",
        fontsize=14,
        pad=18,
        fontweight="bold"
    )

    ax.set_ylabel("Normalized Risk Contribution")

    ax.set_ylim(0, 100)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height}",
            ha="center",
            va="bottom"
        )

    output_path = os.path.join(CHART_DIR, "threat_posture.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def generate_network_activity_chart(protocol_distribution):
    fig, ax = plt.subplots(figsize=(8, 5))

    protocols = list(protocol_distribution.keys())
    counts = list(protocol_distribution.values())

    ax.bar(protocols, counts)

    ax.set_title(
        "Observed Network Protocol Distribution",
        fontsize=14,
        pad=18,
        fontweight="bold"
    )

    ax.set_ylabel("Packet Count")

    output_path = os.path.join(CHART_DIR, "network_protocols.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()
