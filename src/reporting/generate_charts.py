import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = "outputs/charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_top_ip_chart():
    """
    Generates a simple top-source IP chart.
    """
    # Example: read matched_iocs.csv for charting
    data_file = "outputs/logs/matched_iocs.csv"
    if not os.path.exists(data_file):
        print("[!] No matched_iocs.csv found — skipping chart")
        return

    df = pd.read_csv(data_file)
    top_ips = df['IOC'].value_counts().head(10)

    plt.figure(figsize=(8,6))
    sns.barplot(x=top_ips.index, y=top_ips.values)
    plt.xticks(rotation=45)
    plt.ylabel("Count")
    plt.xlabel("Top Source IPs")
    plt.title("Top 10 Source IPs from IOCs")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "top_source_ips.png"))
    plt.close()
    print(f"[+] Chart generated at {OUTPUT_DIR}/top_source_ips.png")
