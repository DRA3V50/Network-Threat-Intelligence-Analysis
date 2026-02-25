from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(".")
README = ROOT / "README.md"

IOCS = ROOT / "build/iocs/osint_iocs.csv"
VULNS = ROOT / "build/vulnerabilities/vuln_scan_sample.csv"
PCAPS = ROOT / "build/pcaps/top_source_ips.csv"

CHART_DIR = ROOT / "build/charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

COMPOSITE_CHART = CHART_DIR / "composite_threat.png"
NETWORK_CHART = CHART_DIR / "network_behavior.png"
VULN_CHART = CHART_DIR / "vulnerability_distribution.png"

START = "<!-- AUTO-GENERATED-START -->"
END = "<!-- AUTO-GENERATED-END -->"


# -------------------------
# Utility Styling
# -------------------------
def apply_dark_style(fig, ax):
    fig.patch.set_facecolor("#0B1118")
    ax.set_facecolor("#0B1118")

    ax.tick_params(colors="#C9D1D9")
    ax.yaxis.label.set_color("#C9D1D9")
    ax.xaxis.label.set_color("#C9D1D9")

    for spine in ax.spines.values():
        spine.set_color("#1F2A36")

    ax.yaxis.grid(True, color="#1F2A36", linewidth=0.6)
    ax.set_axisbelow(True)


def table(df, limit=8):
    return df.head(limit).to_markdown(index=False)


# -------------------------
# Normalize Vulnerabilities
# -------------------------
def normalize_vulnerabilities(df):
    df.columns = df.columns.str.lower()

    if "risk_score" not in df.columns:
        severity_map = {
            "LOW": 25,
            "MEDIUM": 50,
            "HIGH": 75,
            "CRITICAL": 100
        }
        df["risk_score"] = (
            df.get("severity", "")
            .astype(str)
            .str.upper()
            .map(severity_map)
            .fillna(0)
        )

    return df


# -------------------------
# Network Behavior Scoring
# -------------------------
def calculate_network_behavior(pcaps_df, iocs_df):

    pcaps_df.columns = pcaps_df.columns.str.lower()
    iocs_df.columns = iocs_df.columns.str.lower()

    if "source_ip" not in pcaps_df.columns:
        return pcaps_df

    pcaps_df = pcaps_df.copy()

    # Base anomaly = normalized count
    max_count = pcaps_df["count"].max()
    pcaps_df["volume_score"] = (pcaps_df["count"] / max_count) * 70

    # IOC correlation boost
    if "ip" in iocs_df.columns:
        ioc_ips = set(iocs_df["ip"].astype(str))
        pcaps_df["ioc_match"] = pcaps_df["source_ip"].astype(str).isin(ioc_ips)
        pcaps_df["correlation_boost"] = np.where(pcaps_df["ioc_match"], 30, 0)
    else:
        pcaps_df["correlation_boost"] = 0

    pcaps_df["behavior_score"] = pcaps_df["volume_score"] + pcaps_df["correlation_boost"]

    return pcaps_df.sort_values("behavior_score", ascending=False)


# -------------------------
# Composite Risk Model
# -------------------------
def generate_composite_chart(iocs_df, vulns_df, pcaps_df):

    ioc_score = float(iocs_df["confidence"].mean()) if "confidence" in iocs_df.columns else 0
    vuln_score = float(vulns_df["risk_score"].mean()) if "risk_score" in vulns_df.columns else 0
    net_score = float(pcaps_df["behavior_score"].mean()) if "behavior_score" in pcaps_df.columns else 0

    # Dynamic Weights
    ioc_weighted = ioc_score * 0.60
    vuln_weighted = vuln_score * 0.25
    net_weighted = net_score * 0.15

    values = [
        round(ioc_weighted, 1),
        round(vuln_weighted, 1),
        round(net_weighted, 1)
    ]

    composite_score = round(sum(values), 1)

    if composite_score < 30:
        tier = "LOW"
        color = "#2E8B57"
    elif composite_score < 55:
        tier = "ELEVATED"
        color = "#C47A1F"
    elif composite_score < 80:
        tier = "HIGH"
        color = "#B22222"
    else:
        tier = "CRITICAL"
        color = "#FF2E2E"

    fig, ax = plt.subplots(figsize=(10, 5))
    apply_dark_style(fig, ax)

    labels = ["Threat Intel", "Vulnerability Exposure", "Network Behavior"]

    # Purple / Gold variant bars
    colors = ["#6A0DAD", "#D4AF37", "#9370DB"]

    bars = ax.bar(labels, values, width=0.45, color=colors)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f"{height:.1f}",
            ha="center",
            color="#FFFFFF",
            fontweight="bold"
        )

    fig.text(
        0.5,
        0.92,
        f"Enterprise Threat Posture: {tier}  |  Composite Score: {composite_score}",
        ha="center",
        fontsize=13,
        color=color,
        fontweight="bold"
    )

    ax.set_ylabel("Weighted Risk Contribution")
    ax.set_ylim(0, max(values) * 1.2 if max(values) > 0 else 10)

    plt.tight_layout(rect=[0, 0, 1, 0.88])
    plt.savefig(COMPOSITE_CHART, dpi=220, facecolor=fig.get_facecolor())
    plt.close()


# -------------------------
# Network Behavior Chart
# -------------------------
def generate_network_chart(pcaps_df):

    top = pcaps_df.head(6)

    fig, ax = plt.subplots(figsize=(10, 5))
    apply_dark_style(fig, ax)

    bars = ax.bar(top["source_ip"], top["behavior_score"], width=0.45, color="#9B111E")

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f"{int(height)}",
            ha="center",
            color="#FFFFFF",
            fontweight="bold"
        )

    ax.set_title("Network Behavioral Risk Index", color="#C9D1D9")
    ax.set_ylabel("Behavior Risk Score")

    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.savefig(NETWORK_CHART, dpi=220, facecolor=fig.get_facecolor())
    plt.close()


# -------------------------
# Vulnerability Distribution
# -------------------------
def generate_vulnerability_chart(vulns_df):

    severity_counts = vulns_df["risk_score"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 5))
    apply_dark_style(fig, ax)

    ax.bar(severity_counts.index.astype(str), severity_counts.values, color="#D4AF37")

    ax.set_title("Vulnerability Severity Distribution", color="#C9D1D9")
    ax.set_ylabel("Number of Findings")

    plt.tight_layout()
    plt.savefig(VULN_CHART, dpi=220, facecolor=fig.get_facecolor())
    plt.close()


# -------------------------
# README Update
# -------------------------
def update_readme():

    iocs_df = pd.read_csv(IOCS).sort_values("confidence", ascending=False)
    vulns_df = normalize_vulnerabilities(pd.read_csv(VULNS))
    pcaps_df = pd.read_csv(PCAPS).sort_values("count", ascending=False)

    pcaps_df = calculate_network_behavior(pcaps_df, iocs_df)

    generate_composite_chart(iocs_df, vulns_df, pcaps_df)
    generate_network_chart(pcaps_df)
    generate_vulnerability_chart(vulns_df)

    block = f"""
{START}

# Enterprise Security Intelligence Dashboard
**Last Updated (UTC):** {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}

---

## Threat Intelligence Overview
{table(iocs_df)}

---

## Vulnerability Exposure Analysis
{table(vulns_df)}

---

## Enterprise Threat Posture
![Composite Threat](build/charts/composite_threat.png)

---

## Network Behavioral Risk Index
![Network Behavior](build/charts/network_behavior.png)

---

## Vulnerability Severity Distribution
![Vulnerability Distribution](build/charts/vulnerability_distribution.png)

{END}
"""

    text = README.read_text() if README.exists() else ""

    if START in text and END in text:
        text = text.split(START)[0] + block + text.split(END)[1]
    else:
        text += "\n" + block

    README.write_text(text)

    print("README fully updated with dynamic dashboards.")


if __name__ == "__main__":
    update_readme()
