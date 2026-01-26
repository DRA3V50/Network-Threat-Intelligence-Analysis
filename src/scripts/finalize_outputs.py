import pandas as pd
from pathlib import Path

# ---------------- CONFIG ---------------- #

BUILD_DIR = Path("build")

IOCS_CSV = BUILD_DIR / "iocs" / "osint_iocs.csv"
VULNS_CSV = BUILD_DIR / "vulnerabilities" / "vuln_scan_sample.csv"
TOP_IPS_CSV = BUILD_DIR / "top_source_ips.csv"

MIN_ROWS = 3
MAX_ROWS = 10

# ---------------------------------------- #


def trim_csv(
    csv_path: Path,
    sort_col: str,
    ascending: bool = False,
):
    """
    Sort + trim CSV IN PLACE so all downstream consumers match exactly.
    """
    if not csv_path.exists():
        print(f"[!] Missing file: {csv_path}")
        return

    df = pd.read_csv(csv_path)

    if df.empty:
        print(f"[!] Empty file: {csv_path}")
        return

    # Clamp row count
    target_rows = min(MAX_ROWS, max(MIN_ROWS, len(df)))

    # Sort by severity / confidence / count
    df = df.sort_values(sort_col, ascending=ascending).head(target_rows)

    # Overwrite same file (authoritative)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path, index=False)

    print(f"[✓] Finalized {csv_path} → {len(df)} rows")


def finalize_outputs():
    print("\n[+] Finalizing pipeline outputs...\n")

    # OSINT Indicators → highest confidence first
    trim_csv(
        csv_path=IOCS_CSV,
        sort_col="confidence",
        ascending=False
    )

    # Vulnerabilities → highest risk first
    trim_csv(
        csv_path=VULNS_CSV,
        sort_col="risk_score",
        ascending=False
    )

    # Network activity → highest traffic first
    trim_csv(
        csv_path=TOP_IPS_CSV,
        sort_col="count",
        ascending=False
    )

    print("\n[✓] All outputs finalized and aligned\n")


if __name__ == "__main__":
    finalize_outputs()
