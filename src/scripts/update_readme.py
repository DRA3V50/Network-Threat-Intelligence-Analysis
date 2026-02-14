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
    
   #---------------------------

def correlate_sources(iocs_df, vulns_df, pcaps_df):

    # Normalize column names
    iocs_df.columns = iocs_df.columns.str.lower()
    vulns_df.columns = vulns_df.columns.str.lower()
    pcaps_df.columns = pcaps_df.columns.str.lower()

    correlated = []

    # Ensure required columns exist
    if "ip" not in iocs_df.columns:
        return pd.DataFrame()

    if "source_ip" not in pcaps_df.columns:
        return pd.DataFrame()

    # Merge IOC IPs with network source IPs
    merged = pcaps_df.merge(
        iocs_df,
        left_on="source_ip",
        right_on="ip",
        how="inner"
    )

    if merged.empty:
        return pd.DataFrame()

    # Calculate amplified risk score
    merged["correlated_risk"] = (
        merged.get("confidence", 0) * 0.7 +
        merged.get("count", 0) * 0.3
    )

    merged = merged.sort_values("correlated_risk", ascending=False)

    return merged[[
        "source_ip",
        "confidence",
        "count",
        "correlated_risk"
    ]]


# ---------------------------
# Chart Generation
# ---------------------------
# ---------------------------
# Chart Generation
# ---------------------------
def generate_weighted_threat_chart(iocs_df, vulns_df, pcaps_df):

    # Normalize column names
    iocs_df.columns = iocs_df.columns.str.lower()
    vulns_df.columns = vulns_df.columns.str.lower()
    pcaps_df.columns = pcaps_df.columns.str.lower()

    # ---------------------------
    # Safe metric extraction
    # ---------------------------
    ioc_score = (
        float(iocs_df["confidence"].mean())
        if "confidence" in iocs_df.columns and not iocs_df.empty
        else 0
    )

    vuln_score = (
        float(vulns_df["risk_score"].mean())
        if "risk_score" in vulns_df.columns and not vulns_df.empty
        else 0
    )

    net_score = (
        float(pcaps_df["count"].sum())
        if "count" in pcaps_df.columns and not pcaps_df.empty
        else 0
    )

    # Normalize network contribution
    net_score = min(net_score * 2, 100)

    # ---------------------------
    # Correlation boost (IOC seen in traffic)
    # ---------------------------
    correlation_boost = 0
    if "ip" in iocs_df.columns and "source_ip" in pcaps_df.columns:
        merged = pcaps_df.merge(
            iocs_df,
            left_on="source_ip",
            right_on="ip",
            how="inner"
        )

        if not merged.empty and "confidence" in merged.columns:
            correlation_boost = min(
                float(merged["confidence"].mean()) * 0.25,
                20
            )

    # ---------------------------
    # Weighted calculation
    # ---------------------------
    ioc_weighted = round((ioc_score * 0.90) + correlation_boost, 1)
    vuln_weighted = round(vuln_score * 0.05, 1)
    net_weighted = round(net_score * 0.05, 1)

    values = [ioc_weighted, vuln_weighted, net_weighted]

    # Prevent flat chart
    max_val = max(values) if max(values) > 0 else 10

    # ---------------------------
    # Composite Risk Score
    # ---------------------------
    composite_score = round(sum(values), 1)

    if composite_score < 25:
        risk_tier = "LOW"
        tier_color = "#2E8B57"
    elif composite_score < 50:
        risk_tier = "MODERATE"
        tier_color = "#C47A1F"
    elif composite_score < 75:
        risk_tier = "HIGH"
        tier_color = "#B22222"
    else:
        risk_tier = "CRITICAL"
        tier_color = "#FF2E2E"

    # ---------------------------
    # Plot styling
    # ---------------------------
    fig, ax = plt.subplots(figsize=(10, 5))

    fig.patch.set_facecolor("#0B1118")
    ax.set_facecolor("#0B1118")

    labels = [
        "Threat Intelligence",
        "Vulnerability Exposure",
        "Network Activity"
    ]

    colors = ["#7A0C0C", "#8C5A0A", "#4B4F54"]

    bars = ax.bar(
        labels,
        values,
        width=0.42,
        color=colors,
        edgecolor="#1F2A36",
        linewidth=1.1
    )

    # Subtle analyst grid
    ax.yaxis.grid(True, linestyle="-", linewidth=0.6, color="#1F2A36")
    ax.set_axisbelow(True)

    ax.tick_params(axis="y", colors="#C9D1D9")
    ax.tick_params(axis="x", colors="#C9D1D9")

    # Numeric coordinates above bars
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + (max_val * 0.03),
            f"{height:.1f}",
            ha="center",
            va="bottom",
            fontsize=11,
            color="#C9D1D9",
            fontweight="bold"
        )

    # Title
    ax.set_title(
        "Composite Network Threat Posture",
        fontsize=14,
        color="#C9D1D9",
        pad=20,
        fontweight="bold"
    )

    # Risk Tier Subtitle
    ax.text(
        0.5,
        1.04,
        f"Risk Tier: {risk_tier}  |  Composite Score: {composite_score}",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=12,
        color=tier_color,
        fontweight="bold"
    )

    ax.set_ylabel(
        "Weighted Threat Contribution",
        color="#C9D1D9"
    )

    ax.set_ylim(0, max_val * 1.15)

    plt.tight_layout()
    plt.savefig(
        CHART_PATH,
        dpi=200,
        facecolor=fig.get_facecolor()
    )
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
