#!/usr/bin/env python3
"""Read-only probe of FBIL's first-party GSEC index and published-file route."""
import hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
import requests

BASE = "https://www.fbil.org.in/wasdm"
OUT = Path("artifacts/fbil_10y_provenance")
FROM_DATE = "2026-10-01"
TO_DATE = "2026-11-01"

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    observed = datetime.now(timezone.utc).isoformat()
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; PRECISION-WIRES provenance audit)",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.fbil.org.in/"
    })
    url = BASE + "/gsec/fetchfiltered"
    params = {"fromDate": FROM_DATE, "toDate": TO_DATE, "authenticated": "false"}
    response = session.get(url, params=params, timeout=(10, 45))
    raw = response.content
    (OUT / "fbil_gsec_api_response.bin").write_bytes(raw)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list):
        raise RuntimeError("FBIL GSEC index response is not a JSON list")
    report = {
        "index_endpoint": url, "request_params": params, "final_url": response.url,
        "http_status": response.status_code, "content_type": response.headers.get("Content-Type"),
        "response_bytes": len(raw), "response_sha256": hashlib.sha256(raw).hexdigest(),
        "observed_at_utc": observed, "authentication_parameter": "false",
        "auth_bypass_attempted": False, "index_record_count": len(payload),
        "index_sample": payload[:3], "published_file_probes": []
    }
    # Probe only the three newest archive dates; this is a read-only GET of the
    # first-party route explicitly called by the FBIL frontend.
    dates = []
    for item in payload:
        if isinstance(item, dict):
            value = str(item.get("processRunDate", ""))
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                dates.append(value)
    for day in sorted(set(dates), reverse=True)[:3]:
        download_url = BASE + "/gsec/downloadPublished"
        try:
            r = session.get(download_url, params={"date": day}, timeout=(10, 60))
            body = r.content
            safe_name = day.replace("-", "")
            path = OUT / f"fbil_gsec_published_{safe_name}.bin"
            path.write_bytes(body)
            report["published_file_probes"].append({
                "date": day, "url": r.url, "http_status": r.status_code,
                "content_type": r.headers.get("Content-Type"),
                "content_disposition": r.headers.get("Content-Disposition"),
                "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest(),
                "saved_file": path.name,
                "body_preview": body[:240].decode("utf-8", "replace")
                    if "text" in (r.headers.get("Content-Type") or "").lower()
                    or "json" in (r.headers.get("Content-Type") or "").lower()
                    else None
            })
        except requests.RequestException as exc:
            report["published_file_probes"].append({"date": day, "error": str(exc)})
    (OUT / "fbil_gsec_api_probe.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not payload:
        raise RuntimeError("FBIL GSEC index returned no archive records")
    if not report["published_file_probes"]:
        raise RuntimeError("No dated FBIL published-file route was probed")

if __name__ == "__main__":
    main()
