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
from urllib.parse import urljoin, urlparse

import hashlib, json, re, zipfile, io, os
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
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
        "REVENUE_FACT","PAT_FACT","EPS_FACT","REVENUE_UNIT","PAT_UNIT","EPS_UNIT","REVENUE_CONTEXT_START","PAT_CONTEXT_START","EPS_CONTEXT_START","SOURCE_SHA256","SOURCE_CONTENT_TYPE","EXTRACTION_STATUS",
        "EVIDENCE_PATH","OBSERVED_AT_UTC"]
ALIASES={
 "REVENUE":["revenuefromoperations","revenuefromoperation","revenue","incomefromoperations"],
 "PAT":["profitlossforperiod","profitlossfortheperiod","profitloss","profitaftertax","profitaftertaxation","profitlossaftertax","profitlossaftertaxbeforeextraordinaryitems","profitlossaftertaxandextraordinaryitems","profitlossfromcontinuingoperations"],
 "EPS":["earningspersharebasic","basicearningspershare","earningspersharediluted","dilutedearningspershare","basicearningslosspersharefromcontinuinganddiscontinuedoperations","basicearningslosspersharefromcontinuingoperations","dilutedearningslosspersharefromcontinuinganddiscontinuedoperations","dilutedearningslosspersharefromcontinuingoperations","basicearningspershareafterextraordinaryitems","basicearningspersharebeforeextraordinaryitems","dilutedearningspershareafterextraordinaryitems","dilutedearningspersharebeforeextraordinaryitems","basicanddilutedepsbeforeextraordinaryitemsnetoftaxexpensefortheperiodnottobeannualized","basicanddilutedepsafterextraordinaryitemsnetoftaxexpensefortheperiodnottobeannualized"]
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
 s=str(v or "").strip()
 if not s:
  return ""
 # ISO dates must be parsed as year-month-day; pandas dayfirst=True can
 # silently reinterpret 2026-04-01 as 2026-01-04 and corrupt XBRL contexts.
 if re.fullmatch(r"\d{4}-\d{2}-\d{2}",s):
  try:
   return datetime.strptime(s,"%Y-%m-%d").date().isoformat()
  except ValueError:
   return ""
 d=pd.to_datetime(s,errors="coerce",dayfirst=True)
 return "" if pd.isna(d) else d.date().isoformat()
def get(row,*names):
 for n in names:
  for c in row.index:
   if str(c).strip().lower().replace("_","") == n.lower().replace("_",""):
    v=row[c]
    if pd.notna(v) and str(v).strip(): return v
 return ""
class _InlineXbrlHTMLTree(HTMLParser):
 """Build a small tolerant tree for NSE's occasionally non-well-formed iXBRL HTML."""
 VOID={"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
 def __init__(self):
  super().__init__(convert_charrefs=True)
  self.root=ET.Element("htmlroot")
  self.stack=[self.root]
 def handle_starttag(self,tag,attrs):
  node=ET.SubElement(self.stack[-1],tag,{str(k).lower():str(v or "") for k,v in attrs if k})
  if tag.lower() not in self.VOID:
   self.stack.append(node)
 def handle_startendtag(self,tag,attrs):
  self.handle_starttag(tag,attrs)
  if tag.lower() not in self.VOID and len(self.stack)>1:
   self.stack.pop()
 def handle_endtag(self,tag):
  wanted=tag.lower()
  for i in range(len(self.stack)-1,0,-1):
   if self.stack[i].tag.lower()==wanted:
    del self.stack[i:]
    break
 def handle_data(self,data):
  if not self.stack: return
  node=self.stack[-1]
  if len(node):
   child=node[-1]
   child.tail=(child.tail or "")+data
  else:
   node.text=(node.text or "")+data

def _parse_html_tree(blob):
 parser=_InlineXbrlHTMLTree()
 parser.feed(blob.decode("utf-8",errors="replace"))
 parser.close()
 return parser.root

class _AttachmentLinkCollector(HTMLParser):
 """Collect candidate attachment links from NSE's rendered IndAS Details pages."""
 def __init__(self):
  super().__init__(convert_charrefs=True)
  self.values=[]
 def handle_starttag(self,tag,attrs):
  attrs={str(k).lower():str(v or "") for k,v in attrs if k}
  for key in ("href","src","data","data-href","data-url","onclick"):
   if attrs.get(key):
    self.values.append(attrs[key])

def discover_official_attachments(blob, base_url, limit=8):
 """Find bounded official NSE attachment URLs; reject off-host and unrelated links."""
 try:
  parser=_AttachmentLinkCollector()
  parser.feed(blob.decode("utf-8",errors="replace"))
  parser.close()
 except Exception:
  return []
 allowed_hosts={"nsearchives.nseindia.com","archives.nseindia.com","www.nseindia.com","www1.nseindia.com"}
 allowed_paths=("/corporate/xbrl/","/corporate/ixbrl/","/corporate/pdf/","/corporate/attachments/","/corporate/announcements/")
 found=[]
 for raw in parser.values:
  for candidate in re.findall(r"""(?:https?:)?//[^\s"'<>]+|(?:/|\./)[^\s"'<>]+""",raw):
   url=urljoin(base_url,candidate.rstrip(")],;}"))
   try:
    parsed=urlparse(url)
    path=parsed.path.lower()
    if parsed.scheme!="https" or parsed.hostname not in allowed_hosts:
     continue
    if not path.startswith(allowed_paths) or not re.search(r"\.(?:xml|xbrl|html?|pdf|zip)$",path):
     continue
    if url not in found:
     found.append(url)
    if len(found)>=limit:
     return found
   except Exception:
    continue
 return found

def parse_xbrl(blob):
 """Return recognized facts only when context and numeric value are explicit."""
 root=None
 # NSE iXBRL files are HTML documents and can contain harmless HTML constructs
 # that ElementTree rejects. Parse them with a tolerant tree while preserving
 # ix:fact attributes, xbrli contexts, period dates, and explicit dimensions.
 if re.search(br"<\s*(?:[a-z0-9_-]+:)?html\b",blob[:8192],re.I):
  try: root=_parse_html_tree(blob)
  except Exception: root=None
 if root is None:
  try: root=ET.fromstring(blob)
  except Exception:
   try:
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
     name=next((n for n in z.namelist() if n.lower().endswith((".xml",".xbrl"))),None)
     if not name: return []
     root=ET.fromstring(z.read(name))
   except Exception:
    try: root=_parse_html_tree(blob)
    except Exception: return []
 contexts={}
 for node in root.iter():
  if local(node.tag)=="context":
   ident=node.attrib.get("id",""); period={}; dimensions=[]
   for child in node.iter():
    k=local(child.tag)
    if k in ("instant","startdate","enddate"): period[k]=child.text or ""
    # Preserve explicit XBRL dimensional members: these can be the only
    # machine-readable distinction between standalone and consolidated filings.
    if k == "explicitmember":
     member=(child.text or "").strip()
     dimension=str(child.attrib.get("dimension","")).strip()
     if member and dimension:
      dimensions.append({"dimension":dimension,"member":member})
   period["dimensions"]=dimensions
   contexts[ident]=period
 facts=[]
 for node in root.iter():
  tag=local(node.tag)
  # Inline XBRL facts are rendered as ix:nonfraction/ix:fraction nodes; the
  # taxonomy concept is carried by their "name" attribute, not the element tag.
  fact_name=str(node.attrib.get("name","")).strip()
  if fact_name and tag in {"nonfraction","fraction","nonnumeric"}:
   tag=local(fact_name)
  text_value="".join(node.itertext()).strip()
  if not text_value: continue
  ctx=node.attrib.get("contextRef","") or node.attrib.get("contextref","")
  if not ctx or ctx not in contexts: continue
  try:
   clean=re.sub(r"\s+","",text_value).replace(",","")
   value=float(clean)
   if node.attrib.get("scale") not in (None,""):
    value *= 10 ** int(node.attrib["scale"])
   if str(node.attrib.get("sign","")).strip()=="-":
    value = -abs(value)
  except Exception: continue
  period=contexts[ctx]
  end=period.get("enddate") or period.get("instant","")
  if not end: continue
  facts.append({"tag":tag,"value":value,"context":ctx,"period_end":date_iso(end),
                "start_date":date_iso(period.get("startdate","")),"instant":bool(period.get("instant")),
                "unit":node.attrib.get("unitRef","") or node.attrib.get("unitref",""),
                "dimensions":period.get("dimensions",[])})
 return facts
def fetch_attachment(session, url):
 """Fetch an official NSE attachment, falling back between official archive hosts on 403."""
 candidates = [url]
 if url.startswith("https://nsearchives.nseindia.com/"):
  candidates.append(url.replace("https://nsearchives.nseindia.com/", "https://archives.nseindia.com/", 1))
 elif url.startswith("https://archives.nseindia.com/"):
  candidates.append(url.replace("https://archives.nseindia.com/", "https://nsearchives.nseindia.com/", 1))
 last_error = None
 for candidate in dict.fromkeys(candidates):
  try:
   response = session.get(candidate, timeout=(8, 35))
   if response.status_code == 403 and candidate != candidates[-1]:
    last_error = requests.HTTPError(f"403 from official archive host: {candidate}")
    continue
   response.raise_for_status()
   return response, candidate
  except Exception as exc:
   last_error = exc
 if last_error:
  raise last_error
 raise RuntimeError("No official attachment URL candidates")

def parse_pdf_text(blob):
 """Extract selectable PDF text; scanned/image-only PDFs remain blocked, never OCR-guessed."""
 try:
  reader=PdfReader(io.BytesIO(blob))
  return "\\n".join((page.extract_text() or "") for page in reader.pages)
 except Exception:
  return ""
def pdf_evidence_lines(text):
 """Capture candidate lines around financial labels for auditable manual review."""
 lines=[re.sub(r"\s+"," ",x).strip() for x in text.splitlines() if x.strip()]
 patterns={
  "REVENUE":re.compile(r"revenue from operations|total income|income from operations",re.I),
  "PAT":re.compile(r"profit\s*/?\s*(?:loss\s*)?for the period|profit for the year|net profit|profit after tax",re.I),
  "EPS":re.compile(r"earnings per share|basic and diluted|basic earnings per share",re.I),
 }
 found={}
 for metric,pat in patterns.items():
  found[metric]=[{"line_index":i,"text":line} for i,line in enumerate(lines) if pat.search(line)][:20]
 return {"line_count":len(lines),"text_chars":len(text),"metric_candidates":found}
def parse_agel_q2fy27_pdf_metrics(pdf_path):
 """Parse AGEL Q2 FY27 statement tables by page, basis, and first quarter column.
 Values are accepted only when the issuer, reporting period, statement heading,
 row labels, six comparative columns, and units are all explicitly present.
 """
 reader=PdfReader(str(pdf_path))
 pages=[(page.extract_text() or "") for page in reader.pages]
 def norm(s): return re.sub(r"\\s+"," ",s).strip()
 def row_values(page_text, label_pattern):
  for line in page_text.splitlines():
   line=norm(line)
   if re.search(label_pattern,line,re.I):
    tail=re.sub(label_pattern,"",line,count=1,flags=re.I).strip()
    vals=re.findall(r"(?<![A-Za-z])\\(?-?\\d[\\d,]*(?:\\.\\d+)?\\)?",tail)
    vals=[float(v.replace(",","").replace("(","-").replace(")","")) for v in vals]
    if len(vals)>=6: return vals[:6]
  return None
 result={}
 for basis, page_no, heading in [
  ("STANDALONE",4,r"UNAUDITED STANDALONE FINANCIAL RESULTS.*30TH SEPTEMBER, 2026"),
  ("CONSOLIDATED",18,r"UNAUDITED CONSOLIDATED FINANCIAL RESULTS.*30TH SEPTEMBER, 2026")]:
  if page_no>len(pages): raise ValueError(f"AGEL PDF missing expected {basis} table page {page_no}")
  page=pages[page_no-1]
  flat=norm(page)
  if not re.search(heading,flat,re.I) or not re.search(r"30\\.09\\.2026",flat) or not re.search(r"\\(?in Crores\\)?|₹ in Crores|\\(?₹ in Crores\\)?|\\(?f in Crores\\)?",flat,re.I):
   raise ValueError(f"AGEL PDF table identity/period/unit check failed: {basis} page {page_no}")
  if basis=="STANDALONE":
   power=row_values(page,r"i\\.\\s*Power Supply")
   goods=row_values(page,r"ii\\.\\s*Sale of Goods/ Equipments and related Services")
   other=row_values(page,r"iii\\.\\s*Others \\(refer note 7\\)")
   pat=row_values(page,r"7\\s+Profit\\s*/\\s*\\(Loss\\) after tax")
   eps=row_values(page,r"Basic and Diluted EPS")
  else:
   power=row_values(page,r"i\\.\\s*Power Supply")
   goods=row_values(page,r"ii\\.\\s*Sale of Goods/ Equipments and Related Services")
   other=row_values(page,r"iii\\.\\s*Others \\(Refer note 14\\)")
   pat=row_values(page,r"9\\s+Profit for the period/ year")
   eps=row_values(page,r"Basic EPS \\(In")
  if not all([power,goods,other,pat,eps]):
   raise ValueError(f"AGEL PDF required row parse failed: {basis} page {page_no}")
  revenue=power[0]+goods[0]+other[0]
  result[basis]={"period_end":"2026-09-30","revenue":revenue,"pat":pat[0],"eps":eps[0],
   "revenue_unit":"INR_CRORE","pat_unit":"INR_CRORE","eps_unit":"INR_PER_SHARE",
   "revenue_fact":f"PDF:p{page_no}:Revenue from Operations = Power Supply {power[0]} + Sale of Goods/Equipments and related Services {goods[0]} + Others {other[0]}",
   "pat_fact":f"PDF:p{page_no}:{"Profit/(Loss) after tax" if basis=="STANDALONE" else "Profit for the period/year"}",
   "eps_fact":f"PDF:p{page_no}:{"Basic and Diluted EPS" if basis=="STANDALONE" else "Basic EPS"}",
   "evidence_page":page_no}
 return result

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
def basis_from_xbrl_facts(selected_facts):
 """Return a basis only when each selected metric fact explicitly agrees via XBRL dimensions."""
 if not selected_facts:
  return ""
 observed=[]
 for fact in selected_facts:
  labels=[]
  for dimension in fact.get("dimensions",[]) or []:
   labels.extend([str(dimension.get("dimension","")),str(dimension.get("member",""))])
  text_value=" ".join(labels).lower()
  has_consolidated=bool(re.search(r"consolidat(?:ed|ion)",text_value))
  has_standalone=bool(re.search(r"standalone",text_value))
  if has_consolidated == has_standalone:
   return ""
  observed.append("CONSOLIDATED" if has_consolidated else "STANDALONE")
 return observed[0] if len(set(observed)) == 1 and len(observed) == len(selected_facts) else ""

def main():
 EVIDENCE.mkdir(parents=True,exist_ok=True); REPORT.parent.mkdir(parents=True,exist_ok=True)
 if not DISC.exists():
  REPORT.write_text(json.dumps({"status":"BLOCKED_MISSING_DISCLOSURES","rows":0},indent=2)); return 0
 df=pd.read_csv(DISC,dtype=str).fillna("")
 # Optional hard cap keeps live attachment verification bounded in CI. Preserve
 # newest disclosures first; uncapped runs remain the default for full research.
 max_disclosures=int(os.environ.get("QUARTERLY_METRIC_MAX_DISCLOSURES", "500") or 500)
 result_rows=df[df.get("EVENT_KIND", pd.Series(dtype=str)).eq("RESULT_DISCLOSURE")].copy()
 if max_disclosures > 0 and len(result_rows) > max_disclosures:
  result_rows=result_rows.head(max_disclosures)
  df=pd.concat([result_rows, df[~df.get("EVENT_KIND", pd.Series(dtype=str)).eq("RESULT_DISCLOSURE")]], ignore_index=True)
 sess=requests.Session(); sess.headers.update(HEADERS)
 # Establish NSE web-session cookies before requesting archived filing attachments.
 try:
  sess.get(NSE + "/companies-listing/corporate-filings-application", timeout=(5, 12))
 except Exception:
  pass
 out=[]; errors=[]; attempted=0
 agel_pdf_metrics={}
 agel_pdf_path=ROOT/"data/raw/quarterly_filing_evidence/AGEL_Q2_FY27_financial_statement.pdf"
 if agel_pdf_path.exists():
  try:
   agel_pdf_metrics=parse_agel_q2fy27_pdf_metrics(agel_pdf_path)
   pdf_blob=agel_pdf_path.read_bytes()
   (EVIDENCE/(sha(pdf_blob)+".pdf")).write_bytes(pdf_blob)
  except Exception as exc:
   errors.append({"symbol":"ADANIGREEN","reason":"OFFICIAL_PDF_TABLE_PARSE_BLOCKED:"+str(exc)[:300]})
 for _,r in df.iterrows():
  if str(r.get("EVENT_KIND",""))!="RESULT_DISCLOSURE": continue
  raw={}
  try: raw=json.loads(r.get("RAW_RECORD_JSON","{}") or "{}")
  except Exception: raw={}
  symbol=str(r.get("SYMBOL","") or "").strip().upper()
  isin=str(r.get("ISIN","") or "").strip().upper()
  if not isin and symbol:
   # Use the same evidence-backed resolver as Step 2. It only returns an ISIN
   # from the official security master or a company-matched official filing.
   from pipeline.quarterly_results_research import security_isin
   isin=security_isin(symbol,raw)
  period=date_iso(r.get("PERIOD_END",""))
  # Revision disclosures can lack BROADCAST_AT while the event normalizer
  # preserves their explicit revision publication time separately. Use that
  # timestamp for the revision event only; never infer from creation_Date.
  disclosed_raw = r.get("PUBLICATION_TIMESTAMP", "") or r.get("BROADCAST_AT", "")
  disclosed=pd.to_datetime(disclosed_raw,errors="coerce",utc=True)
  disclosed_at="" if pd.isna(disclosed) else disclosed.isoformat()
  links=[]
  for key in ("xbrl","xbrlurl","xbrlfile","xbrlfileurl","xbrlfilepath","xbrlattachment","xbrlattachmenturl","ixbrl","ixbrlurl","ixbrlfile","ixbrlfileurl","ixbrlfilepath","attchmntfile","attachment","attachmenturl","detailsurl","pdfurl","fileurl"):
   for k,v in raw.items():
    if k.lower()==key.lower() and v:
     u=norm_url(v)
     if u and u not in links: links.append(u)
  if not links and r.get("ATTACHMENT_URL"): links=[norm_url(r["ATTACHMENT_URL"])]
  # Initialize per-disclosure evidence fields so missing/bad attachments remain BLOCKED, not a crash.
  source_digest=""; source_content_type=""; evidence_path=""
  extracted=False
  # Bounded queue: rendered NSE detail HTML may link to the actual iXBRL/XML.
  links=list(dict.fromkeys(u for u in links if u))
  link_index=0
  while link_index < len(links) and link_index < 8:
   url=links[link_index]
   link_index+=1
   attempted+=1
   try:
    resp, fetched_url=fetch_attachment(sess, url)
    url=fetched_url
    blob=resp.content; digest=sha(blob); ctype=resp.headers.get("Content-Type","")
    is_pdf=("pdf" in ctype.lower() or blob.startswith(b"%PDF"))
    is_xml=("xml" in ctype.lower() or blob.lstrip().startswith(b"<?xml"))
    suffix=".pdf" if is_pdf else ".xbrl" if is_xml else ".bin"
    ev=EVIDENCE/(digest+suffix)
    if not ev.exists(): ev.write_bytes(blob)
    evidence_path=str(ev); source_digest=digest; source_content_type=ctype
    facts=parse_xbrl(blob)
    # Follow explicit attachment links on rendered NSE IndAS Details pages only.
    if not facts and ("html" in ctype.lower() or re.search(br"<\s*(?:!doctype\s+)?html\b",blob[:8192],re.I)) and link_index < 8:
     for discovered_url in discover_official_attachments(blob, resp.url, limit=8):
      if discovered_url not in links and len(links) < 8:
       links.append(discovered_url)
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
    # Insurance filing taxonomies use sector-specific aggregate income concepts,
    # not the industrial RevenueFromOperations tag. Keep the exact source fact
    # tag in the ledger; never substitute PBT or a component premium fact.
    if rev is None and re.search(r"INTEGRATED_FILING_GI_", url, re.I):
     rev=choose(facts,["operatingincome"],period)
    if rev is None and re.search(r"IF_INS_COM_IND_AS_", url, re.I):
     # Insurance-company Ind AS 117 taxonomy explicitly reports InsuranceRevenue.
     # Do not substitute GrossWrittenPremium or segment-level revenue.
     rev=choose(facts,["insurancerevenue"],period)
    if rev is None and re.search(r"INTEGRATED_FILING_LI_", url, re.I):
     rev=choose(facts,["income"],period)
    # Banking/NBFC integrated filings also use taxonomy concept Income.
    if rev is None and re.search(r"INTEGRATED_FILING_(BANKING|NBFC)", url, re.I):
     rev=choose(facts,["income"],period)
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
     # If filing metadata is silent, accept basis only when Revenue, PAT and
     # EPS contexts each carry the same explicit XBRL dimensional member.
     if not basis:
      basis=basis_from_xbrl_facts([rev,pat,eps])
     if basis:
      out.append({"SYMBOL":symbol,"ISIN":isin,"PERIOD_END":period,"BASIS":basis,"SOURCE_URL":url,
       "DISCLOSED_AT":disclosed_at,"REVENUE":rev["value"],"PAT":pat["value"],"EPS":eps["value"],
       "REVENUE_FACT":rev["tag"]+":"+rev["context"],"PAT_FACT":pat["tag"]+":"+pat["context"],
       "EPS_FACT":eps["tag"]+":"+eps["context"],"REVENUE_UNIT":rev["unit"],"PAT_UNIT":pat["unit"],"EPS_UNIT":eps["unit"],
       "REVENUE_CONTEXT_START":rev["start_date"],"PAT_CONTEXT_START":pat["start_date"],"EPS_CONTEXT_START":eps["start_date"],"SOURCE_SHA256":digest,
       "SOURCE_CONTENT_TYPE":resp.headers.get("Content-Type",""),"EXTRACTION_STATUS":"SOURCE_LINKED_XBRL_FACTS",
       "EVIDENCE_PATH":str(ev),"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
      extracted=True; break
    fact_tag_counts={}
    for fact in facts:
     tag=str(fact.get("tag","")).lower()
     if any(token in tag for token in ("revenue","income","profit","earningspershare","eps","premium")):
      fact_tag_counts[tag]=fact_tag_counts.get(tag,0)+1
    errors.append({"symbol":symbol,"url":url,"reason":"BLOCKED_FACTS_OR_BASIS_INCOMPLETE",
     "facts_found":len(facts),"period_end":period,
     "metric_presence":{"REVENUE":bool(rev),"PAT":bool(pat),"EPS":bool(eps)},
     "metric_candidate_tags":sorted(fact_tag_counts)[:100],
     "selected_fact_details":{
      "REVENUE":None if not rev else {"tag":rev.get("tag"),"context":rev.get("context"),"unit":rev.get("unit"),"period_end":rev.get("period_end"),"start_date":rev.get("start_date"),"dimensions":rev.get("dimensions",[])},
      "PAT":None if not pat else {"tag":pat.get("tag"),"context":pat.get("context"),"unit":pat.get("unit"),"period_end":pat.get("period_end"),"start_date":pat.get("start_date"),"dimensions":pat.get("dimensions",[])} ,
      "EPS":None if not eps else {"tag":eps.get("tag"),"context":eps.get("context"),"unit":eps.get("unit"),"period_end":eps.get("period_end"),"start_date":eps.get("start_date"),"dimensions":eps.get("dimensions",[])}},
     "basis_metadata":{"consolidated":str(raw.get("consolidated","")),"subject":str(r.get("SUBJECT","")),"attachment_text":str(raw.get("attchmntText",""))[:300]},"response_diagnostics":{"content_type":ctype,"bytes":len(blob),"prefix":blob[:500].decode("utf-8",errors="replace"),"contains_ix_nonfraction":bool(re.search(br"ix:nonfraction",blob,re.I)),"contains_context":bool(re.search(br"(?:xbrli:)?context",blob,re.I)),"final_url":resp.url}})
   except Exception as exc: errors.append({"symbol":symbol,"url":url,"reason":type(exc).__name__+":"+str(exc)[:200]})
  if not extracted:
   # Issuer PDF fallback is tightly scoped to the matching issuer, ISIN, period,
   # and basis declared by the NSE disclosure metadata. Never infer basis from
   # row order or copy consolidated figures into standalone disclosures.
   declared_basis=str(raw.get("consolidated","") or "").strip().upper()
   if symbol=="ADANIGREEN" and isin=="INE364U01010" and period=="2026-09-30" and disclosed_at and declared_basis=="STANDALONE" and "STANDALONE" in agel_pdf_metrics:
    m=agel_pdf_metrics["STANDALONE"]
    pdf_blob=agel_pdf_path.read_bytes()
    digest=sha(pdf_blob)
    out.append({"SYMBOL":symbol,"ISIN":isin,"PERIOD_END":period,"BASIS":"STANDALONE",
     "SOURCE_URL":"https://www.adanigreenenergy.com/-/media/project/greenenergy/investor-downloads/financial-statements-dynamic/agel_q2fy27_financial-statement_vf.pdf",
     "DISCLOSED_AT":disclosed_at,"REVENUE":m["revenue"],"PAT":m["pat"],"EPS":m["eps"],
     "REVENUE_FACT":m["revenue_fact"],"PAT_FACT":m["pat_fact"],"EPS_FACT":m["eps_fact"],
     "REVENUE_UNIT":m["revenue_unit"],"PAT_UNIT":m["pat_unit"],"EPS_UNIT":m["eps_unit"],
     "REVENUE_CONTEXT_START":"","PAT_CONTEXT_START":"","EPS_CONTEXT_START":"",
     "SOURCE_SHA256":digest,"SOURCE_CONTENT_TYPE":"application/pdf",
     "EXTRACTION_STATUS":"SOURCE_LINKED_PDF_TABLE_FACTS","EVIDENCE_PATH":str(EVIDENCE/(digest+".pdf")),
     "OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
   else:
    out.append({"SYMBOL":symbol,"ISIN":isin,"PERIOD_END":period,"BASIS":"","SOURCE_URL":links[0] if links else norm_url(r.get("SOURCE_URL","")),
     "DISCLOSED_AT":disclosed_at,"REVENUE":"","PAT":"","EPS":"","REVENUE_FACT":"","PAT_FACT":"","EPS_FACT":"",
     "SOURCE_SHA256":source_digest,"SOURCE_CONTENT_TYPE":source_content_type,
     "EXTRACTION_STATUS":"BLOCKED_NO_VERIFIED_XBRL_METRICS",
     "EVIDENCE_PATH":evidence_path,"OBSERVED_AT_UTC":datetime.now(timezone.utc).isoformat()})
 result=pd.DataFrame(out,columns=FIELDS)
 # A later official revision supersedes an earlier filing for the same symbol,
 # period and basis. Do not block both rows merely because revision history
 # exists. If multiple different source files share the exact latest timestamp,
 # keep them blocked as ambiguous rather than selecting one arbitrarily.
 if not result.empty:
  valid_mask=result.EXTRACTION_STATUS.isin(["SOURCE_LINKED_XBRL_FACTS","SOURCE_LINKED_PDF_TABLE_FACTS"])
  valid_rows=result.loc[valid_mask].copy()
  if not valid_rows.empty:
   valid_rows["_DISCLOSED_SORT"]=pd.to_datetime(valid_rows["DISCLOSED_AT"],errors="coerce",utc=True)
   for _, group in valid_rows.groupby(["SYMBOL","PERIOD_END","BASIS"],dropna=False):
    if len(group) < 2:
     continue
    latest=group["_DISCLOSED_SORT"].max()
    latest_rows=group[group["_DISCLOSED_SORT"].eq(latest)]
    if len(latest_rows) == 1 and pd.notna(latest):
     superseded=group.index.difference(latest_rows.index)
     result.loc[superseded,"EXTRACTION_STATUS"]="SUPERSEDED_BY_LATER_DISCLOSURE"
    else:
     result.loc[group.index,"EXTRACTION_STATUS"]="BLOCKED_AMBIGUOUS_LATEST_PERIOD_BASIS"
     result.loc[group.index,["REVENUE","PAT","EPS"]]=""
 result.to_csv(OUT,index=False)
 valid=int(result.EXTRACTION_STATUS.eq("SOURCE_LINKED_XBRL_FACTS").sum())
 superseded=int(result.EXTRACTION_STATUS.eq("SUPERSEDED_BY_LATER_DISCLOSURE").sum())
 report={"status":"COMPUTED_WITH_VERIFIED_ROWS" if valid else "BLOCKED_NO_VERIFIED_ROWS",
  "input_result_disclosures":int((df.get("EVENT_KIND","")== "RESULT_DISCLOSURE").sum()),
  "attachment_attempts":attempted,"ledger_rows":len(result),"verified_metric_rows":valid,
  "blocked_rows":int(result.EXTRACTION_STATUS.str.startswith("BLOCKED").sum()),"superseded_revision_rows":superseded,"ledger_path":str(OUT),"evidence_dir":str(EVIDENCE),
  "required_provenance":["SYMBOL","ISIN","PERIOD_END","BASIS","SOURCE_URL","DISCLOSED_AT","REVENUE","PAT","EPS","SOURCE_SHA256","fact tags and context refs"],
  "policy":"No PDF OCR guessing or headline-derived values; the AGEL issuer PDF fallback is limited to exact issuer/ISIN/period/basis metadata and validated table pages, units, and row labels; unparsed facts stay BLOCKED.",
  "pdf_text_extraction_attempts":sum(1 for e in errors if "pdf_candidates" in e),
  "pdf_candidate_diagnostics":[e["pdf_candidates"] for e in errors if "pdf_candidates" in e][:20],
  "errors":errors[:100]}
 REPORT.write_text(json.dumps(report,indent=2),encoding="utf-8")
 print(json.dumps(report,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())