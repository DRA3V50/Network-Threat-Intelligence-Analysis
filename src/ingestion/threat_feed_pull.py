import csv
import os

FEED_URL = "https://example.com/iocs.csv"  # placeholder

def pull_osint_iocs(output_path="build/iocs/osint_iocs.csv"):
    """
    Pulls OSINT IOCs and saves to a CSV.
    Creates build/iocs folder if missing.
    Returns list of IOCs.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # For demo: generate a sample IOC
    iocs = [{"IOC": "1.2.3.4", "Type": "IP"}]

    # Save to CSV
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["IOC", "Type"])
        writer.writeheader()
        writer.writerows(iocs)

    print(f"[+] OSINT IOCs saved to {output_path}")
    return iocs
