#!/usr/bin/env python3
"""Capture and cross-validate October 2026 WEO EMDE membership against IMF BOP codes.

WEO October 2026 Database Appendix is the authority for the 154 EMDE labels.
The same-vintage workbook Country Group Composition sheet provides official
ISO3 membership. IMF BOP CL_BOP_COUNTRY confirms code availability. Explicit
name aliases are documented; no guessed/fuzzy country codes are permitted.
"""
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import hashlib,json,re,unicodedata,csv,io
from openpyxl import load_workbook
from pypdf import PdfReader
import xml.etree.ElementTree as ET

OUT=Path("weo_emde_oct2026");RAW=OUT/"raw";RAW.mkdir(parents=True,exist_ok=True)
URLS={
 "weo_workbook":"https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx",
 "weo_appendix":"https://data.imf.org/-/media/iData/External-Storage/Documents/C4182C5C54794FC48892DE8F6C74FF82/en/October-2026-WEO-Database-Appendix.pdf",
 "bop_country_codelist":"https://api.imf.org/external/sdmx/3.0/structure/codelist/IMF.STA/CL_BOP_COUNTRY/1.0.0?references=all"
}
# Appendix label -> exact country name in the WEO workbook; these are label
# concordances only. The ISO3 always comes from the official workbook row.
ALIASES={
 "The Bahamas":"Bahamas, The","The Gambia":"Gambia, The",
 "Democratic Republic of the Congo":"Congo, Democratic Republic of the",
 "Republic of Congo":"Congo, Republic of",
 "Lao P.D.R.":"Lao People's Democratic Republic",
 "Naoero":"Nauru, Republic of",
 "Russia":"Russian Federation","Syria":"Syrian Arab Republic",
 "Türkiye":"Türkiye, Republic of",
 "Micronesia":"Micronesia, Federated States of",
 "São Tomé and Príncipe":"São Tomé and Príncipe, Democratic Republic of"
}
def norm(s):
 s=unicodedata.normalize("NFKD",str(s)).encode("ascii","ignore").decode().casefold()
 return " ".join(re.sub(r"[^a-z0-9]+"," ",s).split())
def get(name,url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-WEO-membership-audit/2.0","Accept":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/pdf, application/vnd.sdmx.structure+xml, application/xml, */*"})
 try:
  with urlopen(req,timeout=90) as r:status=r.status;final=r.geturl();headers=dict(r.headers.items());body=r.read()
 except HTTPError as e:status=e.code;final=e.geturl();headers=dict(e.headers.items()) if e.headers else {};body=e.read()
 except (URLError,TimeoutError) as e:status=0;final=url;headers={};body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 ext={"weo_workbook":"xlsx","weo_appendix":"pdf","bop_country_codelist":"xml"}[name]
 p=RAW/(name+"."+ext);p.write_bytes(body)
 return {"name":name,"url":url,"final_url":final,"retrieved_at_utc":ts,"http_status":status,
  "headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":str(p)}
def local(t):return t.split("}")[-1]
def main():
 manifest=[get(k,v) for k,v in URLS.items()]
 for x in manifest:
  if x["http_status"]!=200:raise SystemExit(f"{x['name']} HTTP {x['http_status']}")
 paths={x["name"]:Path(x["file"]) for x in manifest}
 wb=load_workbook(paths["weo_workbook"],read_only=True,data_only=True)
 ws=wb["Country Group Composition"]
 workbook_members=[]
 for row in ws.iter_rows(min_row=2,values_only=True):
  if str(row[0]).strip()=="G200":
   workbook_members.append({"group_code":str(row[0]),"group_name":str(row[1]),
    "country_code":str(row[3]).strip(),"country_name":str(row[4]).strip()})
 wb.close()
 if len(workbook_members)!=154 or len({x["country_code"] for x in workbook_members})!=154:
  raise SystemExit(f"Workbook G200 expected 154 unique ISO3 codes; got {len(workbook_members)}")
 pdf=PdfReader(str(paths["weo_appendix"]))
 page=pdf.pages[5].extract_text() or ""
 lines=[re.sub(r"\s+"," ",x).strip() for x in page.replace("\u00a0"," ").splitlines()]
 start=next((i for i,x in enumerate(lines) if x=="Emerging and Developing Economies"),None)
 if start is None:raise SystemExit("EMDE heading not found on Appendix page 6")
 stop=next((i for i in range(start+1,len(lines)) if lines[i] in {
  "Emerging and Developing Asia","Emerging and Developing Europe",
  "Latin America and the Caribbean","Middle East and Central Asia","Sub-Saharan Africa"}),len(lines))
 labels=[x for x in lines[start+1:stop] if x and not x.startswith("International Monetary Fund") and x not in {"WORLD ECONOMIC OUTLOOK","DATABASE APPENDIX"}]
 # Join exactly the two hard-wrapped country labels shown in the PDF.
 joined=[];i=0
 while i<len(labels):
  if labels[i]=="Democratic Republic" and i+1<len(labels) and labels[i+1]=="of the Congo":
   joined.append("Democratic Republic of the Congo");i+=2;continue
  if labels[i]=="St. Vincent and the" and i+1<len(labels) and labels[i+1]=="Grenadines":
   joined.append("St. Vincent and the Grenadines");i+=2;continue
  joined.append(labels[i]);i+=1
 labels=joined
 if len(labels)!=154 or len({norm(x) for x in labels})!=154:
  raise SystemExit(f"Appendix EMDE list expected 154 unique labels; got {len(labels)}: {labels[-5:]}")
 # Exact WEO workbook country-name map; for short labels, a unique base-name
 # match is allowed only where the workbook has one candidate. Ambiguities stay unresolved.
 by_full={norm(x["country_name"]):x for x in workbook_members}
 by_base={}
 for x in workbook_members:
  base=x["country_name"].split(",")[0].strip()
  by_base.setdefault(norm(base),[]).append(x)
 crosswalk=[]
 for label in labels:
  target=ALIASES.get(label)
  if target:
   hit=by_full.get(norm(target));hits=[hit] if hit else []
   method="EXPLICIT_LABEL_ALIAS"
  else:
   hits=by_full.get(norm(label))
   if hits: hits=[hits];method="EXACT_FULL_LABEL"
   else:
    candidates=by_base.get(norm(label),[])
    hits=candidates if len(candidates)==1 else []
    method="UNIQUE_WEO_BASE_NAME" if len(hits)==1 else ("AMBIGUOUS" if candidates else "UNMAPPED")
  crosswalk.append({"weo_vintage":"October 2026","appendix_emde_label":label,
   "workbook_country_name":hits[0]["country_name"] if len(hits)==1 else "",
   "iso3":hits[0]["country_code"] if len(hits)==1 else "",
   "mapping_method":method if len(hits)==1 else method,
   "mapping_status":"PASS" if len(hits)==1 else method})
 # Parse BOP codelist and require all WEO workbook ISO3 codes to exist.
 root=ET.fromstring(paths["bop_country_codelist"].read_bytes());bop_codes=set()
 for el in root.iter():
  if local(el.tag)=="Code" and el.attrib.get("id"):bop_codes.add(el.attrib["id"])
 missing=sorted({x["country_code"] for x in workbook_members}-bop_codes)
 with (OUT/"weo_emde_appendix_to_bop_iso3_crosswalk.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(crosswalk[0]));w.writeheader();w.writerows(crosswalk)
 with (OUT/"weo_oct2026_emde_membership.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(workbook_members[0]));w.writeheader();w.writerows(sorted(workbook_members,key=lambda x:x["country_code"]))
 summary={"scope":"October 2026 WEO Appendix top-level EMDE list independently cross-checked against same-vintage workbook G200 composition and IMF BOP country codelist",
  "sources":manifest,"pdf_page_count":len(pdf.pages),"appendix_emde_label_count":len(labels),
  "appendix_unique_label_count":len({norm(x) for x in labels}),"workbook_g200_member_count":len(workbook_members),
  "workbook_g200_unique_iso3_count":len({x["country_code"] for x in workbook_members}),
  "appendix_to_workbook_mapping_pass":sum(x["mapping_status"]=="PASS" for x in crosswalk),
  "appendix_unmapped_or_ambiguous":[x for x in crosswalk if x["mapping_status"]!="PASS"],
  "bop_country_codelist_code_count":len(bop_codes),"workbook_iso3_missing_from_bop_codelist":missing,
  "membership_validation_pass":len(labels)==154 and len(workbook_members)==154 and
   len({norm(x) for x in labels})==154 and sum(x["mapping_status"]=="PASS" for x in crosswalk)==154 and not missing,
  "guardrails":["No fuzzy matching or guessed ISO3 codes.","Every ISO3 comes from official WEO October 2026 Country Group Composition sheet.",
   "BOP codelist is a code-presence check only; it does not prove observation coverage.",
   "Country-level BOP coverage remains a separate observation QA result."]}
 (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,ensure_ascii=False))
 if not summary["membership_validation_pass"]:raise SystemExit("Membership cross-validation incomplete; do not promote")
if __name__=="__main__":main()
