from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(".")
README = ROOT / "README.md"

IOCS = ROOT / "build/iocs/osint_iocs.csv"
VULNS = ROOT / "build/vulnerabilities/vuln_scan_sample.csv"
PCAPS = ROOT / "build/pcaps/top_source_ips.csv"

CHART_DIR = ROOT / "build/charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)
CHART_PATH = CHART_DIR / "network_activity.png"

START = "<!-- AUTO-GENERATED-START -->"
END = "<!-- AUTO-GENERATED-END -->"


def table(df, limit=8):
    return df.head(limit).to_markdown(index=False)


# ---------------------------
# Vulnerability Risk Handling
# ---------------------------
def normalize_vulnerabilities(vulns_df):
    vulns_df.columns = vulns_df.columns.str.lower()

    if "risk_score" in vulns_df.columns:
        return vulns_df

    if "severity" in vulns_df.columns:
        severity_map = {
            "LOW": 25,
            "MEDIUM": 50,
            "HIGH": 75,
            "CRITICAL": 100
        }

        vulns_df["risk_score"] = (
            vulns_df["severity"]
            .astype(str)
            .str.upper()
            .map(severity_map)
            .fillna(0)
        )

        return vulns_df

    # fallback
    vulns_df["risk_score"] = 0
    return vulns_df


# ---------------------------
# Chart Generation
# ---------------------------
def generate_weighted_threat_chart(iocs_df, vulns_df, pcaps_df):

    ioc_score = iocs_df["confidence"].mean() if "confidence" in iocs_df.columns else 0
    vuln_score = vulns_df["risk_score"].mean() if "risk_score" in vulns_df.columns else 0
    net_score = pcaps_df["count"].sum() if "count" in pcaps_df.columns else 0

    net_score = min(net_score * 2, 100)

    ioc_weighted = round(ioc_score * 0.90, 1)
    vuln_weighted = round(vuln_score * 0.05, 1)
    net_weighted = round(net_score * 0.05, 1)

    labels = ["Threat Intelligence", "Vulnerability Exposure", "Network Activity"]
    values = [ioc_weighted, vuln_weighted, net_weighted]

    fig, ax = plt.subplots(figsize=(10, 5))

    # FBI-grade background
    fig.patch.set_facecolor("#0B1118")
    ax.set_facecolor("#0B1118")

    colors = ["#7A0C0C", "#8C5A0A", "#4B4F54"]

    bars = ax.bar(labels, values, width=0.45, color=colors)

    # Tight grid
    ax.yaxis.grid(True, linestyle="-", linewidth=0.6, color="#1F2A36")
    ax.set_axisbelow(True)

    # Precise numeric coordinates above bars
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1.2,
            f"{height:.1f}",
            ha="center",
            va="bottom",
            fontsize=11,
            color="#C9D1D9",
            fontweight="bold"
        )

    ax.set_title(
        "Composite Network Threat Posture",
        fontsize=14,
        color="#C9D1D9",
        pad=12,
        fontweight="bold"
    )

    ax.set_ylabel("Weighted Threat Contribution", color="#C9D1D9")

    ax.tick_params(colors="#C9D1D9")

    ax.set_ylim(0, max(values) + 10)

    plt.tight_layout()
    plt.savefig(CHART_PATH, dpi=200, facecolor=fig.get_facecolor())
    plt.close()


# ---------------------------
# README Update
# ---------------------------
def update_readme():

    print("🔥 update_readme.py EXECUTING 🔥")

    iocs_df = pd.read_csv(IOCS).sort_values("confidence", ascending=False)
    vulns_df = pd.read_csv(VULNS)
    pcaps_df = pd.read_csv(PCAPS).sort_values("count", ascending=False)

    vulns_df = normalize_vulnerabilities(vulns_df)
    vulns_df = vulns_df.sort_values("risk_score", ascending=False)

    generate_weighted_threat_chart(iocs_df, vulns_df, pcaps_df)

    block = f"""
{START}

## 📌 Daily Threat Intelligence Snapshot
**Generated (UTC):** {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}

### 🛰️ High-Confidence Threat Indicators
{table(iocs_df)}

### 🔥 Highest-Risk Vulnerabilities
{table(vulns_df)}

### 📊 Composite Network Threat Posture

![Network Threat Activity](build/charts/network_activity.png)

**Weighting Model**
- Threat Intelligence (IOCs): 90%
- Vulnerability Exposure: 5%
- Network Activity: 5%

{END}
"""

    text = README.read_text() if README.exists() else ""
    if START in text and END in text:
        text = text.split(START)[0] + block + text.split(END)[1]
    else:
        text += "\n" + block

    README.write_text(text)


if __name__ == "__main__":
    update_readme()
