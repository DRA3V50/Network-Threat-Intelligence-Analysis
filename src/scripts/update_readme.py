import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generate_unified_network_chart(
    pcap_path="build/pcaps/top_source_ips.csv",
    ioc_path="build/iocs/osint_iocs.csv",
    vuln_path="build/vulnerabilities/vuln_scan_sample.csv",
    output_path="build/charts/network_activity.png"
):
    # -----------------------------
    # Load datasets
    # -----------------------------
    pcap_df = pd.read_csv(pcap_path)
    ioc_df = pd.read_csv(ioc_path)
    vuln_df = pd.read_csv(vuln_path)

    # -----------------------------
    # PCAP severity (activity-based)
    # -----------------------------
    pcap_df["pcap_score"] = pcap_df["count"]
    pcap_scores = pcap_df.set_index("source_ip")["pcap_score"]

    # -----------------------------
    # IOC severity (confidence-based)
    # -----------------------------
    ioc_df["ioc_score"] = ioc_df["confidence"] / 100.0
    ioc_score = ioc_df["ioc_score"].mean()

    # -----------------------------
    # Vulnerability severity
    # -----------------------------
    if "severity" in vuln_df.columns:
        severity_map = {"LOW": 1, "MEDIUM": 3, "HIGH": 6, "CRITICAL": 10}
        vuln_df["vuln_score"] = vuln_df["severity"].map(severity_map)
        vuln_score = vuln_df["vuln_score"].mean()
    else:
        vuln_score = 0

    # -----------------------------
    # Combine scores
    # -----------------------------
    combined_df = pd.DataFrame({
        "pcap_score": pcap_scores
    })

    combined_df["ioc_score"] = ioc_score
    combined_df["vuln_score"] = vuln_score

    # Weighted final severity
    combined_df["final_score"] = (
        combined_df["pcap_score"] * 0.4 +
        combined_df["ioc_score"] * 10 * 0.3 +
        combined_df["vuln_score"] * 0.3
    )

    combined_df = combined_df.sort_values("final_score", ascending=False)

    # -----------------------------
    # Plot
    # -----------------------------
    plt.figure(figsize=(14, 7))
    plt.bar(combined_df.index, combined_df["final_score"])
    plt.xticks(rotation=45, ha="right")

    plt.title("Unified Network Threat Severity")
    plt.xlabel("Source IP")
    plt.ylabel("Threat Severity Score")

    plt.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

    print(f"[+] Unified threat chart written to {output_path}")
