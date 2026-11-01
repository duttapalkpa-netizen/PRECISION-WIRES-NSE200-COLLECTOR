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

def published_utc(text):
 if not text: return None
 value=pd.to_datetime(text,errors="coerce")
 if pd.isna(value): return None
 return value.tz_localize("Asia/Kolkata").tz_convert("UTC").isoformat()

def normalize_release_observations(report):
 rows=[]; qa={"sources":{}}
 # GDP: two directly stated quarterly headline measures and their comparator/growth.
 g=report["sources"].get("gdp",{})
 gp=RAW/"gdp"/"gdp_landing.html"
 if gp.exists():
  raw=gp.read_text(encoding="utf-8",errors="replace")
  plain=re.sub(r"<[^>]+>"," ",raw)
  plain=__import__("html").unescape(plain)
  pub=published_utc(g.get("release_timestamp_text"))
  for label,pattern in [
   ("REAL_GDP_CONSTANT_PRICE",r"Real GDP or GDP at Constant Prices.*?₹\s*([\d.]+)\s*lakh crore.*?₹\s*([\d.]+)\s*lakh crore.*?growth rate of ([\d.]+)%"),
   ("NOMINAL_GDP_CURRENT_PRICE",r"Nominal GDP or GDP at Current Prices.*?₹\s*([\d.]+)\s*lakh crore.*?₹\s*([\d.]+)\s*lakh crore.*?growth rate of ([\d.]+)%")]:
   m=re.search(pattern,plain,re.I|re.S)
   if m:
    current,prior,growth=map(float,m.groups())
    for period,val in [("2026-Q1",current),("2025-Q1",prior)]:
     rows.append({"source_group":"macro_indicators","series":label,"period":period,"dimension":"ALL_INDIA","value":val,"unit":"INR_LAKH_CRORE","vintage":"OFFICIAL_RELEASE","published_at_utc":pub,"source_url":g["landing_url"],"source_sha256":g.get("landing_sha256"),"release_status":"PUBLISHED"})
    rows.append({"source_group":"macro_indicators","series":label+"_YOY_GROWTH","period":"2026-Q1","dimension":"ALL_INDIA","value":growth,"unit":"PERCENT","vintage":"OFFICIAL_RELEASE","published_at_utc":pub,"source_url":g["landing_url"],"source_sha256":g.get("landing_sha256"),"release_status":"PUBLISHED"})
  qa["sources"]["gdp"]={"status":"PARTIAL_NORMALIZED_RELEASE_WINDOW" if any(x["series"].startswith(("REAL_GDP","NOMINAL_GDP")) for x in rows) else "SCHEMA_PENDING","rows":sum(x["series"].startswith(("REAL_GDP","NOMINAL_GDP")) for x in rows),"coverage_limit":"Latest Q1 headline only; complete quarterly NAS time series not yet ingested"}
 # CPI: normalize the national table by month, rural/urban/combined and CPI/CFPI measure.
 c=report["sources"].get("cpi",{}); cpi_rows=[]
 for item in c.get("release_tables",[]):
  if item.get("file")!="cpi_release_table_02.csv": continue
  p=RAW/"cpi"/item["file"]
  if not p.exists(): continue
  d=pd.read_csv(p,header=None,dtype=object)
  if len(d)<5 or d.shape[1]<8: continue
  for i in range(4,len(d)):
   measure=str(d.iloc[i,0]).strip(); indicator=str(d.iloc[i,1]).strip()
   if measure not in {"Inflation (%)","Index"} or indicator not in {"CPI (General)","CFPI"}: continue
   for j in range(2,8):
    heading=str(d.iloc[1,j]); geo=str(d.iloc[3,j]).strip()
    m=re.match(r"([A-Za-z]+),\s*(\d{4})\s*\((Final|Provisional)\)",heading)
    val=pd.to_numeric(pd.Series([d.iloc[i,j]]),errors="coerce").iloc[0]
    if not m or pd.isna(val) or geo not in {"Rural","Urban","Combined"}: continue
    period=pd.to_datetime(f"{m.group(1)} 1 {m.group(2)}").strftime("%Y-%m")
    cpi_rows.append({"source_group":"macro_indicators","series":indicator+("_INFLATION" if measure=="Inflation (%)" else "_INDEX"),"period":period,"dimension":geo,"value":float(val),"unit":"PERCENT" if measure=="Inflation (%)" else "INDEX_2024_100","vintage":m.group(3).upper(),"published_at_utc":published_utc(c.get("release_timestamp_text")),"source_url":c.get("landing_url"),"source_sha256":c.get("landing_sha256"),"release_status":m.group(3).upper()})
 rows.extend(cpi_rows)
 qa["sources"]["cpi"]={"status":"PARTIAL_NORMALIZED_RELEASE_WINDOW" if cpi_rows else "SCHEMA_PENDING","rows":len(cpi_rows),"coverage_limit":"Latest two national months only; full catalogue monthly history and item/state dimensions pending"}
 # WPI: monthly index and YoY tables, retaining provisional/final vintage flags.
 w=report["sources"].get("wpi",{}); wpi_rows=[]
 for item in w.get("release_tables",[]):
  if item.get("file") not in {"wpi_release_table_01.csv","wpi_release_table_02.csv"}: continue
  p=RAW/"wpi"/item["file"]
  if not p.exists(): continue
  d=pd.read_csv(p)
  measure="WPI_INDEX" if item["file"].endswith("01.csv") else "WPI_YOY_INFLATION"
  for _,row in d.iterrows():
   group=str(row.iloc[0]).strip()
   for col in d.columns[2:]:
    m=re.match(r"([A-Za-z]{3})-(\d{2})\s*\(([FP])\)",str(col).strip())
    val=pd.to_numeric(pd.Series([row[col]]),errors="coerce").iloc[0]
    if not m or pd.isna(val): continue
    month=pd.to_datetime(f"{m.group(1)} 1 20{m.group(2)}").strftime("%Y-%m")
    wpi_rows.append({"source_group":"macro_indicators","series":measure,"period":month,"dimension":group,"value":float(val),"unit":"INDEX_2022_23_100" if measure=="WPI_INDEX" else "PERCENT","vintage":"PROVISIONAL" if m.group(3)=="P" else "FINAL","published_at_utc":published_utc(w.get("release_timestamp_text")),"source_url":w.get("landing_url"),"source_sha256":w.get("landing_sha256"),"release_status":"PROVISIONAL" if m.group(3)=="P" else "FINAL"})
 rows.extend(wpi_rows)
 qa["sources"]["wpi"]={"status":"PARTIAL_NORMALIZED_RELEASE_WINDOW" if wpi_rows else "SCHEMA_PENDING","rows":len(wpi_rows),"coverage_limit":"Latest six months of group-wise release tables; complete Apr-2023 onward OEA index file pending"}
 # CGA: monthly actual expenditure observations from the official macro-enabled workbook.
 cg=report["sources"].get("government_capex",{}); capex_rows=[]
 for item in cg.get("captured_files",[]):
  name=item.get("file")
  if not name: continue
  p=RAW/"government_capex"/name
  if not p.exists(): continue
  d=pd.read_excel(p,sheet_name="actual")
  needed={"FY","Month","Capital Expenditure"}
  if not needed.issubset(set(d.columns)): continue
  for _,row in d.iterrows():
   dt=pd.to_datetime(str(row.get("Month","")),format="%b-%y",errors="coerce")
   val=pd.to_numeric(pd.Series([row.get("Capital Expenditure")]),errors="coerce").iloc[0]
   if pd.isna(dt) or pd.isna(val): continue
   capex_rows.append({"source_group":"government_capex","series":"UNION_GOVT_CAPITAL_EXPENDITURE_CUMULATIVE","period":dt.strftime("%Y-%m"),"dimension":"ACTUAL_CUMULATIVE_FY","value":float(val),"unit":"INR_CRORE","vintage":"ACTUAL_PROVISIONAL","published_at_utc":None,"source_url":item.get("url"),"source_sha256":item.get("sha256"),"release_status":"PUBLICATION_TIMESTAMP_UNVERIFIED"})
 rows.extend(capex_rows)
 qa["sources"]["government_capex"]={"status":"OBSERVATIONS_NORMALIZED_PUBLICATION_TIMESTAMP_PENDING" if capex_rows else "SCHEMA_PENDING","rows":len(capex_rows),"coverage_limit":"CGA workbook monthly actuals through Feb-2026; public page capture time is not a verified release timestamp"}
 # PMI stays excluded until licensed source observations are available.
 qa["sources"]["pmi"]={"status":"PUBLIC_HEADLINE_ONLY_LICENSE_REQUIRED","rows":0,"coverage_limit":"Underlying survey time series not publicly downloadable from the publisher endpoint"}
 frame=pd.DataFrame(rows)
 if not frame.empty:
  key=["source_group","series","period","dimension","unit"]
  frame=frame.drop_duplicates(subset=key+["value","vintage","source_sha256"],keep="first")
  if frame.duplicated(key).any(): raise ValueError("Conflicting normalized macro observation keys detected")
  if frame["value"].isna().any() or not pd.to_numeric(frame["value"],errors="coerce").notna().all(): raise ValueError("Normalized macro values contain missing/non-numeric observations")
  frame=frame.sort_values(["source_group","series","period","dimension"]).reset_index(drop=True)
  frame.to_csv(Path("data/external/macro_series_observations.csv"),index=False)
  qa["total_observations"]=len(frame);qa["duplicate_keys"]=int(frame.duplicated(key).sum());qa["sha256"]=sha(Path("data/external/macro_series_observations.csv").read_bytes())
 else:
  qa["total_observations"]=0;qa["duplicate_keys"]=0
 # Canonical macro registry adapter: only observations with a genuine
 # source publication timestamp are promoted. Period date is never RELEASED_AT.
 macro=frame[frame["source_group"].eq("macro_indicators")].copy() if not frame.empty else pd.DataFrame()
 if not macro.empty:
  def period_date(value):
   value=str(value)
   m=re.fullmatch(r"(\\d{4})-Q([1-4])",value)
   if m:
    return (pd.Timestamp(year=int(m.group(1)),month=1,day=1)+pd.DateOffset(months=(int(m.group(2))-1)*3)).strftime("%Y-%m-%d")
   return pd.to_datetime(value+"-01" if re.fullmatch(r"\\d{4}-\\d{2}",value) else value,errors="coerce").strftime("%Y-%m-%d")
  macro["DATE"]=macro["period"].map(period_date)
  macro["INDICATOR"]=macro["series"].astype(str)+"|"+macro["dimension"].astype(str)
  macro["VALUE"]=pd.to_numeric(macro["value"],errors="coerce")
  macro["RELEASED_AT"]=pd.to_datetime(macro["published_at_utc"],errors="coerce",utc=True)
  macro["SOURCE"]=macro["source_url"].map(lambda u:"MoSPI/PIB official release" if "pib.gov.in" in str(u) else "Official statistical source")
  macro["SOURCE_URL"]=macro["source_url"];macro["OBSERVED_AT_UTC"]=report.get("observed_at_utc")
  macro["UNIT"]=macro["unit"];macro["PERIOD"]=macro["period"];macro["VINTAGE"]=macro["vintage"]
  macro["SOURCE_SHA256"]=macro["source_sha256"];macro["RELEASE_STATUS"]=macro["release_status"]
  macro=macro.dropna(subset=["DATE","VALUE","RELEASED_AT","SOURCE_URL"])
  macro_path=Path("data/external/macro_indicators.csv")
  macro[["DATE","INDICATOR","VALUE","RELEASED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC","UNIT","PERIOD","VINTAGE","SOURCE_SHA256","RELEASE_STATUS"]].to_csv(macro_path,index=False)
  qa["registry_macro_rows"]=int(len(macro));qa["registry_macro_sha256"]=sha(macro_path.read_bytes())
 else: qa["registry_macro_rows"]=0
 # Capex is normalized separately, but release time remains unknown and is
 # intentionally not inferred from retrieval time or HTTP metadata.
 capex=frame[frame["source_group"].eq("government_capex")].copy() if not frame.empty else pd.DataFrame()
 if not capex.empty:
  capex["DATE"]=capex["period"].astype(str)+"-01";capex["DEPARTMENT"]="UNION_GOVERNMENT"
  capex["ACTUAL_SPEND"]=pd.to_numeric(capex["value"],errors="coerce");capex["BUDGET_SPEND"]=pd.NA
  capex["RELEASED_AT"]=pd.NA;capex["SOURCE_URL"]=capex["source_url"]
  capex["SOURCE"]="Controller General of Accounts";capex["OBSERVED_AT_UTC"]=report.get("observed_at_utc")
  Path("data/external/government_capex.csv").parent.mkdir(parents=True,exist_ok=True)
  capex[["DATE","DEPARTMENT","ACTUAL_SPEND","BUDGET_SPEND","RELEASED_AT","SOURCE_URL","SOURCE","OBSERVED_AT_UTC","unit","vintage","source_sha256"]].to_csv("data/external/government_capex.csv",index=False)
 qa["status"]="NORMALIZED_PARTIAL_SERIES_WITH_PROVENANCE_LIMITS"
 OUT.mkdir(parents=True,exist_ok=True)
 (OUT/"macro_series_observation_qa.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n")
 for key,item in qa["sources"].items():
  if key in report["sources"]:
   report["sources"][key]["normalized_status"]=item["status"]
   report["sources"][key]["normalized_rows"]=item["rows"]
   report["sources"][key]["coverage_limit"]=item["coverage_limit"]
   report["sources"][key]["status"]=item["status"]
 report["normalized_observation_qa"]=qa

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
 normalize_release_observations(report)
 covpath=OUT/"source_coverage.json"
 if covpath.exists():
  cov=json.loads(covpath.read_text()); srcs=cov.setdefault("sources",[])
  for name,path,rows,status,reason in [
   ("macro_indicators","data/external/macro_indicators.csv",int(qa.get("registry_macro_rows",0)),"AVAILABLE" if int(qa.get("registry_macro_rows",0))>0 else "DATA_QUALITY_WARN","Only source-published GDP/CPI/WPI observations with publication timestamps are promoted; historical completeness remains partial."),
   ("government_capex","data/external/government_capex.csv",int(qa["sources"]["government_capex"]["rows"]),"DATA_QUALITY_WARN","CGA actual observations captured, but publication timestamp and complete point-in-time release vintage are unverified.")
  ]:
   row=next((v for v in srcs if isinstance(v,dict) and v.get("source")==name),None)
   if row is None: row={"source":name};srcs.append(row)
   row.update({"status":status,"rows":rows,"observed_rows":rows,"selected_path":path if rows else "","evidence_path":"outputs/macro_geo/macro_series_observation_qa.json","reason":reason})
  cov["sources_total"]=len(srcs)
  cov["available"]=sum(1 for x in srcs if x.get("status") in ("AVAILABLE","AVAILABLE_SECONDARY") and int(x.get("rows",0) or 0)>0)
  cov["not_connected"]=sum(1 for x in srcs if x.get("status")=="NOT_CONNECTED")
  cov["quality_warn"]=sum(1 for x in srcs if x.get("status")=="DATA_QUALITY_WARN")
  cov["p0_source_coverage_as_of_utc"]=cov.get("as_of_utc")
  cov["as_of_utc"]=report["as_of_utc"]
  cov["macro_series_source_audit_as_of_utc"]=report["as_of_utc"]
  csvpath=OUT/"source_coverage.csv"
  if csvpath.exists():
   cdf=pd.read_csv(csvpath)
   for name,path,rows,status,reason in [
    ("macro_indicators","data/external/macro_indicators.csv",int(qa.get("registry_macro_rows",0)),"AVAILABLE" if int(qa.get("registry_macro_rows",0))>0 else "DATA_QUALITY_WARN","Published GDP/CPI/WPI observations; historical completeness partial."),
    ("government_capex","data/external/government_capex.csv",int(qa["sources"]["government_capex"]["rows"]),"DATA_QUALITY_WARN","CGA publication timestamp unverified; remains UNKNOWN.")
   ]:
    if name in set(cdf["source"].astype(str)):
     cdf.loc[cdf["source"].astype(str).eq(name),"status"]=status
     cdf.loc[cdf["source"].astype(str).eq(name),"selected_path"]=path if rows else ""
     cdf.loc[cdf["source"].astype(str).eq(name),"rows"]=rows
     cdf.loc[cdf["source"].astype(str).eq(name),"notes"]=reason
   cdf.to_csv(csvpath,index=False)
  covpath.write_text(json.dumps(cov,ensure_ascii=False,indent=2)+"\n")
 p=OUT/"india_macro_series_source_audit.json";p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 (OUT/"india_macro_series_source_audit.sha256").write_text(sha(p.read_bytes())+"  "+p.name+"\n")
 print(json.dumps({"status":report["status"],"sources":{k:v["status"] for k,v in report["sources"].items()}},indent=2))
if __name__=="__main__": main()
