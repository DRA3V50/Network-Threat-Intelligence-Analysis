def correlate_iocs(traffic, iocs):
    """
    Correlates IOCs with captured traffic packets.
    Returns a list of matches.
    """
    matches = []

    # Example logic: check if any IOC IP is in packet summary
    for pkt in traffic:
        pkt_summary = str(pkt.summary())
        for ioc in iocs:
            if ioc["IOC"] in pkt_summary:
                matches.append(ioc["IOC"])

    print(f"[+] Correlated {len(matches)} IOC matches with traffic")
    return matches
