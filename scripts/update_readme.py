"""
Updates README.md with the latest automated analysis snapshot
"""

from datetime import datetime
from pathlib import Path

README_PATH = Path("README.md")

def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    snapshot = f"""
## 📊 Daily Analysis Snapshot

> This section is automatically updated by GitHub Actions.

### **Daily Automated Threat Intelligence Update**

- **Last run:** {timestamp}
- **OSINT IOCs:** Generated
- **PCAP traffic:** Generated
- **Vulnerabilities:** Generated
- **Charts:** Generated

![Top Source IPs](outputs/charts/top_source_ips.png)

---
"""

    content = README_PATH.read_text(encoding="utf-8")

    marker = "## 📊 Daily Analysis Snapshot"
    if marker in content:
        content = content.split(marker)[0].rstrip()

    content = content + "\n\n" + snapshot
    README_PATH.write_text(content, encoding="utf-8")

    print("[+] README updated")

if __name__ == "__main__":
    main()
