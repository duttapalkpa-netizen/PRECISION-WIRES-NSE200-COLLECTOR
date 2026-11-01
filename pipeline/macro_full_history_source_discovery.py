#!/usr/bin/env python3
"""Official macro full-history source discovery; inventory only, no registry promotion."""
# PRODUCTION_SELECTOR, RANKING_SCORE, +1 PRESSURE_FADE, 672 diagnostics and UNKNOWN/NOT_CONNECTED classifications remain immutable.
import json,hashlib,ssl,urllib.request,urllib.parse,re
from pathlib import Path
from datetime import datetime,timezone
from html.parser import HTMLParser
from openpyxl import load_workbook
OUT=Path("artifacts/macro_full_history_discovery")
UA="Mozilla/5.0 (compatible; PRECISION-WIRES-Macro-History-Discovery/1.0)"
def get(url,limit=60000000):
 # Preserve TLS certificate and hostname verification. MoSPI public API needs the
 # same legacy TLS cipher compatibility already validated in the GDP collector.
 ctx=ssl.create_default_context()
 if "api.mospi.gov.in" in url:
  ctx.set_ciphers("DEFAULT:@SECLEVEL=1");ctx.options |= 0x4
 req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"*/*","Origin":"https://esankhyiki.mospi.gov.in","Referer":"https://esankhyiki.mospi.gov.in/catalogue-main/catalogue"})
 with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx)).open(req,timeout=45) as r:
  b=r.read(limit);return b,{"status":r.status,"content_type":r.headers.get("Content-Type",""),"final_url":r.geturl(),"bytes":len(b)}
def sha(b):return hashlib.sha256(b).hexdigest()
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.href=None;self.text=[]
 def handle_starttag(self,t,a):
  if t=="a":
   d=dict(a);self.href=d.get("href");self.text=[]
 def handle_data(self,d):
  if self.href is not None:self.text.append(d.strip())
 def handle_endtag(self,t):
  if t=="a" and self.href is not None:
   self.links.append({"href":self.href,"text":" ".join(x for x in self.text if x)});self.href=None;self.text=[]
def wpi():
 url="https://eaindustry.nic.in/download_data_2223.asp"
 try:
  b,m=get(url,20000000)
 except Exception as first:
  fallback="https://www.eaindustry.nic.in/download_data_2223.asp"
  try:b,m=get(fallback,20000000);url=fallback
  except Exception as second:
   return {"status":"SOURCE_TRANSPORT_BLOCKED","url":url,"fallback_url":fallback,
    "error":str(second),"primary_error":str(first),"links":[],"link_count":0}
 (OUT/"oea_download_data_2223.html").write_bytes(b)
 p=Links();p.feed(b.decode("utf-8-sig",errors="replace"))
 links=[]
 for x in p.links:
  href=urllib.parse.urljoin(url,x["href"])
  if re.search(r"\.(xlsx?|csv|zip|xlsm)(?:[?#]|$)",href,re.I) or any(k in (x["text"]+" "+href).lower() for k in ["download","item","wpi","index"]):
   if href.startswith("https://eaindustry.nic.in/"):links.append({**x,"absolute_url":href})
 return {"status":m["status"],"url":m["final_url"],"bytes":m["bytes"],"sha256":sha(b),"links":links,"link_count":len(links)}
def cga():
 url="https://cga.gov.in/writereaddata/MonthAccount/MonthAccountDashboard/DAMA%20dashboard%20February%202026%20Data%20file22026.xlsm"
 b,m=get(url,80000000);raw=OUT/"CGA_Monthly_Accounts_Dashboard_February_2026.xlsm";raw.write_bytes(b)
 if not b.startswith(b"PK"):raise RuntimeError("CGA dashboard is not a valid OOXML XLSM ZIP file")
 wb=load_workbook(raw,read_only=True,data_only=True,keep_vba=False)
 sheets=[];fy=[];months=set();numeric=0
 for ws in wb.worksheets:
  sample=[];nn=0;nonempty=0;maxrow=0;maxcol=0
  for ri,row in enumerate(ws.iter_rows(),1):
   vals=[c.value for c in row]
   if any(v is not None for v in vals):
    nonempty+=sum(v is not None for v in vals);maxrow=ri;maxcol=max(maxcol,len(vals))
   for v in vals:
    if isinstance(v,(int,float)) and not isinstance(v,bool):nn+=1
    if isinstance(v,str):
     s=v.strip()
     if re.search(r"20\d{2}[-–]20\d{2}",s):fy.append(s)
     if re.search(r"^(April|May|June|July|August|September|October|November|December|January|February|March)$",s,re.I):months.add(s.title())
   if len(sample)<16 and any(v is not None for v in vals):sample.append([str(v) if v is not None else None for v in vals[:16]])
  numeric+=nn;sheets.append({"sheet":ws.title,"max_row":maxrow,"max_col":maxcol,"nonempty_cells":nonempty,"numeric_cells":nn,"sample_rows":sample})
 wb.close()
 return {"status":m["status"],"url":m["final_url"],"bytes":m["bytes"],"sha256":sha(b),"format":"OLE/Excel macro-enabled","sheet_count":len(sheets),"numeric_cells":numeric,"financial_year_tokens":sorted(set(fy)),"month_tokens":sorted(months),"sheets":sheets}
def mospi(product):
 api="https://api.mospi.gov.in/api/esankhyiki/cms/golden-sheet/list"
 allrows=[];page=1;limit=100;pages=[]
 while page<=100:
  url=api+"?"+urllib.parse.urlencode({"product":product,"page":page,"limit":limit})
  b,m=get(url,20000000);p=json.loads(b.decode("utf-8-sig"));rows=p.get("data") or [];meta=p.get("meta_data") or {}
  pages.append({"page":page,"rows":len(rows),"sha256":sha(b),"status":m["status"]})
  allrows.extend(rows)
  total=int(meta.get("totalPages") or 0)
  if not rows or (total and page>=total):break
  page+=1
 if page>100:raise RuntimeError(product+" catalogue exceeded 100 pages safety cap")
 filtered=[]
 for r in allrows:
  title=str(r.get("table_name","")).lower()
  if product=="NAS" and any(k in title for k in ["gdp","gross domestic","gross value added","national income","expenditure","capital formation"]):
   filtered.append({k:r.get(k) for k in ["unique_id","product","table_name","ref_period","release_date","file_path","file_name"]})
  if product=="CPI":
   filtered.append({k:r.get(k) for k in ["unique_id","product","table_name","ref_period","release_date","file_path","file_name"]})
 return {"product":product,"catalogue_records":len(allrows),"pages":pages,"filtered_records":filtered}
def main():
 OUT.mkdir(parents=True,exist_ok=True);retrieved=datetime.now(timezone.utc).isoformat()
 result={"retrieved_at_utc":retrieved,"sources":{}}
 result["sources"]["oea_wpi"]=wpi()
 result["sources"]["cga_dashboard"]=cga()
 result["sources"]["mospi_nas"]=mospi("NAS")
 result["sources"]["mospi_cpi"]=mospi("CPI")
 (OUT/"source_inventory.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+chr(10))
 print(json.dumps({"status":"DISCOVERY_COMPLETE","retrieved_at_utc":retrieved,
  "oea_download_links":result["sources"]["oea_wpi"]["link_count"],\n  "oea_status":result["sources"]["oea_wpi"]["status"],
  "cga_sheets":result["sources"]["cga_dashboard"]["sheet_count"],
  "cga_numeric_cells":result["sources"]["cga_dashboard"]["numeric_cells"],
  "nas_catalogue_records":result["sources"]["mospi_nas"]["catalogue_records"],
  "nas_gdp_related_tables":len(result["sources"]["mospi_nas"]["filtered_records"]),
  "cpi_catalogue_records":result["sources"]["mospi_cpi"]["catalogue_records"]},indent=2))
if __name__=="__main__":main()
