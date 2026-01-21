"""
Updates README.md using outputs/logs/high_risk_vulns.csv
"""

from pathlib import Path
from datetime import datetime
import pandas as pd

README = Path("README.md")
CSV = Path("outputs/logs/high_risk_vulns.csv")

def csv_to_markdown(df):
    return df.to_markdown(index=False)

def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    if not CSV.exists():
        table = "_No vulnerability data generated yet._"
    else:
        df = pd.read_csv(CSV)
        table = csv_to_markdown(df.head(15))

    section = f"""
## 📊 Daily Analysis Snapshot

_Last automated run: **{timestamp}**_

### 🔥 High-Risk Vulnerabilities (Top 15)

{table}

---
"""

    content = README.read_text(encoding="utf-8") if README.exists() else ""

    marker = "## 📊 Daily Analysis Snapshot"
    if marker in content:
        content = content.split(marker)[0].rstrip()

    README.write_text(content + "\n\n" + section, encoding="utf-8")
    print("[+] README updated successfully")

if __name__ == "__main__":
    main()
