#!/usr/bin/env python3
"""Bounded official India macro-series source capture and fail-closed provenance QA.

GDP/CPI use MoSPI e-Sankhyiki catalogue vintages; WPI uses OEA/DPIIT;
Government capex uses CGA monthly accounts. PMI is published by S&P Global,
not Government of India; public headlines are not licensed underlying data.
Raw-file capture is never promoted to AVAILABLE without a reviewed normalized
schema adapter, valid periods/units/release timestamps, unique keys and QA.
"""
import hashlib,json,re,time
from io import StringIO
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urlencode,urljoin,quote
import requests,pandas as pd
from selectolax.parser import HTMLParser
API="https://api.mospi.gov.in/api/esankhyiki/"
LIST=API+"cms/golden-sheet/list"
DOWNLOAD=API+"file/download/"
RAW=Path("data/external/macro_series_raw"); OUT=Path("outputs/macro_geo")
UA="PRECISION-WIRES-NSE200-COLLECTOR/1.0 (official macro source audit)"
SOURCES={
"gdp":{"provider":"MoSPI e-Sankhyiki / National Accounts Statistics","url":"https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2304949&lang=1&reg=3","catalogue_url":"https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=NAS","terms":["quarterly estimates of gdp","gross domestic product"],"frequency":"QUARTERLY","unit":"INR crore; current/constant price basis mandatory"},
"cpi":{"provider":"MoSPI e-Sankhyiki / Consumer Price Index","url":"https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2322244&lang=1&reg=3","catalogue_url":"https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI","terms":["all india combined","general index and inflation"],"frequency":"MONTHLY","unit":"2024=100 index; geography and rural/urban mandatory"},
"wpi":{"provider":"Office of Economic Adviser, DPIIT","url":"https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2323098&lang=1&reg=1","catalogue_url":"https://eaindustry.nic.in/download_data_2223.asp","terms":["wholesale price index","wpi"],"frequency":"MONTHLY","unit":"2022-23=100 index; commodity class and vintage mandatory"},
"government_capex":{"provider":"Controller General of Accounts, Ministry of Finance","url":"https://cga.gov.in/MonthDashboardReport/Published/list.aspx","terms":["monthly accounts dashboard","capital expenditure"],"frequency":"MONTHLY_CUMULATIVE_FY","unit":"INR crore; actual vs budget and FY/month mandatory"},
"pmi":{"provider":"S&P Global PMI (publisher primary source; not Government of India)","url":"https://www.pmi.spglobal.com/Public/Release/PressReleases?language=en","terms":["india manufacturing pmi","india services pmi"],"frequency":"MONTHLY","unit":"Diffusion index; underlying historical series licensed"}
}
def sha(b): return hashlib.sha256(b).hexdigest()
def get(s,u):
 r=s.get(u,timeout=(5,25),headers={"User-Agent":UA,"Accept":"text/html,application/json,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,*/*"});r.raise_for_status()
 if not r.content: raise ValueError("empty source response")
 return r
def catalogue(s,product):
 r=get(s,LIST+"?"+urlencode({"product":product,"page":1,"limit":10})); p=r.json(); m=p.get("meta_data") or {}
 pages=int(m.get("totalPages") or 0); total=int(m.get("totalRecords") or 0)
 if pages<1 or total<1: raise ValueError("catalogue pagination metadata absent")
 rows=list(p.get("data") or [])
 for n in range(2,pages+1):
  time.sleep(.1); rows.extend(get(s,LIST+"?"+urlencode({"product":product,"page":n,"limit":10})).json().get("data") or [])
 if len(rows)<total: raise ValueError(f"catalogue pagination incomplete {len(rows)}/{total}")
 return rows,{"total_records":total,"total_pages":pages,"records_returned":len(rows),"first_page_sha256":sha(r.content)}
def select(rows,terms):
 out=[]
 for x in rows:
  title=" ".join(str(x.get(k,"")) for k in ("table_name","description","file_name")).lower()
  if any(t in title for t in terms) and all(x.get(k) for k in ("file_path","file_name","unique_id")): out.append(x)
 return sorted(out,key=lambda x:(str(x.get("release_date","")),str(x.get("ref_period",""))),reverse=True)
def workbook(p):
 xl=pd.ExcelFile(p); result=[]
 for n in xl.sheet_names:
  d=pd.read_excel(p,sheet_name=n,header=None,dtype=object)
  result.append({"sheet":n,"rows":len(d),"columns":len(d.columns),"nonempty_cells":int(d.notna().sum().sum()),"preview":[str(v)[:100] for v in d.iloc[0].tolist()[:12]] if len(d) else []})
 return result
def capture_page(s,key,sp,folder):
 r=get(s,sp["url"]); (folder/(key+"_landing.html")).write_bytes(r.content)
 tree=HTMLParser(r.text); links=[]
 for a in tree.css("a[href]"):
  h=a.attributes.get("href",""); label=" ".join(a.text().split())
  candidate=urljoin(r.url,h) if h else ""
  is_sheet=bool(re.search(r"\.(xlsx?|xlsm)(?:$|\?)",candidate,re.I))
  relevant=any(t in (label+" "+h).lower() for t in sp["terms"]) or (key=="government_capex" and is_sheet)
  if h and relevant: links.append({"label":label,"url":candidate})
 files=[]
 for a in links[:8]:
  if not re.search(r"\.(?:xlsx?|xlsm)(?:$|\?)",a["url"],re.I): continue
  try:
   f=get(s,a["url"])
   if not (f.content.startswith(b"PK") or f.content.startswith(b"\xd0\xcf\x11\xe0")): continue
   name=key+"_"+Path(a["url"].split("?")[0]).name;p=folder/name;p.write_bytes(f.content)
   files.append({"label":a["label"],"url":f.url,"file":name,"bytes":len(f.content),"sha256":sha(f.content),"sheets":workbook(p)})
  except Exception as e: files.append({"url":a["url"],"error":f"{type(e).__name__}: {str(e)[:180]}"})
 tables=[]
 try:
  for i,frame in enumerate(pd.read_html(StringIO(r.text))):
   name=f"{key}_release_table_{i+1:02d}.csv"; target=folder/name
   frame.to_csv(target,index=False)
   tables.append({"file":name,"rows":len(frame),"columns":len(frame.columns),"sha256":sha(target.read_bytes()),"headers":[str(c) for c in frame.columns]})
 except (ValueError,ImportError):
  pass
 page_text=tree.text(separator=" ")
 posted=re.search(r"(?:Posted On|Dated)\s*:\s*(.{1,100}?)(?:\s+by\s+PIB|$)",page_text,re.I)
 return {"http_status":r.status_code,"landing_url":r.url,"landing_sha256":sha(r.content),"release_timestamp_text":posted.group(1).strip() if posted else None,"catalogue_url":sp.get("catalogue_url"),"candidate_links":links[:30],"captured_files":files,"release_tables":tables}
def main():
 RAW.mkdir(parents=True,exist_ok=True);OUT.mkdir(parents=True,exist_ok=True);s=requests.Session()
 report={"schema_version":"1.0","observed_at_utc":datetime.now(timezone.utc).isoformat(),"sources":{}}
 for key,sp in SOURCES.items():
  folder=RAW/key;folder.mkdir(parents=True,exist_ok=True)
  x={"provider":sp["provider"],"landing_url":sp["url"],"expected_frequency":sp["frequency"],"unit_contract":sp["unit"],"observed_at_utc":datetime.now(timezone.utc).isoformat(),"rows":0,"status":"BLOCKED"}
  try:
   if sp.get("product"):
    rows,pag=catalogue(s,sp["product"]); matches=select(rows,sp["terms"])
    if not matches: raise ValueError("no matching catalogue dataset with official file identity")
    x["pagination"]=pag;x["vintages"]=[]
    for rec in matches[:3]:
     url=DOWNLOAD+quote(str(rec["file_path"]).lstrip("/") + str(rec["file_name"]),safe="/");r=get(s,url)
     if not (r.content.startswith(b"PK") or r.content.startswith(b"\xd0\xcf\x11\xe0")): raise ValueError("download is not an Excel container")
     p=folder/str(rec["file_name"]);p.write_bytes(r.content)
     x["vintages"].append({"table_id":rec["unique_id"],"table_name":rec.get("table_name"),"reference_period":rec.get("ref_period"),"release_date":rec.get("release_date"),"frequency":rec.get("frequency"),"file_name":rec["file_name"],"file_path":rec["file_path"],"download_url":r.url,"bytes":len(r.content),"sha256":sha(r.content),"sheets":workbook(p)})
    x["status"]="RAW_OFFICIAL_VINTAGES_CAPTURED_NORMALIZATION_PENDING"
    x["reason"]="Catalogue and workbook vintages captured; source-specific numeric parser, release-time alignment and revision-aware normalized panel remain unapproved."
   else:
    x.update(capture_page(s,key,sp,folder))
    x["status"]="RAW_OFFICIAL_RELEASE_TABLES_CAPTURED_NORMALIZATION_PENDING" if x.get("release_tables") else ("RAW_OFFICIAL_RELEASES_CAPTURED_NORMALIZATION_PENDING" if x["captured_files"] else "OFFICIAL_LANDING_PAGE_CAPTURED_SCHEMA_PENDING")
    x["reason"]="Landing page and candidate official downloads inspected; normalized observation schema and publication-time contract remain pending."
   if key=="pmi":
    x["status"]="PUBLISHER_PRIMARY_PUBLIC_HEADLINE_ONLY"
    x["reason"]="S&P Global is the primary survey publisher, not a Government of India statistical agency; public headlines do not provide licensed underlying history."
  except Exception as e: x["error"]=f"{type(e).__name__}: {str(e)[:350]}"
  report["sources"][key]=x
  print(json.dumps({"source":key,"status":x["status"],"vintages":len(x.get("vintages",[])),"files":len(x.get("captured_files",[]))}))
 report["status"]="SOURCE_ACQUISITION_AUDITED_WITH_NORMALIZATION_GAPS";report["as_of_utc"]=datetime.now(timezone.utc).isoformat()
 covpath=OUT/"source_coverage.json"
 if covpath.exists():
  cov=json.loads(covpath.read_text()); srcs=cov.setdefault("sources",[])
  for name in ("macro_indicators","government_capex"):
   row=next((v for v in srcs if isinstance(v,dict) and v.get("source")==name),None)
   if row is None: row={"source":name};srcs.append(row)
   row.update({"status":"DATA_QUALITY_WARN","rows":0,"observed_rows":0,"evidence_path":"outputs/macro_geo/india_macro_series_source_audit.json","reason":"Official source releases captured in this exact run, but normalized observations/release-vintage schema QA is not yet complete; remain UNKNOWN."})
  cov["macro_series_source_audit_as_of_utc"]=report["as_of_utc"]
  covpath.write_text(json.dumps(cov,ensure_ascii=False,indent=2)+"\\n")
 p=OUT/"india_macro_series_source_audit.json";p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 (OUT/"india_macro_series_source_audit.sha256").write_text(sha(p.read_bytes())+"  "+p.name+"\n")
 print(json.dumps({"status":report["status"],"sources":{k:v["status"] for k,v in report["sources"].items()}},indent=2))
if __name__=="__main__": main()
