#!/usr/bin/env python3
"""Capture the official BCB monthly Balance of Payments historical ZIP; research-only."""
from __future__ import annotations
import hashlib, json, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from zipfile import ZipFile

URL = "https://www.bcb.gov.br/ftp/notaecon/balpagm.zip"
OUT = Path("bcb_monthly_bop_history")
OUT.mkdir(parents=True, exist_ok=True)
started = datetime.now(timezone.utc).isoformat()
last = None
for attempt in range(3):
    try:
        req = Request(URL, headers={"User-Agent":"PRECISION-WIRES-BCB-history-audit/1.0","Accept":"application/zip, application/octet-stream, */*"})
        with urlopen(req, timeout=120) as response:
            payload = response.read()
            status = response.status
            headers = {k.lower():v for k,v in response.headers.items()}
            final_url = response.geturl()
        if status != 200 or not payload:
            raise RuntimeError(f"unexpected HTTP status/empty body: {status}/{len(payload)}")
        if not payload.startswith(b"PK"):
            raise RuntimeError("response is not a ZIP signature")
        path = OUT / "balpagm.zip"
        path.write_bytes(payload)
        with ZipFile(path) as zf:
            bad = zf.testzip()
            if bad:
                raise RuntimeError(f"ZIP CRC failure: {bad}")
            members = [{"name":x.filename,"size":x.file_size,"compressed_size":x.compress_size} for x in zf.infolist()]
        manifest = {
            "schema_version":1,"purpose":"research_only_independent_bcb_bop_history_capture",
            "source_url":URL,"final_url":final_url,"retrieval_started_at_utc":started,
            "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
            "http_status":status,"response_headers":headers,
            "byte_length":len(payload),"sha256":hashlib.sha256(payload).hexdigest(),
            "zip_crc_test":"PASS","member_count":len(members),"members":members,
            "content_use":"INDEPENDENT_CROSSCHECK_CANDIDATE_ONLY",
            "series_mapping":"NOT_DONE","date_value_reconciliation":"NOT_DONE",
            "accounting_sign_acceptance":"NOT_DONE","production_integration":"NOT_AUTHORIZED",
            "errors":[]
        }
        (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
        print(json.dumps(manifest,indent=2,sort_keys=True))
        sys.exit(0)
    except (HTTPError,URLError,TimeoutError,OSError,RuntimeError) as exc:
        last=repr(exc)
        if attempt<2: time.sleep(attempt+1)
manifest={"schema_version":1,"purpose":"research_only_independent_bcb_bop_history_capture","source_url":URL,"retrieval_started_at_utc":started,"status":"BLOCKED","errors":[last]}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
print(json.dumps(manifest,indent=2,sort_keys=True))
sys.exit(1)
