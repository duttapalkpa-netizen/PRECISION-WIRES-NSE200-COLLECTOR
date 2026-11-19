#!/usr/bin/env python3
"""Capture October 2026 WEO workbook, Appendix and IMF BOP country codelist.

No fuzzy code assignment: only normalized exact label matches and a small,
versioned explicit alias table are allowed. Unmatched names remain UNKNOWN.
"""
from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from urllib.parse import quote
import hashlib,json,re,unicodedata,csv,zipfile,io
from openpyxl import load_workbook
from pypdf import PdfReader
import xml.etree.ElementTree as ET

OUT=Path("weo_emde_oct2026"); RAW=OUT/"raw"; RAW.mkdir(parents=True,exist_ok=True)
URLS={
 "weo_workbook":"https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx",
 "weo_appendix":"https://data.imf.org/-/media/iData/External-Storage/Documents/C4182C5C54794FC48892DE8F6C74FF82/en/October-2026-WEO-Database-Appendix.pdf",
 "bop_country_codelist":"https://api.imf.org/external/sdmx/3.0/structure/codelist/IMF.STA/CL_BOP_COUNTRY/1.0.0?references=none"
}
ALIASES={
 "naoero":"nauru","the gambia":"gambia","the bahamas":"bahamas",
 "kyrgyz republic":"kyrgyzstan","lao p.d.r.":"lao people's democratic republic",
 "republic of congo":"congo","democratic republic of the congo":"democratic republic of the congo",
 "west bank and gaza":"west bank and gaza","korea":"korea, republic of",
 "iran":"iran, islamic republic of","moldova":"moldova, republic of",
 "russia":"russian federation","syria":"syrian arab republic",
 "tanzania":"tanzania, united republic of","venezuela":"venezuela, bolivarian republic of",
 "bolivia":"bolivia, plurinational state of","micronesia":"micronesia, federated states of",
 "taiwan province of china":"taiwan, province of china","cape verde":"cabo verde",
 "cote d'ivoire":"côte d'ivoire","turkiye":"türkiye"
}
def norm(s):
 s=unicodedata.normalize("NFKD",str(s)).encode("ascii","ignore").decode().lower()
 s=s.replace("&","and")
 s=re.sub(r"[^a-z0-9]+"," ",s)
 return " ".join(s.split())
def fetch(name,url):
 ts=datetime.now(timezone.utc).isoformat()
 req=Request(url,headers={"User-Agent":"PRECISION-WIRES-WEO-membership-audit/1.0","Accept":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/pdf, application/vnd.sdmx.structure+xml, application/xml, */*"})
 try:
  with urlopen(req,timeout=90) as r:
   status=r.status; headers=dict(r.headers.items()); body=r.read()
 except HTTPError as e:
  status=e.code; headers=dict(e.headers.items()) if e.headers else {}; body=e.read()
 except (URLError,TimeoutError) as e:
  status=0; headers={}; body=str(e).encode()
 safe={k:v for k,v in headers.items() if k.lower() not in {"set-cookie","authorization","www-authenticate"}}
 ext={"weo_workbook":"xlsx","weo_appendix":"pdf","bop_country_codelist":"xml"}[name]
 p=RAW/(name+"."+ext); p.write_bytes(body)
 return {"name":name,"url":url,"retrieved_at_utc":ts,"http_status":status,
  "headers":safe,"byte_count":len(body),"sha256":hashlib.sha256(body).hexdigest(),"file":str(p)}
def local(tag): return tag.split("}")[-1]
def main():
 manifest=[fetch(k,v) for k,v in URLS.items()]
 for r in manifest:
  if r["http_status"]!=200: raise SystemExit(f"{r['name']} HTTP {r['http_status']}")
 paths={r["name"]:Path(r["file"]) for r in manifest}
 # Workbook: preserve workbook sheet names and locate country/group worksheets.
 wb=load_workbook(paths["weo_workbook"],read_only=True,data_only=True)
 workbook_info={"sheet_names":wb.sheetnames,"sheets":[]}
 for ws in wb.worksheets:
  workbook_info["sheets"].append({"title":ws.title,"max_row":ws.max_row,"max_column":ws.max_column})
 (OUT/"workbook_structure.json").write_text(json.dumps(workbook_info,indent=2)+"\n")
 # PDF page 6 has the exact WEO classification list.
 pdf=PdfReader(str(paths["weo_appendix"]))
 pages=[p.extract_text() or "" for p in pdf.pages]
 alltext="\n".join(pages)
 start=alltext.find("Emerging and Developing Economies")
 if start<0: raise SystemExit("EMDE heading not found in October 2026 WEO appendix")
 tail=alltext[start+len("Emerging and Developing Economies"):]
 stops=[tail.find(x) for x in ["Emerging and Developing Asia","Emerging and Developing Europe","Latin America and the Caribbean"] if tail.find(x)>=0]
 if not stops: raise SystemExit("Could not locate next WEO regional group heading")
 block=tail[:min(stops)]
 lines=[re.sub(r"\s+"," ",x).strip(" \t\r\n-") for x in block.splitlines()]
 lines=[x for x in lines if x and x not in {"WORLD ECONOMIC OUTLOOK","DATABASE APPENDIX"}]
 # repair PDF line wraps only when the next line starts with a continuation
 names=[]; pending=""
 for line in lines:
  if pending:
   pending += " "+line
   names.append(pending); pending=""
  elif line in {"Democratic Republic","St. Vincent and the"}:
   pending=line
  else: names.append(line)
 if pending: names.append(pending)
 names=[x for x in names if x]
 # exact unique list, retain order
 seen=set(); unique=[]
 for n in names:
  k=norm(n)
  if k not in seen: seen.add(k); unique.append(n)
 # parse official BOP country codelist
 root=ET.fromstring(paths["bop_country_codelist"].read_bytes())
 codes=[]
 for el in root.iter():
  if local(el.tag)=="Code":
   cid=el.attrib.get("id")
   label=next((x.text for x in el if local(x.tag)=="Name" and x.text),None)
   if cid and label: codes.append({"bop_country_code":cid,"bop_country_label":label,"norm":norm(label)})
 bynorm={}
 for c in codes: bynorm.setdefault(c["norm"],[]).append(c)
 rows=[]
 for name in unique:
  n=norm(name); target=norm(ALIASES.get(n,name))
  hits=bynorm.get(target,[])
  rows.append({"weo_edition":"October 2026","weo_group":"Emerging and Developing Economies",
   "weo_country_name":name,"normalized_name":n,"alias_used":ALIASES.get(n,""),
   "bop_country_code":hits[0]["bop_country_code"] if len(hits)==1 else "",
   "bop_country_label":hits[0]["bop_country_label"] if len(hits)==1 else "",
   "mapping_status":"EXACT_LABEL" if len(hits)==1 and target==n else ("EXPLICIT_ALIAS" if len(hits)==1 else ("AMBIGUOUS" if len(hits)>1 else "UNMAPPED")),
   "candidate_codes":";".join(x["bop_country_code"] for x in hits)})
 with (OUT/"weo_emde_to_bop_country_crosswalk.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 summary={"scope":"October 2026 WEO official classification Appendix + Entire Dataset workbook + IMF BOP COUNTRY codelist",
  "manifest":manifest,"pdf_page_count":len(pdf.pages),"workbook":workbook_info,
  "emde_member_count":len(unique),"unique_member_count":len(set(norm(x) for x in unique)),
  "expected_154_check":len(unique)==154,
  "bop_codelist_code_count":len(codes),
  "mapping_status_counts":{s:sum(x["mapping_status"]==s for x in rows) for s in ["EXACT_LABEL","EXPLICIT_ALIAS","UNMAPPED","AMBIGUOUS"]},
  "unmapped":[x["weo_country_name"] for x in rows if x["mapping_status"]=="UNMAPPED"],
  "ambiguous":[x for x in rows if x["mapping_status"]=="AMBIGUOUS"],
  "notes":["WEO Appendix is the authority for WEO EMDE classification; workbook is captured as the vintage's complete data file.",
   "Country-code mapping is a separate exact/explicit-alias operation against IMF BOP CL_BOP_COUNTRY.",
   "No fuzzy matching, guessed code, or imputed mapping. Unmapped/ambiguous names remain unresolved.",
   "A 154-member count is a validation assertion, not a forced target; a different observed count must be reported, not silently edited."]}
 (OUT/"summary.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,ensure_ascii=False))
 if summary["emde_member_count"]!=154: raise SystemExit("WEO EMDE count differs from expected 154; inspect extracted list before acceptance")
if __name__=="__main__": main()
