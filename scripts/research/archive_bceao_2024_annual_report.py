#!/usr/bin/env python3
"""Archive the official BCEAO 2024 Annual Report PDF and hash its exact bytes."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from hashlib import sha256
import json

URL = "https://cofeb.bceao.int/sites/default/files/2025-07/Rapport_Annuel_2024_BCEAO_INTERACTIF_compressed.pdf"
OUT = Path("bceao_2024_raw")
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
    raise SystemExit(f"Unexpected response: status={status}, bytes={len(raw)}, pdf_magic={raw[:8]!r}")
filename = "Rapport_Annuel_2024_BCEAO_INTERACTIF_compressed.pdf"
(OUT / filename).write_bytes(raw)
manifest = {
    "source_url": URL,
    "retrieved_at_utc": retrieved,
    "http_status": status,
    "content_type": headers.get("Content-Type") or headers.get("content-type"),
    "content_length_header": headers.get("Content-Length") or headers.get("content-length"),
    "byte_count": len(raw),
    "sha256": sha256(raw).hexdigest(),
    "pdf_magic": raw[:8].decode("ascii", errors="replace"),
    "archive_file": filename,
    "scope": "BCEAO Annual Report 2024, Annexes A23-A27, eight UEMOA national BOP tables",
    "limitations": ["2024 rows are marked estimates in the report", "net financial-account balances do not separately identify IMF A_NFA_T and L_NIL_T legs"]
}
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(manifest, indent=2, ensure_ascii=False))
