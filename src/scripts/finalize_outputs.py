import pandas as pd
from pathlib import Path
from src.analysis.charting import generate_top_source_ips_chart

BUILD_DIR = Path("build")
CHARTS_DIR = Path("outputs/charts")

CHARTS_DIR.mkdir(parents=True, exist_ok=True)


def trim_csv(csv_path: Path, sort_col: str, limit: int = 7):
    if not csv_path.exists():
        print(f"[!] Missing file: {csv_path}")
        return

    df = pd.read_csv(csv_path)

    if sort_col in df.columns:
        df = df.sort_values(sort_col, ascending=False)

    df.head(limit).to_csv(csv_path, index=False)


def finalize_outputs():
    # Trim OSINT
    trim_csv(
        BUILD_DIR / "iocs/osint_iocs.csv",
        sort_col="confidence"
    )

    # Trim Vulnerabilities
    trim_csv(
        BUILD_DIR / "vulnerabilities/vuln_scan_sample.csv",
        sort_col="risk_score"
    )

    # Trim PCAP + generate chart
    pcap_csv = BUILD_DIR / "pcaps/top_source_ips.csv"
    trim_csv(pcap_csv, sort_col="count")

    generate_top_source_ips_chart(
        csv_path=pcap_csv,
        output_path=CHARTS_DIR / "top_source_ips.png"
    )

    print("[+] Final outputs trimmed and chart generated")


if __name__ == "__main__":
    finalize_outputs()
