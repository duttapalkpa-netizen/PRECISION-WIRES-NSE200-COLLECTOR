#!/usr/bin/env python3
"""Read-only raw capture of official India FPI source landing pages.
No POSTs, credentials, inferred records, or production ingestion.
"""
import hashlib, json, pathlib, time
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

OUT = pathlib.Path("outputs/gcr_india_fpi_raw_capture")
OUT.mkdir(parents=True, exist_ok=True)
SOURCES = {
    "nsdl_latest": "https://www.fpi.nsdl.co.in/web/Reports/Latest.aspx",
    "nsdl_monthly": "https://www.fpi.nsdl.co.in/web/Reports/Monthly.aspx",
    "nsdl_archive": "https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx",
    "nsdl_fortnightly_selector": "https://www.fpi.nsdl.co.in/web/Reports/FPI_Fortnightly_Selection.aspx",
    "cdsl_daily_latest_eservices": "https://www.cdslindia.com/eservices/publications/fiidaily",
    "cdsl_daily_archive": "https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx",
    "cdsl_fortnightly_sector": "https://www.cdslindia.com/Publications/ForeignPortInvestor.html",
}
manifest = {
    "capture_started_utc": datetime.now(timezone.utc).isoformat(),
    "method": "GET",
    "sources": [],
    "policy": "Raw page capture only; no form submission or data interpretation."
}
for name, url in SOURCES.items():
    row = {"name": name, "requested_url": url, "retrieved_at_utc": datetime.now(timezone.utc).isoformat()}
    req = Request(url, headers={"User-Agent": "PRECISION-WIRES-research-evidence/1.0", "Accept": "text/html,application/xhtml+xml,*/*"})
    try:
        with urlopen(req, timeout=25) as response:
            body = response.read()
            row.update({
                "http_status": response.status,
                "final_url": response.geturl(),
                "headers": dict(response.headers.items()),
                "content_type": response.headers.get("Content-Type"),
                "byte_count": len(body),
                "sha256": hashlib.sha256(body).hexdigest(),
            })
    except HTTPError as exc:
        body = exc.read()
        row.update({
            "http_status": exc.code, "final_url": exc.geturl(),
            "headers": dict(exc.headers.items()) if exc.headers else {},
            "content_type": exc.headers.get("Content-Type") if exc.headers else None,
            "byte_count": len(body), "sha256": hashlib.sha256(body).hexdigest(),
            "error": "HTTPError"
        })
    except (URLError, TimeoutError, OSError) as exc:
        body = b""
        row.update({"http_status": None, "byte_count": 0, "sha256": hashlib.sha256(body).hexdigest(),
                    "error": type(exc).__name__ + ": " + str(exc)[:500]})
    suffix = ".html" if body else ".empty"
    raw_path = OUT / (name + suffix)
    raw_path.write_bytes(body)
    row["raw_file"] = str(raw_path)
    manifest["sources"].append(row)
    print(json.dumps({"name": name, "status": row.get("http_status"), "bytes": row["byte_count"], "sha256": row["sha256"]}))
manifest["capture_finished_utc"] = datetime.now(timezone.utc).isoformat()
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
summary = {"sources": len(manifest["sources"]), "http_200": sum(x.get("http_status") == 200 for x in manifest["sources"]),
           "non_200_or_error": sum(x.get("http_status") != 200 for x in manifest["sources"]),
           "manifest": str(OUT / "manifest.json")}
(OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary))
