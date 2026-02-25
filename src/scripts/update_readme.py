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
PROTOCOL_CHART = CHART_DIR / "network_behavior.png"

START = "<!-- AUTO-GENERATED-START -->"
END = "<!-- AUTO-GENERATED-END -->"


# ---------------------------
# Utility
# ---------------------------
def table(df, limit=8):
    return df.head(limit).to_markdown(index=False)


def apply_soc_style(fig, ax):
    fig.patch.set_facecolor("#0B1118")
    ax.set_facecolor("#0B1118")

    ax.tick_params(colors="#C9D1D9")
    ax.yaxis.label.set_color("#C9D1D9")
    ax.xaxis.label.set_color("#C9D1D9")

    for spine in ax.spines.values():
        spine.set_color("#1F2A36")

    ax.yaxis.grid(True, linestyle="-", linewidth=0.6, color="#1F2A36")
    ax.set_axisbelow(True)


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

    else:
        vulns_df["risk_score"] = 0

    return vulns_df


# ---------------------------
# Composite Threat Chart
# ---------------------------
def generate_weighted_threat_chart(iocs_df, vulns_df, pcaps_df):

    iocs_df.columns = iocs_df.columns.str.lower()
    vulns_df.columns = vulns_df.columns.str.lower()
    pcaps_df.columns = pcaps_df.columns.str.lower()

    # --- Component Scores ---
    ioc_score = float(iocs_df["confidence"].mean()) if "confidence" in iocs_df.columns else 0
    vuln_score = float(vulns_df["risk_score"].mean()) if "risk_score" in vulns_df.columns else 0
    net_volume = float(pcaps_df["count"].sum()) if "count" in pcaps_df.columns else 0

    # Normalize network activity
    net_score = min(net_volume * 2, 100)

    # Weighted Model
    ioc_weighted = round(ioc_score * 0.85, 1)
    vuln_weighted = round(vuln_score * 0.10, 1)
    net_weighted = round(net_score * 0.05, 1)

    values = [ioc_weighted, vuln_weighted, net_weighted]
    labels = [
        "Threat Intelligence",
        "Vulnerability Exposure",
        "Network Behavior"
    ]

    composite_score = round(sum(values), 1)
    max_val = max(values) if max(values) > 0 else 10

    # Risk Tier Logic
    if composite_score < 25:
        risk_tier, tier_color = "LOW", "#2E8B57"
    elif composite_score < 50:
        risk_tier, tier_color = "MODERATE", "#C47A1F"
    elif composite_score < 75:
        risk_tier, tier_color = "HIGH", "#B22222"
    else:
        risk_tier, tier_color = "CRITICAL", "#FF2E2E"

    fig, ax = plt.subplots(figsize=(10, 5))
    apply_soc_style(fig, ax)

    colors = ["#9B111E", "#C47A1F", "#4B4F54"]
    bars = ax.bar(labels, values, width=0.45, color=colors)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + (max_val * 0.04),
            f"{height:.1f}",
            ha="center",
            color="#C9D1D9",
            fontweight="bold"
        )

    fig.text(
        0.5,
        0.92,
        f"Risk Tier: {risk_tier}  |  Composite Score: {composite_score}",
        ha="center",
        fontsize=13,
        color=tier_color,
        fontweight="bold"
    )

    ax.set_ylabel("Weighted Threat Contribution")
    ax.set_ylim(0, max_val * 1.15)

    plt.tight_layout(rect=[0, 0, 1, 0.88])
    plt.savefig(COMPOSITE_CHART, dpi=220, facecolor=fig.get_facecolor())
    plt.close()


# ---------------------------
# Network Behavior Chart (Upgraded)
# ---------------------------
def generate_network_behavior_chart(pcaps_df):

    pcaps_df.columns = pcaps_df.columns.str.lower()

    if "count" not in pcaps_df.columns or "source_ip" not in pcaps_df.columns:
        return

    top = pcaps_df.head(6).copy()

    # Behavioral weighting example
    suspicious_ports = [23, 21, 445, 3389]
    if "destination_port" in pcaps_df.columns:
        top["behavior_weight"] = top.apply(
            lambda x: x["count"] * 1.8 if x.get("destination_port") in suspicious_ports else x["count"],
            axis=1
        )
    else:
        top["behavior_weight"] = top["count"]

    fig, ax = plt.subplots(figsize=(10, 5))
    apply_soc_style(fig, ax)

    bars = ax.bar(top["source_ip"], top["behavior_weight"], width=0.45)

    max_val = top["behavior_weight"].max() if len(top) else 10

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + (max_val * 0.04),
            f"{int(height)}",
            ha="center",
            color="#C9D1D9",
            fontweight="bold"
        )

    ax.set_title("Network Behavioral Threat Indicators", color="#C9D1D9", pad=12)
    ax.set_ylabel("Behavioral Risk Weight")

    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.savefig(PROTOCOL_CHART, dpi=220, facecolor=fig.get_facecolor())
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

## Network Traffic Behavioral Analysis
![Network Behavior](build/charts/network_behavior.png)

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
