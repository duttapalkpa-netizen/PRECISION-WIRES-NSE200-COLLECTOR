#!/usr/bin/env python3
"""Bounded archive of the official BCEAO Côte d'Ivoire 2024 BOP report."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from hashlib import sha256
import json

URL = "https://www.bceao.int/sites/default/files/2026-09/Balance_des_Paiements_et_Position_Ext%C3%A9rieure_Globale_2024-C%C3%B4te_d-Ivoire.pdf"
OUT = Path("bceao_civ_2024_raw")
OUT.mkdir(parents=True, exist_ok=True)
req = Request(URL, headers={"User-Agent":"PRECISION-WIRES-GCR-evidence-archive/1.0","Accept":"application/pdf,*/*"})
retrieved = datetime.now(timezone.utc).isoformat()
with urlopen(req, timeout=35) as response:
    status = response.status
    headers = dict(response.headers.items())
    raw = response.read(25_000_001)
if len(raw) > 25_000_000:
    raise SystemExit("PDF exceeded 25 MB safety cap")
if status != 200 or not raw.startswith(b"%PDF-"):
    raise SystemExit(f"Unexpected response: status={status}, bytes={len(raw)}, prefix={raw[:16]!r}")
name = "Cote_dIvoire_BOP_2024.pdf"
(OUT/name).write_bytes(raw)
manifest = {
 "source_url": URL, "retrieved_at_utc": retrieved, "http_status": status,
 "content_type": headers.get("Content-Type"), "content_length_header": headers.get("Content-Length"),
 "byte_count": len(raw), "sha256": sha256(raw).hexdigest(),
 "pdf_magic": raw[:8].decode("ascii", errors="replace"), "archive_file": name,
 "purpose": "Check whether 2024 national report exposes separate net acquisition of financial assets and net incurrence of liabilities",
 "limitations": ["No IMF series mapping is performed by this acquisition-only script"]
}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(manifest,indent=2,ensure_ascii=False))
