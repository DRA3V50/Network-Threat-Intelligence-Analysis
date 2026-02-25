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

COMPOSITE_CHART = CHART_DIR / "composite_threat.png"
PROTOCOL_CHART = CHART_DIR / "protocol_distribution.png"

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

    vulns_df["risk_score"] = 0
    return vulns_df


# ---------------------------
# Chart Generation
# ---------------------------
def generate_weighted_threat_chart(iocs_df, vulns_df, pcaps_df):

    iocs_df.columns = iocs_df.columns.str.lower()
    vulns_df.columns = vulns_df.columns.str.lower()
    pcaps_df.columns = pcaps_df.columns.str.lower()

    ioc_score = float(iocs_df["confidence"].mean()) if "confidence" in iocs_df.columns else 0
    vuln_score = float(vulns_df["risk_score"].mean()) if "risk_score" in vulns_df.columns else 0
    net_score = float(pcaps_df["count"].sum()) if "count" in pcaps_df.columns else 0

    net_score = min(net_score * 2, 100)

    ioc_weighted = round(ioc_score * 0.90, 1)
    vuln_weighted = round(vuln_score * 0.05, 1)
    net_weighted = round(net_score * 0.05, 1)

    values = [ioc_weighted, vuln_weighted, net_weighted]
    max_val = max(values) if max(values) > 0 else 10
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

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#0B1118")
    ax.set_facecolor("#0B1118")

    labels = [
        "Threat Intelligence",
        "Vulnerability Exposure",
        "Network Activity"
    ]

    bars = ax.bar(labels, values, width=0.42)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + (max_val * 0.03),
            f"{height:.1f}",
            ha="center",
            va="bottom"
        )

    fig.text(
        0.5,
        0.92,
        f"Risk Tier: {risk_tier} | Composite Score: {composite_score}",
        ha="center",
        fontsize=12,
        color=tier_color,
        fontweight="bold"
    )

    ax.set_ylabel("Weighted Threat Contribution")
    ax.set_ylim(0, max_val * 1.15)

    plt.tight_layout(rect=[0, 0, 1, 0.88])
    plt.savefig(COMPOSITE_CHART, dpi=200)
    plt.close()


def generate_network_behavior_chart(pcaps_df):

    pcaps_df.columns = pcaps_df.columns.str.lower()

    if "count" not in pcaps_df.columns:
        return

    top = pcaps_df.head(6)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(top["source_ip"], top["count"])

    ax.set_title("Top Network Source IP Activity")
    ax.set_ylabel("Packet Count")
    ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.savefig(PROTOCOL_CHART, dpi=200)
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
    generate_network_behavior_chart(pcaps_df)

    block = f"""
{START}

## Operational Threat Intelligence Report
**Generated (UTC):** {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}

---

### High-Confidence Indicators of Compromise
{table(iocs_df)}

---

### Critical Vulnerability Exposure
{table(vulns_df)}

---

## Composite Threat Risk Assessment
![Composite Threat Risk](build/charts/composite_threat.png)

---

## Network Traffic Analysis
![Network Traffic Analysis](build/charts/protocol_distribution.png)

{END}
"""

    text = README.read_text() if README.exists() else ""

    if START in text and END in text:
        text = text.split(START)[0] + block + text.split(END)[1]
    else:
        text += "\n" + block

    README.write_text(text)

    print("✅ README successfully updated.")


if __name__ == "__main__":
    update_readme()
