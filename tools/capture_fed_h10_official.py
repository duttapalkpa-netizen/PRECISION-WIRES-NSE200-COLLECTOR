#!/usr/bin/env python3
"""Capture the official Federal Reserve H.10 ZIP response with transport evidence."""
from __future__ import annotations
import hashlib, json, os, sys, urllib.request, urllib.error, zipfile
from datetime import datetime, timezone
from pathlib import Path

URL = "https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=H10"
OUT = Path(os.environ.get("OUTPUT_DIR", "fed_h10_capture"))
OUT.mkdir(parents=True, exist_ok=True)
started = datetime.now(timezone.utc)
request = urllib.request.Request(URL, headers={"User-Agent": "PRECISION-WIRES-research-evidence-capture/1.0", "Accept": "application/zip, application/octet-stream;q=0.9, */*;q=0.8"})
try:
    with urllib.request.urlopen(request, timeout=90) as response:
        retrieved = datetime.now(timezone.utc)
        status = response.status
        final_url = response.geturl()
        headers = {k.lower(): v for k, v in response.headers.items()}
        payload = response.read()
except Exception as exc:
    print(f"official H.10 download failed: {type(exc).__name__}: {exc}", file=sys.stderr)
    raise

if status != 200:
    raise SystemExit(f"unexpected HTTP status: {status}")
if not payload:
    raise SystemExit("empty H.10 response")
content_type = headers.get("content-type", "").split(";", 1)[0].strip().lower()
if "zip" not in content_type and not payload.startswith(b"PK\\x03\\x04"):
    raise SystemExit(f"response is not a ZIP payload: content-type={content_type!r}")
zip_path = OUT / "FRB_H10_official_response.zip"
zip_path.write_bytes(payload)
with zipfile.ZipFile(zip_path) as archive:
    bad_member = archive.testzip()
    if bad_member:
        raise SystemExit(f"ZIP integrity failure in member {bad_member}")
    members = [{"name": x.filename, "size_bytes": x.file_size, "compressed_size_bytes": x.compress_size} for x in archive.infolist()]
manifest = {
    "schema_version": 1,
    "evidence_type": "official_http_transport_capture",
    "publisher": "Board of Governors of the Federal Reserve System",
    "dataset": "G.5/H.10 - Foreign Exchange Rates",
    "requested_url": URL,
    "final_url": final_url,
    "request_started_at_utc": started.isoformat(),
    "retrieved_at_utc": retrieved.isoformat(),
    "http_status": status,
    "response_headers": headers,
    "content_type": content_type,
    "byte_length": len(payload),
    "sha256": hashlib.sha256(payload).hexdigest(),
    "raw_payload_path": zip_path.name,
    "zip_integrity_test": "PASS",
    "members": members,
    "github": {
        "repository": os.environ.get("GITHUB_REPOSITORY"),
        "commit_sha": os.environ.get("GITHUB_SHA"),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT")
    }
}
(OUT / "FRB_H10_official_response_manifest.json").write_text(json.dumps(manifest, indent=2) + "\\n", encoding="utf-8")
(OUT / "FRB_H10_official_response.sha256").write_text(f"{manifest['sha256']}  {zip_path.name}\\n", encoding="ascii")
print(json.dumps({k: manifest[k] for k in ("final_url","retrieved_at_utc","http_status","content_type","byte_length","sha256","zip_integrity_test")}, indent=2))
