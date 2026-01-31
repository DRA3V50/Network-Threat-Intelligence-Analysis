import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generate_unified_network_chart(
    iocs_csv: str,
    vulns_csv: str,
    pcaps_csv: str,
    output_path: str,
    max_rows: int = 15
):
    """
    Generates a comprehensive network activity chart combining:
    - Top IOCs (high confidence)
    - Vulnerabilities (highest risk)
    - Top source IPs
    """
    iocs_csv = Path(iocs_csv)
    vulns_csv = Path(vulns_csv)
    pcaps_csv = Path(pcaps_csv)
    output_path = Path(output_path)

    plt.style.use("dark_background")
    plt.rcParams.update({
        "figure.figsize": (14, 6),
        "axes.facecolor": "#0b0b0b",
        "figure.facecolor": "#0b0b0b",
        "axes.edgecolor": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "text.color": "white",
    })

    fig, ax = plt.subplots()

    # Top Source IPs
    if pcaps_csv.exists():
        df_pcaps = pd.read_csv(pcaps_csv)
        df_pcaps["count"] = pd.to_numeric(df_pcaps.get("count", 1), errors="coerce").fillna(1)
        df_pcaps = df_pcaps.groupby("source_ip", as_index=False)["count"].sum()
        df_pcaps = df_pcaps.sort_values("count", ascending=False).head(max_rows)
        ax.bar(df_pcaps["source_ip"], df_pcaps["count"],
               color="#b30000", edgecolor="white", label="Top Source IPs")

    # Vulnerabilities
    if vulns_csv.exists():
        df_vulns = pd.read_csv(vulns_csv)
        if "risk_score" in df_vulns.columns:
            df_vulns["risk_score"] = pd.to_numeric(df_vulns["risk_score"], errors="coerce").fillna(0)
            df_vulns = df_vulns.sort_values("risk_score", ascending=False).head(max_rows)
            ax.bar(df_vulns["vuln_id"], df_vulns["risk_score"],
                   color="#ff4500", edgecolor="white", alpha=0.7, label="Top Vulnerabilities")

    # IOCs
    if iocs_csv.exists():
        df_iocs = pd.read_csv(iocs_csv)
        if "confidence" in df_iocs.columns:
            df_iocs["confidence"] = pd.to_numeric(df_iocs["confidence"], errors="coerce").fillna(0)
            df_iocs = df_iocs.sort_values("confidence", ascending=False).head(max_rows)
            ax.bar(df_iocs["ioc_value"], df_iocs["confidence"],
                   color="#ff6666", edgecolor="white", alpha=0.6, label="High-Confidence IOCs")

    ax.set_title("Comprehensive Network Threat Activity Overview", fontsize=14)
    ax.set_ylabel("Event Count / Severity / Confidence")
    plt.xticks(rotation=45, ha="right", fontsize=8)
    ax.legend()
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=140)
    plt.close()
    print(f"[+] Unified network chart written to {output_path}")

