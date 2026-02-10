import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generate_threat_chart():
    base = Path("outputs")

    pcap_path = base / "pcap_summary.csv"
    ioc_path  = base / "ioc_summary.csv"
    vuln_path = base / "vuln_summary.csv"
    chart_out = base / "network_threat_chart.png"

    # -----------------------
    # Load tables
    # -----------------------
    pcap = pd.read_csv(pcap_path)
    ioc  = pd.read_csv(ioc_path)
    vuln = pd.read_csv(vuln_path)

    pcap.columns = pcap.columns.str.lower()
    ioc.columns  = ioc.columns.str.lower()
    vuln.columns = vuln.columns.str.lower()

    # -----------------------
    # Base per-IP frame
    # -----------------------
    df = pcap.rename(columns={"source_ip": "ip"})
    df["A_pcap"] = df["count"]

    # -----------------------
    # IOC score per IP
    # -----------------------
    if "indicator" in ioc.columns:
        ioc_ip = (
            ioc.groupby("indicator")["confidence"]
            .max()
            .reset_index()
            .rename(columns={"indicator": "ip", "confidence": "B_ioc"})
        )
        df = df.merge(ioc_ip, on="ip", how="left")
    else:
        df["B_ioc"] = 0

    df["B_ioc"] = df["B_ioc"].fillna(0)

    # -----------------------
    # Vuln score per IP
    # -----------------------
    severity_weight = {
        "LOW": 1,
        "MEDIUM": 3,
        "HIGH": 6,
        "CRITICAL": 10
    }

    if "host" in vuln.columns:
        vuln["sev"] = vuln["severity"].map(severity_weight)
        vuln_ip = (
            vuln.groupby("host")["sev"]
            .max()
            .reset_index()
            .rename(columns={"host": "ip", "sev": "C_vuln"})
        )
        df = df.merge(vuln_ip, on="ip", how="left")
    else:
        df["C_vuln"] = 0

    df["C_vuln"] = df["C_vuln"].fillna(0)

    # -----------------------
    # FINAL WEIGHTED SCORE
    # A = 90%
    # B = 5%
    # C = 5%
    # -----------------------
    df["final_score"] = (
        df["A_pcap"] * 0.90 +
        df["B_ioc"]  * 0.05 +
        df["C_vuln"] * 0.05
    )

    df = df.sort_values("final_score", ascending=False)

    # -----------------------
    # Chart (clean, readable)
    # -----------------------
    plt.figure(figsize=(14, 6))
    plt.bar(df["ip"], df["final_score"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Network Threat Severity (A=90%, B=5%, C=5%)")
    plt.xlabel("Source IP")
    plt.ylabel("Weighted Threat Score")
    plt.tight_layout()

    chart_out.parent.mkdir(exist_ok=True)
    plt.savefig(chart_out)
    plt.close()

    print("[+] Threat chart regenerated from tables")
