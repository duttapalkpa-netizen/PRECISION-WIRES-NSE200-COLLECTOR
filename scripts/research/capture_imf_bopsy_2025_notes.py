#!/usr/bin/env python3
"""Capture official IMF BOPSY 2025 notes and derive reporting coverage metadata.
No BOP observations or estimated aggregate observations are generated.
"""
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,csv,re
URL="https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf"
OUT=Path("imf_bopsy_2025_official_notes"); OUT.mkdir(parents=True,exist_ok=True)
ts=datetime.now(timezone.utc).isoformat()
req=Request(URL,headers={"User-Agent":"PRECISION-WIRES-official-source-archive/1.0","Accept":"application/pdf"})
try:
 with urlopen(req,timeout=60) as r: status=r.status; headers=dict(r.headers.items()); raw=r.read()
except (HTTPError,URLError,TimeoutError) as e: status=getattr(e,"code",0); headers={}; raw=str(e).encode()
if status!=200 or not raw.startswith(b"%PDF-"): raise SystemExit(f"PDF capture failed HTTP={status}")
pdf=OUT/"BOPSY_Explanatory_Notes_November_2025.pdf"; pdf.write_bytes(raw)
from pypdf import PdfReader
reader=PdfReader(str(pdf)); pages=[p.extract_text() or "" for p in reader.pages]
if len(pages)!=31: raise SystemExit(f"Expected 31 PDF pages; got {len(pages)}")
(OUT/"extracted_text.txt").write_text("\n".join(pages),encoding="utf-8")
overview=[]
for pno in range(5,10):
 for line in pages[pno].splitlines():
  s=" ".join(line.split())
  m=re.match(r"^(.*?)\s+(USD|EUR|XDC)\s+(\d{4})(?:\s+(\d{4}))?$",s)
  if m: overview.append({"economy":m.group(1).strip(),"reporting_currency":m.group(2),"bop_last_reported_year":m.group(3),"iip_last_reported_year":m.group(4) or "","source_pdf_page":pno+1,"source_url":URL})
headings=["Advanced Economies","Euro Area","Emerging and Developing Economies","Emerging and Developing Asia","Emerging and Developing Europe","Middle East and Central Asia","Sub-Saharan Africa","Western Hemisphere"]
groups=[]; current=None
for line in "\n".join(pages[10:13]).splitlines():
 s=" ".join(line.split())
 if not s: continue
 if s in headings: current=s; continue
 if current and "International Monetary Fund" not in s and "Country Group Aggregates" not in s and not re.match(r"^(Notes|[0-9]+\s)",s):
  groups.append({"group_heading":current,"member_label":s,"source_url":URL})
def write_csv(name,rows,fields):
 with (OUT/name).open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
write_csv("country_reporting_coverage.csv",overview,["economy","reporting_currency","bop_last_reported_year","iip_last_reported_year","source_pdf_page","source_url"])
write_csv("country_group_membership_raw.csv",groups,["group_heading","member_label","source_url"])
manifest={"source":"International Monetary Fund","title":"BOPSY Explanatory Notes November 2025","source_url":URL,"retrieved_at_utc":ts,"http_status":status,"content_type":headers.get("Content-Type"),"byte_count":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"pdf_pages":len(pages),"country_reporting_coverage_rows_extracted":len(overview),"country_group_membership_rows_extracted":len(groups),"scope_note":"Reporting coverage and group metadata only, not BOP observations. BOPSY country-group aggregates can include estimates for nonreporting economies.","limitations":["Derived text/CSV is a convenience extraction and must be checked against source PDF pages before production use.","No quarterly observations or portfolio-flow observations are generated."]}
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(manifest,indent=2,ensure_ascii=False))
if len(overview)<100: raise SystemExit("Coverage extraction unexpectedly small; inspect raw PDF and extracted text")
