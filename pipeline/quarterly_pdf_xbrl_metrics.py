#!/usr/bin/env python3
"""Audit-only source-linked financial metric ledger from NSE PDF/XBRL attachments.

The collector never estimates values from headlines. It downloads original NSE
attachments, extracts recognized XBRL facts with explicit contexts/units, and
writes one row per symbol/ISIN/period/basis with hashes and provenance. PDFs
are retained as evidence but not OCR-guessed; if XBRL facts cannot be mapped,
the row is BLOCKED for manual PDF review.
"""
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urljoin
import hashlib, json, re, zipfile, io
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from pypdf import PdfReader

ROOT=Path(".")
DISC=ROOT/"data/raw/quarterly_results_disclosures.csv"
OUT=ROOT/"data/raw/quarterly_financial_metrics.csv"
EVIDENCE=ROOT/"data/raw/quarterly_filing_evidence"
REPORT=ROOT/"outputs/quarterly_results/filing_metric_extraction_report.json"
NSE="https://www.nseindia.com"
HEADERS={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/132 Safari/537.36",
         "Accept":"application/json,text/html,application/pdf,application/xml,*/*",
         "Referer":NSE+"/companies-listing/corporate-filings-application"}
FIELDS=["SYMBOL","ISIN","PERIOD_END","BASIS","SOURCE_URL","DISCLOSED_AT","REVENUE","PAT","EPS",
        "REVENUE_FACT","PAT_FACT","EPS_FACT","SOURCE_SHA256","SOURCE_CONTENT_TYPE","EXTRACTION_STATUS",
        "EVIDENCE_PATH","OBSERVED_AT_UTC"]
ALIASES={
 "REVENUE":["revenuefromoperations","revenuefromoperation","revenue","income from operations","revenuefromoperations"],
 "PAT":["profitlossfortheperiod","profitloss","profitaftertax","profitaftertaxation","profitlossfromcontinuingoperations"],
 "EPS":["earningspersharebasic","basicearningspershare","earningspersharediluted","dilutedearningspershare"]
}
def local(tag): return tag.rsplit("}",1)[-1].split(":")[-1].lower()
def sha(b): return hashlib.sha256(b).hexdigest()
def norm_url(value):
 s=str(value or "").strip()
 if not s: return ""
 if s.startswith("//"): return "https:"+s
 if s.startswith("/"): return urljoin(NSE,s)
 return s if s.startswith("http") else ""
def date_iso(v):
 d=pd.to_datetime(v,errors="coerce",dayfirst=True)
 return "" if pd.isna(d) else d.date().isoformat()
def get(row,*names):
 for n in names:
  for c in row.index:
   if str(c).strip().lower().replace("_","") == n.lower().replace("_",""):
    v=row[c]
    if pd.notna(v) and str(v).strip(): return v
 return ""
def parse_xbrl(blob):
 """Return recognized facts only when context and numeric value are explicit."""
 try: root=ET.fromstring(blob)
 except Exception:
  try:
   with zipfile.ZipFile(io.BytesIO(blob)) as z:
    name=next((n for n in z.namelist() if n.lower().endswith((".xml",".xbrl"))),None)
    if not name: return []
    root=ET.fromstring(z.read(name))
  except Exception: return []
 contexts={}
 for node in root.iter():
  if local(node.tag)=="context":
   ident=node.attrib.get("id",""); period={}
   for child in node.iter():
    k=local(child.tag)
    if k in ("instant","startdate","enddate"): period[k]=child.text or ""
   contexts[ident]=period
 facts=[]
 for node in root.iter():
  tag=local(node.tag)
  if not node.text or not node.text.strip(): continue
  ctx=node.attrib.get("contextRef","")
  if not ctx or ctx not in contexts: continue
  try: value=float(node.text.strip().replace(",",""))
  except Exception: continue
  period=contexts[ctx]
  end=period.get("enddate") or period.get("instant","")
  if not end: continue
  facts.append({"tag":tag,"value":value,"context":ctx,"period_end":date_iso(end),
                "start_date":date_iso(period.get("startdate","")),"instant":bool(period.get("instant")),
                "unit":node.attrib.get("unitRef","")})
 return facts
def parse_pdf_text(blob):
 """Extract selectable PDF text; scanned/image-only PDFs remain blocked, never OCR-guessed."""
 try:
  reader=PdfReader(io.BytesIO(blob))
  return "\\n".join((page.extract_text() or "") for page in reader.pages)
 except Exception:
  return ""
def pdf_evidence_lines(text):
 """Capture candidate lines around financial labels for auditable manual review."""
 lines=[re.sub(r"\\s+"," ",x).strip() for x in text.splitlines() if x.strip()]
 patterns={
  "REVENUE":re.compile(r"revenue from operations|total income|income from operations",re.I),
  "PAT":re.compile(r"profit/(?:loss )?for the period|profit for the year|net profit|profit after tax",re.I),
  "EPS":re.compile(r"earnings per share|basic and diluted|basic earnings per share",re.I),
 }
 found={}
 for metric,pat in patterns.items():
  found[metric]=[{"line_index":i,"text":line} for i,line in enumerate(lines) if pat.search(line)][:20]
 return {"line_count":len(lines),"text_chars":len(text),"metric_candidates":found}
def choose(facts, aliases, period, instant_preference=False):
 terms={re.sub(r"[^a-z0-9]","",x.lower()) for x in aliases}
 # Reject facts without an explicit unit/context. Revenue and PAT must be duration
 # facts; EPS may be duration-based but never inferred from a presentation table.
 cand=[f for f in facts if re.sub(r"[^a-z0-9]","",f["tag"]) in terms
       and f["period_end"]==period and f.get("unit") and f.get("context")]
 if not cand: return None
 if instant_preference: cand.sort(key=lambda f:(not f["instant"],f["tag"]))
 else: cand.sort(key=lambda f:(f["instant"],f["tag"]))
 return cand[0]
def main():
 EVIDENCE.mkdir(parents=True,exist_ok=True); REPORT.parent.mkdir(parents=True,exist_ok=True)
 if not DISC.exists():
  REPORT.write_text(json.dumps({"status":"BLOCKED_MISSING_DISCLOSURES","rows":0},indent=2)); return 0
 df=pd.read_csv(DISC,dtype=str).fillna("")
 sess=requests.Session(); sess.headers.update(HEADERS)
 out=[]; errors=[]; attempted=0
 for _,r in df.iterrows():
  if str(r.get("EVENT_KIND",""))!="RESULT_DISCLOSURE": continue
  raw={}
  try: raw=json.loads(r.get("RAW_RECORD_JSON","{}") or "{}")
  except Exception: raw={}
  symbol=str(r.get("SYMBOL","") or "").strip().upper()
  isin=str(r.get("ISIN","") or "").strip().upper()
  period=date_iso(r.get("PERIOD_END",""))
  disclosed=pd.to_datetime(r.get("BROADCAST_AT",""),errors="coerce",utc=True)
  disclosed_at="" if pd.isna(disclosed) else disclosed.isoformat()
  links=[]
  for key in ("xbrl","xbrlurl","xbrlfile","xbrlfileurl","xbrlfilepath","xbrlattachment","xbrlattachmenturl","attchmntfile","attachment","attachmenturl","detailsurl","pdfurl","fileurl"):
   for k,v in raw.items():
    if k.lower()==key.lower() and v:
     u=norm_url(v)
     if u and u not in links: links.append(u)
  if not links and r.get("ATTACHMENT_URL"): links=[norm_url(r["ATTACHMENT_URL"])]
  extracted=False
  for url in links:
   attempted+=1
   try:
    resp=sess.get(url,timeout=(8,35)); resp.raise_for_status()
    blob=resp.content; digest=sha(blob); ctype=resp.headers.get("Content-Type","")
    is_pdf=("pdf" in ctype.lower() or blob.startswith(b"%PDF"))
    is_xml=("xml" in ctype.lower() or blob.lstrip().startswith(b"<?xml"))
    suffix=".pdf" if is_pdf else ".xbrl" if is_xml else ".bin"
    ev=EVIDENCE/(digest+suffix)
    if not ev.exists(): ev.write_bytes(blob)
    evidence_path=str(ev); source_digest=digest; source_content_type=ctype
    facts=parse_xbrl(blob)
    if is_pdf:
     pdf_text=parse_pdf_text(blob)
     text_path=EVIDENCE/(digest+".txt")
     if pdf_text and not text_path.exists(): text_path.write_text(pdf_text,encoding="utf-8")
     evidence_path=str(ev)
     pdf_candidates={"source_url":url,"sha256":digest,"text_path":str(text_path) if pdf_text else "",
      "text_extraction":pdf_evidence_lines(pdf_text),"status":"TEXT_EXTRACTED_REQUIRES_CONTEXTUAL_VALIDATION" if pdf_text else "BLOCKED_SCANNED_OR_UNREADABLE_PDF"}
     if not facts: errors.append({"symbol":symbol,"url":url,"reason":pdf_candidates["status"],"pdf_text_chars":len(pdf_text),"pdf_candidates":pdf_candidates})
    if not period:
     # Only use a period explicitly represented in the downloaded XBRL contexts;
     # never infer from the filing timestamp.
     periods=sorted(set(f["period_end"] for f in facts if f["period_end"]))
     if len(periods)==1: period=periods[0]
    rev=choose(facts,ALIASES["REVENUE"],period)
    pat=choose(facts,ALIASES["PAT"],period)
    eps=choose(facts,ALIASES["EPS"],period)
    if rev and pat and eps and symbol and isin and period and disclosed_at:
     # Keep facts with exact filing provenance. Basis must be explicit in metadata/URL.
     txt=" ".join([str(r.get("SUBJECT","")),str(raw.get("attchmntText","")),str(raw.get("subject","")),str(raw.get("consolidated","")),url]).lower()
     basis_value=str(raw.get("consolidated","")).strip().lower()
     if basis_value == "consolidated": basis="CONSOLIDATED"
     elif basis_value == "standalone": basis="STANDALONE"
     elif "consolidated" in txt and "standalone" not in txt: basis="CONSOLIDATED"
     elif "standalone" in txt and "consolidated" not in txt: basis="STANDALONE"
     else: basis=""
     if basis:
      out.append({"SYMBOL":symbol,"ISIN":isin,"PERIOD_END":period,"BASIS":basis,"SOURCE_URL":url,
       "DISCLOSED_AT":disclosed_at,"REVENUE":rev["value"],"PAT":pat["value"],"EPS":eps["value"],
       "REVENUE_FACT":rev["tag"]+":"+rev["context"],"PAT_FACT":pat["tag"]+":"+pat["context"],
       "EPS_FACT":eps["tag"]+":"+eps["context"],"SOURCE_SHA256":digest,
       "SOURCE_CONTENT_TYPE":resp.headers.get("Content-Type",""),"EXTRACTION_STATUS":"SOURCE_LINKED_XBRL_FACTS",
       "EVIDENCE_PATH":str(ev),"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
      extracted=True; break
    errors.append({"symbol":symbol,"url":url,"reason":"BLOCKED_FACTS_OR_BASIS_INCOMPLETE","facts_found":len(facts),"period_end":period})
   except Exception as exc: errors.append({"symbol":symbol,"url":url,"reason":type(exc).__name__+":"+str(exc)[:200]})
  if not extracted:
   out.append({"SYMBOL":symbol,"ISIN":isin,"PERIOD_END":period,"BASIS":"","SOURCE_URL":links[0] if links else norm_url(r.get("SOURCE_URL","")),
    "DISCLOSED_AT":disclosed_at,"REVENUE":"","PAT":"","EPS":"","REVENUE_FACT":"","PAT_FACT":"","EPS_FACT":"",
    "SOURCE_SHA256":source_digest,"SOURCE_CONTENT_TYPE":source_content_type,
    "EXTRACTION_STATUS":"BLOCKED_NO_VERIFIED_XBRL_METRICS",
    "EVIDENCE_PATH":evidence_path,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
 result=pd.DataFrame(out,columns=FIELDS)
 # No ambiguous duplicates can silently pass into the feature builder.
 if not result.empty:
  valid=result[result.EXTRACTION_STATUS.eq("SOURCE_LINKED_XBRL_FACTS")]
  if valid.duplicated(["SYMBOL","PERIOD_END","BASIS"]).any():
   dup=valid[valid.duplicated(["SYMBOL","PERIOD_END","BASIS"],keep=False)].index
   result.loc[dup,"EXTRACTION_STATUS"]="BLOCKED_DUPLICATE_PERIOD_BASIS"
   result.loc[dup,["REVENUE","PAT","EPS"]]=""
 result.to_csv(OUT,index=False)
 valid=int(result.EXTRACTION_STATUS.eq("SOURCE_LINKED_XBRL_FACTS").sum())
 report={"status":"COMPUTED_WITH_VERIFIED_ROWS" if valid else "BLOCKED_NO_VERIFIED_ROWS",
  "input_result_disclosures":int((df.get("EVENT_KIND","")== "RESULT_DISCLOSURE").sum()),
  "attachment_attempts":attempted,"ledger_rows":len(result),"verified_metric_rows":valid,
  "blocked_rows":int(len(result)-valid),"ledger_path":str(OUT),"evidence_dir":str(EVIDENCE),
  "required_provenance":["SYMBOL","ISIN","PERIOD_END","BASIS","SOURCE_URL","DISCLOSED_AT","REVENUE","PAT","EPS","SOURCE_SHA256","fact tags and context refs"],
  "policy":"No PDF OCR guessing or headline-derived values; PDF text candidates are evidence only until symbol, period, basis, units and table columns are unambiguously verified; unparsed facts stay BLOCKED.",
  "pdf_text_extraction_attempts":sum(1 for e in errors if "pdf_candidates" in e),
  "pdf_candidate_diagnostics":[e["pdf_candidates"] for e in errors if "pdf_candidates" in e][:20],
  "errors":errors[:100]}
 REPORT.write_text(json.dumps(report,indent=2),encoding="utf-8")
 print(json.dumps(report,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
