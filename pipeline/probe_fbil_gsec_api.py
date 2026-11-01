#!/usr/bin/env python3
"""Read-only probe of FBIL's first-party GSEC data API; never bypasses auth."""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path
import requests

BASE = "https://www.fbil.org.in/wasdm"
OUT = Path("artifacts/fbil_10y_provenance")
FROM_DATE = "2026-10-01"
TO_DATE = "2026-11-01"

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    observed = datetime.now(timezone.utc).isoformat()
    url = BASE + "/gsec/fetchfiltered"
    params = {"fromDate": FROM_DATE, "toDate": TO_DATE, "authenticated": "false"}
    response = requests.get(url, params=params, headers={
        "User-Agent": "Mozilla/5.0 (compatible; PRECISION-WIRES provenance audit)",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.fbil.org.in/"
    }, timeout=(10, 45))
    raw = response.content
    (OUT / "fbil_gsec_api_response.bin").write_bytes(raw)
    report = {
        "endpoint": url, "request_params": params, "final_url": response.url,
        "http_status": response.status_code, "content_type": response.headers.get("Content-Type"),
        "response_bytes": len(raw), "response_sha256": hashlib.sha256(raw).hexdigest(),
        "observed_at_utc": observed, "authentication_parameter": "false",
        "auth_bypass_attempted": False
    }
    try:
        payload = response.json()
        report["json_type"] = type(payload).__name__
        if isinstance(payload, dict):
            report["top_level_keys"] = sorted(payload.keys())
            data = next((payload[k] for k in ("data", "result", "records", "content") if isinstance(payload.get(k), list)), None)
        elif isinstance(payload, list):
            data = payload
        else:
            data = None
        report["record_count"] = len(data) if isinstance(data, list) else None
        report["sample_record_keys"] = sorted(data[0].keys()) if data and isinstance(data[0], dict) else []
        report["sample_records"] = data[:3] if isinstance(data, list) else None
        report["response_preview"] = None
    except ValueError:
        report["json_type"] = "non_json"
        report["record_count"] = None
        report["response_preview"] = raw[:1200].decode("utf-8", "replace")
    (OUT / "fbil_gsec_api_probe.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if response.status_code >= 400:
        raise RuntimeError(f"FBIL GSEC API returned HTTP {response.status_code}; raw response retained")
    if report.get("record_count") is None:
        raise RuntimeError("FBIL GSEC API response is not a recognized JSON record collection; diagnostics retained")

if __name__ == "__main__":
    main()
