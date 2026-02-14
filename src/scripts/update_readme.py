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

    # Normalize network contribution
    net_score = min(net_score * 2, 100)

    # Apply weights
    ioc_weighted = ioc_score * 0.90
    vuln_weighted = vuln_score * 0.05
    net_weighted = net_score * 0.05

    values = [ioc_weighted, vuln_weighted, net_weighted]
    labels = ["Threat Intelligence", "Vulnerabilities", "Network Activity"]
    colors = ["#b11226", "#d98c1f", "#888888"]

    plt.figure(figsize=(12, 3))
    plt.style.use("dark_background")

    left = 0
    for value, color, label in zip(values, colors, labels):
        plt.barh(
            y=0,
            width=value,
            left=left,
            color=color,
            height=0.6,
            label=f"{label} ({value:.1f})"
        )
        left += value

    plt.xlim(0, 100)
    plt.yticks([])
    plt.xlabel("Composite Threat Contribution (Weighted)")
    plt.title("Composite Network Threat Posture", pad=10)

    plt.legend(loc="upper right", frameon=False)

    plt.tight_layout()
    plt.savefig(CHART_PATH, dpi=160)
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
