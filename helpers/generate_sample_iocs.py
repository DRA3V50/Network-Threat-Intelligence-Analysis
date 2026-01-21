import csv
import os

os.makedirs("build/iocs", exist_ok=True)

with open("build/iocs/osint_iocs.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["IOC", "Type"])
    writer.writeheader()
    writer.writerow({"IOC": "1.2.3.4", "Type": "IP"})

print("[+] Sample IOC CSV generated in build/iocs/osint_iocs.csv")
