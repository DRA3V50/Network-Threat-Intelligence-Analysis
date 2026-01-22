from pathlib import Path
from datetime import datetime
import pandas as pd

# ----------------------------
# CONFIG
# ----------------------------
README_PATH = Path("README.md")

# CSV paths
IOCS_CSV = Path("build/iocs/osint_iocs.csv")
VULNS_CSV = Path("build/vulnerabilities/vuln_scan_sample.csv")

# Chart path
CHART_PATH = Path("outputs/charts/top_source_ips.png")

# Auto-section markers
MARKER_START = "<!-- AUTO-GENERATED-SECTION:START -->"
MARKER_END = "<!-- AUTO-GENERATED-SECTION:END -->"

# How many rows to show in summary tables
TOP_N = 10

# ----------------------------
# HELPER FUNCTIONS
# ----------------------------
def read_csv_preview(csv_path, top_n=TOP_N):
    """Read CSV and return top_n rows as markdown table."""
    if not csv_path.exists():
        return f"*CSV not found: {csv_path.name}*"
    try:
        df = pd.read_csv(csv_path)
        if df.empty:
            return f"*No data in {csv_path.name}*"
        df_preview = df.head(top_n)
        return df_preview.to_markdown(index=False)
    except Exception as e:
        return f"*Error reading {csv_path.name}: {e}*"


def generate_auto_section():
    """Generate the markdown content for the auto-updated section."""
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    iocs_table = read_csv_preview(IOCS_CSV)
    vulns_table = read_csv_preview(VULNS_CSV)

    section = f"""
{MARKER_START}

### **Daily Automated Threat Intelligence Update**

**Timestamp (UTC):** {timestamp}

#### Top High-Risk Vulnerabilities
{vulns_table}

#### Top OSINT IOCs
{iocs_table}

#### Network Activity Chart
![Top Source IPs Chart]({CHART_PATH})

*This summary is auto-generated.*

{MARKER_END}
"""
    return section


def update_readme():
    """Replace the auto-generated section in README."""
    if not README_PATH.exists():
        print(f"[!] README.md not found at {README_PATH}")
        return

    readme_text = README_PATH.read_text(encoding="utf-8")

    # Ensure markers exist
    if MARKER_START not in readme_text or MARKER_END not in readme_text:
        print("[!] Auto-section markers not found in README, inserting them at end.")
        readme_text += f"\n{MARKER_START}\n{MARKER_END}\n"

    # Split and replace
    before, remainder = readme_text.split(MARKER_START, 1)
    _, after = remainder.split(MARKER_END, 1)

    new_section = generate_auto_section()

    updated_text = before + new_section + after
    README_PATH.write_text(updated_text, encoding="utf-8")
    print("[+] README.md updated successfully.")


if __name__ == "__main__":
    update_readme()
