#!/usr/bin/env python3
"""Capture October 2026 WEO EMDE membership from workbook composition sheet.

Authoritative membership source is the exact WEO vintage workbook's
'Country Group Composition' sheet, group code G200. Crosswalk to IMF BOP
COUNTRY codelist by exact code ID only; no fuzzy country-name matching.
"""
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,csv,io,unicodedata,re
import openpyxl,xml.etree.ElementTree as ET

OUT=Path("weo_emde_oct2026");RAW=OUT/"raw";RAW.mkdir(parents=True,exist_ok=True)
URLS={
 "weo_workbook":"https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx",
 "weo_appendix":"https://data.imf.org/-/media/iData/External-Storage/Documents/C4182C5C54794FC48892DE8F6C74FF82/en/October-2026-WEO-Database-Appendix.pdf",
 "bop_country_codelist":"https://api.imf.org/external/sdmx/3.0/structure/codelist/IMF.STA/CL_BOP_COUNTRY/1.0.0?references=none"
}
def norm(s):
 s=unicodedata.normalize("NFKD",str(s)).encode("ascii","ignore").decode().lower()
 return " ".join(re.sub(r"[^a-z0-9]+"," ",s).split())
def fetch(name,url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-WEO-membership-audit/1.1","Accept":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/pdf, application/vnd.sdmx.structure+xml, application/xml, */*"})
 try:
  with urlopen(req,timeout=90) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 ext={"weo_workbook":"xlsx","weo_appendix":"pdf","bop_country_codelist":"xml"}[name]
 p=RAW/(name+"."+ext);p.write_bytes(body)
 return {"name":name,"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,
  "headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":str(p)}
def local(tag):return tag.split("}")[-1]
def main():
 manifest=[fetch(k,v) for k,v in URLS.items()]
 for x in manifest:
  if x["http_status"]!=200:raise SystemExit(f"{x['name']} HTTP {x['http_status']}")
 paths={x["name"]:Path(x["file"]) for x in manifest}
 wb=openpyxl.load_workbook(paths["weo_workbook"],read_only=True,data_only=True)
 if "Country Group Composition" not in wb.sheetnames:raise SystemExit("WEO workbook missing Country Group Composition sheet")
 ws=wb["Country Group Composition"]
 headers=next(ws.iter_rows(min_row=1,max_row=1,values_only=True))
 members=[]
 for row in ws.iter_rows(min_row=2,values_only=True):
  if str(row[0]).strip()=="G200":
   members.append({"group_code":str(row[0]).strip(),"group_name":str(row[1]).strip(),
    "country_code":str(row[3]).strip(),"country_name":str(row[4]).strip()})
 wb_info={"sheet_names":wb.sheetnames,"composition_headers":list(headers),
  "composition_max_row":ws.max_row,"composition_max_column":ws.max_column}
 wb.close()
 if not members:raise SystemExit("No G200 EMDE rows found in WEO Country Group Composition")
 # Exact ISO-like country code IDs from official BOP codelist.
 root=ET.parse(paths["bop_country_codelist"]).getroot()
 codes={}
 for el in root.iter():
  if local(el.tag)=="Code" and el.attrib.get("id"):
   code=el.attrib["id"]
   names=[x.text.strip() for x in el.iter() if local(x.tag)=="Name" and x.text and x.text.strip()]
   codes.setdefault(code,{"bop_country_code":code,"bop_country_names":sorted(set(names))})
 rows=[]
 for m in members:
  hit=codes.get(m["country_code"])
  rows.append({"weo_edition":"October 2026","weo_group_code":m["group_code"],
   "weo_group_name":m["group_name"],"weo_country_code":m["country_code"],
   "weo_country_name":m["country_name"],
   "bop_country_code":hit["bop_country_code"] if hit else "",
   "bop_country_names":";".join(hit["bop_country_names"]) if hit else "",
   "mapping_status":"EXACT_CODE" if hit else "UNMAPPED",
   "name_label_normalized_match":bool(hit and any(norm(m["country_name"])==norm(n) for n in hit["bop_country_names"]))})
 with (OUT/"weo_emde_to_bop_country_crosswalk.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 counts={s:sum(x["mapping_status"]==s for x in rows) for s in ("EXACT_CODE","UNMAPPED")}
 summary={"scope":"October 2026 WEO G200 EMDE composition sheet to IMF BOP COUNTRY codelist exact-code crosswalk",
  "weo_group_code":"G200","weo_group_name":"Emerging Market and Developing Economies",
  "weo_membership_count":len(members),"unique_weo_country_codes":len({x["country_code"] for x in members}),
  "duplicate_weo_codes":sorted(c for c in {x["country_code"] for x in members} if sum(y["country_code"]==c for y in members)>1),
  "bop_codelist_code_count":len(codes),"mapping_status_counts":counts,
  "unmapped":[x["weo_country_code"]+":"+x["weo_country_name"] for x in rows if x["mapping_status"]=="UNMAPPED"],
  "name_label_nonmatches":[x["weo_country_code"]+":"+x["weo_country_name"]+" => "+x["bop_country_names"] for x in rows if x["mapping_status"]=="EXACT_CODE" and not x["name_label_normalized_match"]],
  "workbook":wb_info,"manifest":manifest,
  "membership_authority":"WEO October 2026 workbook Country Group Composition sheet, G200; not PDF text extraction.",
  "crosswalk_rule":"Exact country code ID only; no fuzzy name matching or guessed aliases."}
 (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,ensure_ascii=False))
 if len(members)!=154 or len({x["country_code"] for x in members})!=154:
  raise SystemExit("WEO G200 membership count/uniqueness not 154; inspect source rows, do not force count")
 if counts["UNMAPPED"]:
  raise SystemExit("Some WEO G200 country codes are absent from IMF BOP codelist")
if __name__=="__main__":main()
