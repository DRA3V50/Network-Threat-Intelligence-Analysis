import os
import pandas as pd

def prioritize_vulns():
    vuln_file = "data/vulnerabilities/vuln_scan_sample.csv"
    os.makedirs(os.path.dirname(vuln_file), exist_ok=True)

    if not os.path.exists(vuln_file) or os.path.getsize(vuln_file) == 0:
        pd.DataFrame({
            "Host": ["192.168.1.100"],
            "Vulnerability": ["Sample Vulnerability"],
            "Severity": ["High"]
        }).to_csv(vuln_file, index=False)

    vulns = pd.read_csv(vuln_file)
    print(f"[+] Loaded {len(vulns)} vulnerabilities")

    output_file = "outputs/logs/prioritized_vulns.csv"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    vulns.to_csv(output_file, index=False)
    print(f"[+] Vulnerabilities prioritized and saved to {output_file}")
