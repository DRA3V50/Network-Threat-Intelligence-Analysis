import pandas as pd


# Dynamic weighting model
WEIGHTS = {
    "ioc": 0.60,
    "vulnerability": 0.25,
    "network": 0.15
}


def calculate_scores(ioc_count, vuln_df, traffic_df):
    """
    Dynamically compute weighted threat posture
    """

    # IOC Score (scale based on count)
    ioc_score = min(ioc_count * 2, 100)

    # Vulnerability Exposure Score
    if vuln_df is not None and not vuln_df.empty:
        high = vuln_df[vuln_df["severity"] == "High"].shape[0]
        critical = vuln_df[vuln_df["severity"] == "Critical"].shape[0]
        vuln_score = min((high * 5 + critical * 10), 100)
    else:
        vuln_score = 0

    # Network Activity Score
    if traffic_df is not None and not traffic_df.empty:
        suspicious = traffic_df[traffic_df["flagged"] == True].shape[0]
        network_score = min(suspicious * 3, 100)
    else:
        network_score = 0

    composite_score = (
        ioc_score * WEIGHTS["ioc"] +
        vuln_score * WEIGHTS["vulnerability"] +
        network_score * WEIGHTS["network"]
    )

    return {
        "ioc_score": round(ioc_score, 2),
        "vuln_score": round(vuln_score, 2),
        "network_score": round(network_score, 2),
        "composite_score": round(composite_score, 2),
        "weights": WEIGHTS
    }
