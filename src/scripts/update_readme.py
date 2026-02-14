from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PATHS ----------------
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

# ---------------- HELPERS ----------------
def table(df, limit=8):
    return df.head(limit).to_markdown(index=False)


# ---------------- CHART ----------------
def generate_weighted_threat_chart(iocs_df, vulns_df, pcaps_df):
    """
    Generates a weighted threat dominance chart:
    - IOCs: 90%
    - Vulnerabilities: 5%
    - Network activity: 5%
    """

    # --- Aggregate values ---
    ioc_score = iocs_df["confidence"].mean()
    vuln_score = vulns_df["risk_score"].mean()
    net_score = pcaps_df["count"].sum()

    # Normalize
    net_score = min(net_score * 2, 100)

    weighted = {
        "Threat Intelligence (IOCs)": ioc_score * 0.90,
        "Vulnerability Exposure": vuln_score * 0.05,
        "Network Activity": net_score * 0.05,
    }

    labels = list(weighted.keys())
    values = list(weighted.values())

    # ---------------- STYLE ----------------
    plt.figure(figsize=(12, 6))
    plt.style.use("dark_background")

    bars = plt.bar(
        labels,
        values,
        width=0.55
    )

    # Clinical red / amber / muted white
    colors = ["#b11226", "#d98c1f", "#aaaaaa"]
    for bar, color in zip(bars, colors):
        bar.set_color(color)

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1,
            f"{height:.1f}",
            ha="center",
            va="bottom",
            fontsize=11
        )

    plt.title("Composite Network Threat Posture", fontsize=15, pad=14)
    plt.ylabel("Weighted Threat Contribution")
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.25)

    plt.tight_layout()
    plt.savefig(CHART_PATH, dpi=160)
    plt.close()


# ---------------- README ----------------
def update_readme():
    iocs_df = pd.read_csv(IOCS).sort_values("confidence", ascending=False)
    vulns_df = pd.read_csv(VULNS).sort_values("risk_score", ascending=False)
    pcaps_df = pd.read_csv(PCAPS).sort_values("count", ascending=False)

    generate_weighted_threat_chart(iocs_df, vulns_df, pcaps_df)

    block = f"""
{START}

## 📌 Daily Threat Intelligence Snapshot
**Generated (UTC):** {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}

### 🛰️ High-Confidence Threat Indicators
Top indicators prioritized by confidence and relevance.

{table(iocs_df)}

### 🔥 Highest-Risk Vulnerabilities
Vulnerabilities ranked by calculated operational risk.

{table(vulns_df)}

### 📊 Composite Network Threat Posture
Weighted threat dominance derived from intelligence correlation.

![Network Threat Activity](build/charts/network_activity.png)

**Weighting Model**
- Threat Intelligence (IOCs): **90%**
- Vulnerability Exposure: **5%**
- Network Activity: **5%**

{END}
"""

    text = README.read_text() if README.exists() else ""
    if START in text and END in text:
        text = text.split(START)[0] + block + text.split(END)[1]
    else:
        text += "\n" + block

    README.write_text(text)


if __name__ == "__main__":
    print("🔥 update_readme.py EXECUTING 🔥")
    update_readme()

