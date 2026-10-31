#!/usr/bin/env python3
"""Fetch and preserve a public MoSPI IIP aggregate release page; no credentials."""
from __future__ import annotations
import argparse, hashlib, json, os, urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

URL = "https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2329475&lang=1&reg=3"

class Tables(HTMLParser):
    def __init__(self):
        super().__init__(); self.tables=[]; self.in_table=False; self.in_cell=False
        self.table=[]; self.row=[]; self.cell=[]
    def handle_starttag(self, tag, attrs):
        if tag=="table":
            self.in_table=True; self.table=[]
        elif self.in_table and tag=="tr": self.row=[]
        elif self.in_table and tag in ("td","th"):
            self.in_cell=True; self.cell=[]
    def handle_data(self, data):
        if self.in_table and self.in_cell: self.cell.append(data)
    def handle_endtag(self, tag):
        if self.in_table and tag in ("td","th") and self.in_cell:
            self.row.append(" ".join(" ".join(self.cell).split())); self.in_cell=False
        elif self.in_table and tag=="tr":
            if self.row: self.table.append(self.row)
        elif tag=="table" and self.in_table:
            if self.table: self.tables.append(self.table)
            self.in_table=False

def parse_html(raw: bytes):
    text=raw.decode("utf-8", errors="replace")
    p=Tables(); p.feed(text)
    return text, p.tables

def collect(out: Path, opener=urllib.request.urlopen):
    req=urllib.request.Request(URL, headers={"User-Agent":"PRECISION-WIRES public aggregate data QA/1.0"})
    with opener(req, timeout=30) as response:
        raw=response.read()
        status=getattr(response,"status",200)
        content_type=response.headers.get("Content-Type","")
        final_url=response.geturl()
    if status != 200: raise RuntimeError(f"HTTP status {status}")
    if "html" not in content_type.lower(): raise RuntimeError(f"Unexpected content type: {content_type}")
    html, tables=parse_html(raw)
    required=("September 2026","6.7","Base: 2022-23=100","STATEMENT II A")
    missing=[x for x in required if x.lower() not in html.lower()]
    if missing: raise RuntimeError(f"Official release content markers missing: {missing}")
    out.mkdir(parents=True, exist_ok=True)
    (out/"mospi_iip_release_raw.html").write_bytes(raw)
    (out/"mospi_iip_tables.json").write_text(json.dumps(tables,ensure_ascii=False,indent=2),encoding="utf-8")
    manifest={
      "source":"MoSPI release via Press Information Bureau",
      "url":URL,"final_url":final_url,"http_status":status,"content_type":content_type,
      "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),
      "sha256_raw":hashlib.sha256(raw).hexdigest(),"raw_bytes":len(raw),
      "table_count":len(tables),"release_reference_period":"2026-09",
      "release_posted_ist":"2026-10-28 16:00",
      "base_year":"2022-23","series_deflator":"Output PPI",
      "verification":"PUBLIC_HTML_CAPTURE_AND_MARKER_QA_ONLY",
      "limitations":["No e-Sankhyiki CSV/API response captured in this run.",
        "HTML table extraction is archival diagnostic; numeric schema/domain normalization remains pending.",
        "Quick estimates are revisable; preserve each release vintage."]
    }
    (out/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return manifest

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--out",default="artifacts/mospi_iip_public_smoke")
    args=ap.parse_args(); print(json.dumps(collect(Path(args.out)),indent=2))
