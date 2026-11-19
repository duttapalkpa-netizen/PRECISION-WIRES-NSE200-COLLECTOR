#!/usr/bin/env python3
"""Bounded raw-byte archive of three official BCEAO 2024 national BOP reports."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from hashlib import sha256
import json, time

SOURCES = {
 "BEN": "https://www.bceao.int/sites/default/files/2026-09/Balance%20des%20Paiements%20et%20Position%20Ext%C3%A9rieure%20Globale%202024%20-%20B%C3%A9nin.pdf",
 "BFA": "https://www.bceao.int/sites/default/files/2026-09/Balance%20des%20Paiements%20et%20Position%20Ext%C3%A9rieure%20Globale%202024%20-%20Burkina.pdf",
 "SEN": "https://www.bceao.int/sites/default/files/2026-09/Balance%20des%20Paiements%20et%20Position%20Ext%C3%A9rieure%20Globale%202024%20-%20S%C3%A9n%C3%A9gal.pdf",
}
ROOT=Path("bceao_three_country_2024_raw"); ROOT.mkdir(parents=True,exist_ok=True)
receipts=[]
for code,url in SOURCES.items():
    started=datetime.now(timezone.utc).isoformat()
    req=Request(url,headers={"User-Agent":"PRECISION-WIRES-GCR-evidence-archive/1.0","Accept":"application/pdf,*/*"})
    try:
        with urlopen(req,timeout=30) as r:
            status=r.status; headers=dict(r.headers.items()); raw=r.read(20_000_001)
        if len(raw)>20_000_000: raise ValueError("PDF exceeds 20MB safety cap")
        if status!=200 or not raw.startswith(b"%PDF-"): raise ValueError(f"unexpected response status={status}, bytes={len(raw)}, prefix={raw[:16]!r}")
        name=f"{code}_BOP_2024.pdf"; (ROOT/name).write_bytes(raw)
        receipts.append({"country_code":code,"source_url":url,"retrieved_at_utc":started,"http_status":status,"content_type":headers.get("Content-Type"),"content_length_header":headers.get("Content-Length"),"byte_count":len(raw),"sha256":sha256(raw).hexdigest(),"pdf_magic":raw[:8].decode("ascii",errors="replace"),"archive_file":name,"status":"ARCHIVED"})
    except Exception as e:
        receipts.append({"country_code":code,"source_url":url,"retrieved_at_utc":started,"status":"FAILED","error":repr(e)})
    time.sleep(1)
manifest={"scope":"BCEAO 2024 national BOP reports BEN/BFA/SEN; source-byte capture only","retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"sources":receipts}
(ROOT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(manifest,indent=2,ensure_ascii=False))
if not all(x["status"]=="ARCHIVED" for x in receipts): raise SystemExit("One or more official report downloads failed; inspect manifest.")
