#!/usr/bin/env python3
"""Capture IMF BOP P_F asset/liability flows for the WEO Oct-2026 EMDE membership.

Downloads official WEO workbook and IMF BOP country codelist, requires exact
154/154 ISO3 membership mapping, then queries public IMF SDMX 3.0 data for
quarterly portfolio investment assets and liabilities in ALL reported units.
No currency conversion, aggregation, fill, or synthetic rows.
"""
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from urllib.parse import quote
import hashlib,json,csv,io,collections,zipfile
import openpyxl,xml.etree.ElementTree as ET

WEO_URL="https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx"
CL_URL="https://api.imf.org/external/sdmx/3.0/structure/codelist/IMF.STA/CL_BOP_COUNTRY/1.0.0?references=all"
BASE="https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0"
OUT=Path("imf_emde_portfolio_flows");RAW=OUT/"raw";RAW.mkdir(parents=True,exist_ok=True)
START="2015-Q1";END="2026-Q3";GROUP="G200"
def sha(b):return hashlib.sha256(b).hexdigest()
def get(url,accept,timeout=90):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-GCR-EMDE-panel/1.0","Accept":accept})
 try:
  with urlopen(req,timeout=timeout) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 return {"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,"headers":safe,"byte_count":len(body),"sha256":sha(body),"body":body}
def local(t):return t.split("}")[-1]
def main():
 provenance={}
 # WEO workbook
 wr=get(WEO_URL,"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
 (RAW/"WEOOct2026all.xlsx").write_bytes(wr["body"])
 provenance["weo_workbook"]={k:v for k,v in wr.items() if k!="body"}
 if wr["http_status"]!=200:raise SystemExit("WEO workbook HTTP failure")
 wb=openpyxl.load_workbook(io.BytesIO(wr["body"]),read_only=True,data_only=True)
 ws=wb["Country Group Composition"]
 emde=[]
 for row in ws.iter_rows(min_row=2,values_only=True):
  if row[0]==GROUP:
   emde.append({"group_code":row[0],"group_name":row[1],"country_code":str(row[3]).strip(),"country_name":str(row[4]).strip()})
 wb.close()
 if len(emde)!=154 or len({x["country_code"] for x in emde})!=154:raise SystemExit(f"WEO group membership expected 154 unique codes, got {len(emde)}")
 # BOP codelist
 cr=get(CL_URL,"application/vnd.sdmx.structure+xml, application/xml")
 (RAW/"CL_BOP_COUNTRY.xml").write_bytes(cr["body"])
 provenance["bop_country_codelist"]={k:v for k,v in cr.items() if k!="body"}
 if cr["http_status"]!=200:raise SystemExit("BOP country codelist HTTP failure")
 root=ET.fromstring(cr["body"]);codes=set()
 for cl in root.iter():
  if local(cl.tag)=="Codelist" and cl.attrib.get("id")=="CL_BOP_COUNTRY":
   for el in cl.iter():
    if local(el.tag)=="Code" and el.attrib.get("id"):codes.add(el.attrib["id"])
 missing=sorted({x["country_code"] for x in emde}-codes)
 if missing:raise SystemExit(f"WEO EMDE codes missing from BOP country codelist: {missing}")
 (OUT/"emde_membership.csv").write_text("group_code,group_name,country_code,country_name\n"+"".join(
  ",".join('"'+str(x[k]).replace('"','""')+'"' for k in ("group_code","group_name","country_code","country_name"))+"\n" for x in sorted(emde,key=lambda x:x["country_code"])),encoding="utf-8")
 countries="+".join(sorted(x["country_code"] for x in emde))
 reqs=[];all_rows=[]
 for entry in ("A_NFA_T","L_NIL_T"):
  key=countries+"."+entry+".P_F.*.Q"
  url=f"{BASE}/{key}?c%5BTIME_PERIOD%5D=ge%3A{START}&c%5BTIME_PERIOD%5D=le%3A{END}&format=csvdata"
  rr=get(url,"text/csv, */*",timeout=120)
  fn=f"EMDE_{entry}_P_F_ALL_UNITS_Q.csv";(RAW/fn).write_bytes(rr["body"])
  row={k:v for k,v in rr.items() if k!="body"};row.update({"entry":entry,"key":key,"file":"raw/"+fn})
  if rr["http_status"]!=200:row["parse_status"]="HTTP_FAIL";reqs.append(row);continue
  try:
   txt=rr["body"].decode("utf-8-sig")
   if txt.lstrip().startswith("<"):raise ValueError("non-CSV response")
   parsed=list(csv.DictReader(io.StringIO(txt)))
   obs=[]
   for x in parsed:
    val=(x.get("OBS_VALUE") or "").strip()
    if not val:continue
    period=x.get("TIME_PERIOD","")
    if not START<=period<=END:raise ValueError(f"period outside requested range: {period}")
    if x.get("INDICATOR")!="P_F" or x.get("BOP_ACCOUNTING_ENTRY")!=entry or x.get("FREQUENCY")!="Q":
     raise ValueError("response contains an unexpected dimension value")
    if x.get("COUNTRY") not in {m["country_code"] for m in emde}:raise ValueError("response contains non-WEO-EMDE country")
    obs.append(x);all_rows.append({**x,"SOURCE_FILE":fn,"SOURCE_SHA256":rr["sha256"]})
   row["parse_status"]="PASS";row["raw_csv_rows"]=len(parsed);row["nonempty_observations"]=len(obs)
   row["empty_rows"]=len(parsed)-len(obs);row["country_count"]=len({x["COUNTRY"] for x in obs})
   row["unit_codes"]=sorted({x["UNIT"] for x in obs})
   row["period_min"]=min((x["TIME_PERIOD"] for x in obs),default=None)
   row["period_max"]=max((x["TIME_PERIOD"] for x in obs),default=None)
   row["sample_first"]=obs[:2];row["sample_last"]=obs[-2:]
  except Exception as e:row["parse_status"]="FAIL";row["parse_error"]=str(e)
  reqs.append(row)
 # Normalized panel retains all columns and all source attributes.
 fields=list(dict.fromkeys([*(all_rows[0].keys() if all_rows else []),"SOURCE_FILE","SOURCE_SHA256"]))
 with (OUT/"emde_portfolio_flows.csv").open("w",newline="",encoding="utf-8") as f:
  if fields:
   w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(all_rows)
 keycols=["COUNTRY","BOP_ACCOUNTING_ENTRY","INDICATOR","UNIT","FREQUENCY","TIME_PERIOD"]
 keys=[tuple(x.get(k,"") for k in keycols) for x in all_rows]
 by=collections.defaultdict(list)
 for x in all_rows:by[(x["COUNTRY"],x["BOP_ACCOUNTING_ENTRY"])].append(x)
 coverage=[]
 for m in sorted(emde,key=lambda x:x["country_code"]):
  for entry in ("A_NFA_T","L_NIL_T"):
   vals=by.get((m["country_code"],entry),[])
   coverage.append({"country_code":m["country_code"],"country_name":m["country_name"],"entry":entry,
    "observation_count":len(vals),"unit_codes":sorted({x["UNIT"] for x in vals}),
    "period_min":min((x["TIME_PERIOD"] for x in vals),default=None),
    "period_max":max((x["TIME_PERIOD"] for x in vals),default=None)})
 with (OUT/"coverage_by_country_entry.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(coverage[0]));w.writeheader();w.writerows(coverage)
 summary={"scope":"WEO October 2026 G200 EMDE member BOP P_F financial-account quarterly flows; not yet aggregated",
  "weo_group_code":GROUP,"weo_group_name":"Emerging Market and Developing Economies",
  "weo_membership_count":len(emde),"weo_unique_country_codes":len({x["country_code"] for x in emde}),
  "bop_country_codelist_code_count":len(codes),"membership_codes_missing_from_bop_codelist":missing,
  "weo_retrieval":provenance["weo_workbook"],"codelist_retrieval":provenance["bop_country_codelist"],
  "dataflow":"IMF.STA:BOP(21.0.0)","dsd":"IMF.STA:DSD_BOP(24.0.0)",
  "period_window":[START,END],"indicator":"P_F","indicator_definition":"Portfolio investment, Total financial assets/liabilities",
  "entries":{"A_NFA_T":"Assets, Net acquisition of financial assets","L_NIL_T":"Liabilities, Net incurrence of liabilities"},
  "frequency":"Q","unit_dimension":"ALL reported units; no currency conversion",
  "requests":reqs,"request_http_200_count":sum(x["http_status"]==200 for x in reqs),
  "request_parse_pass_count":sum(x.get("parse_status")=="PASS" for x in reqs),
  "normalized_observation_count":len(all_rows),"unique_key_count":len(set(keys)),
  "duplicate_key_count":len(keys)-len(set(keys)),
  "country_entry_with_observations":sum(x["observation_count"]>0 for x in coverage),
  "country_entry_total":len(coverage),
  "countries_with_any_observations":len({x["COUNTRY"] for x in all_rows}),
  "unit_codes":sorted({x["UNIT"] for x in all_rows}),
  "period_min":min((x["TIME_PERIOD"] for x in all_rows),default=None),
  "period_max":max((x["TIME_PERIOD"] for x in all_rows),default=None),
  "no_forward_fill":True,"no_synthetic_rows":True,"no_currency_conversion":True,"all_source_attributes_preserved":True,
  "coverage_csv":"coverage_by_country_entry.csv","panel_csv":"emde_portfolio_flows.csv"}
 (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 (OUT/"provenance.json").write_text(json.dumps(provenance,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,ensure_ascii=False))
 if summary["request_http_200_count"]!=2 or summary["request_parse_pass_count"]!=2 or summary["duplicate_key_count"] or not all_rows:
  raise SystemExit("EMDE BOP panel acquisition/validation incomplete")
if __name__=="__main__":main()
