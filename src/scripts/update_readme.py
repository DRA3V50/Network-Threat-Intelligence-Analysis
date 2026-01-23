from datetime import datetime
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Paths
BUILD_DIR = Path("build")
OUTPUT_DIR = Path("outputs")
CHARTS_DIR = OUTPUT_DIR / "charts"
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

# Max rows to display in README tables
MAX_TABLE_ROWS = 8

# Auto-generated section markers
SECTION_START = "<!-- AUTO-GENERATED-SECTION:START -->"
SECTION_END = "<!-- AUTO-GENERATED-SECTION:END -->"


def limit_rows(df: pd.DataFrame, max_rows=MAX_TABLE_ROWS):
    """Limit DataFrame rows for README display."""
    return df.head(max_rows)


def generate_chart(top_ips_csv: Path, chart_path: Path):
    """Generate dark Resident Evil style chart from top source IPs CSV."""
    df = pd.read_csv(top_ips_csv)

    # Try to auto-detect columns
    ip_col = None
    count_col = None
    for c in df.columns:
        if "ip" in c.lower():
            ip_col = c
        if "count" in c.lower() or "total" in c.lower():
            count_col = c

    if not ip_col or not count_col:
        print(f"[!] Could not find IP/count columns in {top_ips_csv}")
        return

    top = df.head(10)
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(top[ip_col], top[count_col], color="red", edgecolor="white")
    ax.set_title("Top Source IPs", color="white")
    ax.set_xlabel("IP Address", color="white")
    ax.set_ylabel("Count", color="white")
    ax.tick_params(colors="white")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    fig.savefig(chart_path, dpi=150)
    plt.close(fig)


def generate_markdown_table(df: pd.DataFrame, headers=None):
    """Generate markdown table string from DataFrame."""
    if headers is None:
        headers = df.columns.tolist()
    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join([":" + "-" * (len(h)) + ":" for h in headers]) + " |\n"
    for _, row in df.iterrows():
        table += "| " + " | ".join([str(row[h]) for h in headers]) + " |\n"
    return table


def main():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    readme_path = Path("README.md")

    # --- Load CSVs ---
    iocs_csv = BUILD_DIR / "iocs/osint_iocs.csv"
    vulns_csv = BUILD_DIR / "vulnerabilities/vuln_scan_sample.csv"
    top_ips_csv = BUILD_DIR / "pcaps/top_source_ips.csv"
    chart_file = CHARTS_DIR / "top_source_ips.png"

    # Limit table rows
    iocs_df = limit_rows(pd.read_csv(iocs_csv))
    vulns_df = limit_rows(pd.read_csv(vulns_csv))

    # Generate chart
    if top_ips_csv.exists():
        generate_chart(top_ips_csv, chart_file)

    # Generate markdown
    iocs_md = generate_markdown_table(iocs_df)
    vulns_md = generate_markdown_table(vulns_df)

    auto_generated_section = f"""
{SECTION_START}

### **Daily Automated Threat Intelligence Update**

📊 **Timestamp (UTC):** {timestamp}

#### 🧪 Top OSINT IOCs
{iocs_md}

#### 🔴 High-Risk Vulnerabilities
{vulns_md}

#### 📈 Network Activity Chart
{'![Top Source IPs Chart](outputs/charts/top_source_ips.png)' if chart_file.exists() else 'Chart not generated.'}

*This summary is auto-generated.*

{SECTION_END}
""".strip()

    # Read current README
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace auto-generated section
    if SECTION_START in content and SECTION_END in content:
        before = content.split(SECTION_START)[0]
        after = content.split(SECTION_END)[1]
        new_content = before + auto_generated_section + after
    else:
        # Append if no markers found
        new_content = content + "\n\n" + auto_generated_section

    # Write updated README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("[+] README.md updated successfully.")


if __name__ == "__main__":
    main()
