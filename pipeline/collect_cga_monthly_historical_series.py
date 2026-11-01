#!/usr/bin/env python3
"""Extract official CGA dashboard cumulative and derived monthly series with vintage limits."""
import csv,hashlib,json,re,ssl,urllib.request
from pathlib import Path
from datetime import datetime,timezone
from openpyxl import load_workbook
from html.parser import HTMLParser
OUT=Path("artifacts/cga_monthly_historical_series")
PAGE="https://cga.gov.in/MonthDashboardReport/Published/list.aspx"
FILE="https://cga.gov.in/writereaddata/MonthAccount/MonthAccountDashboard/DAMA%20dashboard%20February%202026%20Data%20file22026.xlsm"
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-CGA-Historical-Series/1.0)"
MONTHS={m:i for i,m in enumerate(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],1)}
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,d):
  if d.strip():self.parts.append(" ".join(d.split()))
def fetch(url):
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"*/*"})
 with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl.create_default_context())).open(req,timeout=45) as r:
  b=r.read(90_000_000);return b,{"status":r.status,"final_url":r.geturl(),"content_type":r.headers.get("Content-Type",""),"bytes":len(b)}
def sha(b):return hashlib.sha256(b).hexdigest()
def period(fy,mon):
 m=re.fullmatch(r"([A-Za-z]{3})-(\d{2})",str(mon).strip())
 if not m:raise ValueError("Invalid month label "+str(mon))
 month=MONTHS[m.group(1).title()]
 year=2000+int(m.group(2))
 fy0=int(str(fy)[:4])
 if (month>=4 and year!=fy0) or (month<4 and year!=fy0+1):
  raise ValueError(f"FY/month mismatch {fy}/{mon}")
 return f"{year:04d}-{month:02d}",month
def main():
 OUT.mkdir(parents=True,exist_ok=True);retrieved=datetime.now(timezone.utc).isoformat()
 page,pm=fetch(PAGE);parser=Text();parser.feed(page.decode("utf-8-sig",errors="replace"));pt=" ".join(parser.parts)
 if "Monthly Accounts Dashboard upto February 2026" not in pt:raise RuntimeError("Official CGA publication page does not identify Feb-2026 workbook")
 wbraw,wm=fetch(FILE)
 if not wbraw.startswith(b"PK"):raise RuntimeError("CGA workbook is not valid OOXML XLSM")
 raw=OUT/"CGA_Monthly_Accounts_Dashboard_February_2026.xlsm";raw.write_bytes(wbraw)
 wb=load_workbook(raw,read_only=True,data_only=True,keep_vba=False)
 exports={};summaries={};all_errors=[]
 for sheet in ["actual","actual2"]:
  if sheet not in wb.sheetnames:raise RuntimeError("Missing required data sheet "+sheet)
  ws=wb[sheet];it=ws.iter_rows(values_only=True);header=next(it)
  cols=[str(x).strip() if x is not None else "" for x in header]
  keyrows={};duplicates=[]
  for row in it:
   if len(row)<2 or not re.fullmatch(r"\d{4}-\d{2}",str(row[0] or "")):continue
   if not re.fullmatch(r"[A-Za-z]{3}-\d{2}",str(row[1] or "")):continue
   key=(str(row[0]),str(row[1]))
   if key in keyrows:
    if tuple(row)==keyrows[key]:duplicates.append({"key":key,"type":"identical_duplicate"})
    else:raise RuntimeError(f"Conflicting duplicate {sheet} {key}")
   else:keyrows[key]=tuple(row)
  ordered=[]
  for (fy,mon),row in keyrows.items():
   p,month=period(fy,mon);ordered.append((p,fy,mon,month,row))
  ordered.sort(key=lambda x:x[0])
  if not ordered:raise RuntimeError("No monthly rows in "+sheet)
  periods=[x[0] for x in ordered]
  if len(periods)!=len(set(periods)):raise RuntimeError("Duplicate normalized month in "+sheet)
  expected=[];start=periods[0]
  from datetime import date
  y,m=map(int,start.split("-"))
  while (y,m)<=(int(periods[-1][:4]),int(periods[-1][5:])):
   expected.append(f"{y:04d}-{m:02d}");m+=1
   if m==13:y+=1;m=1
  missing=sorted(set(expected)-set(periods))
  if missing:raise RuntimeError(f"Missing monthly periods in {sheet}: {missing}")
  output=[];prev_by_fy={}
  for p,fy,mon,month,row in ordered:
   rec={"financial_year":fy,"period":p,"month_label":mon,"vintage_workbook":"February 2026 dashboard"}
   for idx,name in enumerate(cols):
    if idx<2 or not name:continue
    val=row[idx] if idx<len(row) else None
    if isinstance(val,(int,float)) and not isinstance(val,bool):
     rec[name+"_cumulative"]=val
     prev=prev_by_fy.get(fy,{}).get(name)
     rec[name+"_monthly_derived"]=val if month==4 or prev is None else val-prev
     prev_by_fy.setdefault(fy,{})[name]=val
    else:
     rec[name+"_cumulative"]="" if val is None else str(val)
     rec[name+"_monthly_derived"]=""
     if val is not None:prev_by_fy.setdefault(fy,{}).pop(name,None)
   output.append(rec)
  csvpath=OUT/(sheet+"_cumulative_and_monthly.csv")
  with csvpath.open("w",newline="",encoding="utf-8") as f:
   w=csv.DictWriter(f,fieldnames=list(output[0]));w.writeheader();w.writerows(output)
  exports[sheet]=csvpath.name
  summaries[sheet]={"unique_months":len(output),"first_period":periods[0],"last_period":periods[-1],
   "duplicate_identical_rows_removed":len(duplicates),"missing_periods":missing,
   "columns":cols,"csv_sha256":sha(csvpath.read_bytes())}
 wb.close()
 page_text=pt.upper()
 last_update=re.search(r"LAST UPDATED DATE\s*:\s*(\d{1,2}\s+[A-Z]{3}\s+\d{4})",page_text)
 qa={"status":"PASS_BOUNDED_HISTORICAL_EXTRACTION","publisher":"Controller General of Accounts, Ministry of Finance",
  "dataset_reference_period":"April 2014 to February 2026","workbook_label":"Monthly Accounts Dashboard upto February 2026",
  "workbook_publication_date":"NOT_STATED_ON_SOURCE_PAGE","source_page_last_updated_date":last_update.group(1) if last_update else None,
  "vintage_status":"VINTAGE_UNVERIFIED_SINGLE_LATEST_SNAPSHOT",
  "sheets":summaries,"limitations":["The dashboard provides cumulative year-to-date actuals; monthly standalone values are derived by differencing within each financial year.",
   "This is one latest dashboard snapshot, not a historical archive of publication vintages or revision snapshots.",
   "CGA source page last-updated date is not treated as workbook publication timestamp.",
   "CGA disclaimer states data may be updated, corrected and revised; historical vintages remain unverified."]}
 manifest={"retrieved_at_utc":retrieved,"source_page_url":PAGE,"source_page_http":pm,"source_page_sha256":sha(page),
  "workbook_url":FILE,"workbook_http":wm,"workbook_sha256":sha(wbraw),"raw_file":raw.name,
  "qa_status":qa["status"],"exports":exports}
 (OUT/"domain_qa.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n")
 (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"status":qa["status"],"sheets":{k:{x:v[x] for x in ["unique_months","first_period","last_period","duplicate_identical_rows_removed"]} for k,v in summaries.items()},"vintage_status":qa["vintage_status"],"source_page_last_updated_date":qa["source_page_last_updated_date"],"sha256":manifest["workbook_sha256"]},indent=2))
if __name__=="__main__":main()
