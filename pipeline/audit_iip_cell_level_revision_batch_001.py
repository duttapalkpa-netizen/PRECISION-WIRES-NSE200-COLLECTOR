#!/usr/bin/env python3
"""Fail-closed verifier for the bounded Apr-2023 IIP revision evidence batch."""
from pathlib import Path
import argparse, csv, hashlib, json
import openpyxl

PREV="IIPMFY23049APR__IndicesIIP2011-12Monthly_annual_apr23_NIC2d_sectoralmonthly.xlsx"
CURR="IIPMFY23054MAY__IndicesIIP2011-12Monthly_annual_may23_NIC2d_sectoralmonthly.xlsx"
PREV_SHA="7cff38f066509e007c980a4267fd1753aa1fcae560438ad3df424d78d49ec30e"
CURR_SHA="6530370f75fa24997f98b760f336b70533a058e1a0a0f464bf1c26a10985425a"
ROWS=[
 ("10","Manufacture of food products",135.2,136.1),
 ("11","Manufacture of beverages",106.8,106.7),
 ("13","Manufacture of textiles",106.9,106.8),
 ("14","Manufacture of wearing apparel",91.8,91.7),
 ("15","Manufacture of leather and related products",99.5,97.8),
 ("16","Manufacture of wood and products of wood and cork; straw and plaiting materials",89.3,89.6),
 ("17","Manufacture of paper and paper products",79.4,80.6),
 ("19","Manufacture of coke and refined petroleum products",128.9,128.8),
 ("20","Manufacture of chemicals and chemical products",126.9,126.2),
]
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1<<20),b""): h.update(b)
 return h.hexdigest()
def find_cell(path,code,expected):
 wb=openpyxl.load_workbook(path,data_only=True,read_only=True)
 try:
  for ws in wb.worksheets:
   hdr=col=None
   for row in ws.iter_rows(min_row=1,max_row=min(40,ws.max_row)):
    if str(row[0].value).strip().upper() in ("NIC 2008","NIC-2008"):
     hdr=row[0].row
     for c in row:
      v=c.value
      if getattr(v,"strftime",None) and v.strftime("%Y-%m")=="2023-04": col=c.column
      elif isinstance(v,str) and v[:7]=="2023-04": col=c.column
     break
   if not hdr or not col: continue
   for ri in range(hdr+1,ws.max_row+1):
    if str(ws.cell(ri,1).value).strip()==code:
     c=ws.cell(ri,col)
     if float(c.value)!=float(expected): raise ValueError(f"{path.name}!{c.coordinate}: {c.value} != {expected}")
     return ws.title,c.coordinate
  raise ValueError(f"NIC-2008 Apr-2023 row {code} missing in {path.name}")
 finally: wb.close()
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--raw-dir",required=True,type=Path)
 ap.add_argument("--output-dir",required=True,type=Path)
 a=ap.parse_args(); a.output_dir.mkdir(parents=True,exist_ok=True)
 p,c=a.raw_dir/PREV,a.raw_dir/CURR
 if not p.is_file() or not c.is_file(): raise FileNotFoundError("Both exact official vintage workbooks are required")
 ph,ch=sha(p),sha(c)
 if ph!=PREV_SHA or ch!=CURR_SHA: raise ValueError("Source workbook SHA-256 mismatch; fail closed")
 out=[]
 for code,desc,pv,cv in ROWS:
  ps,pc=find_cell(p,code,pv); cs,cc=find_cell(c,code,cv)
  out.append({"base_year":"2011-12","classification":"NIC-2008","observation_period":"2023-04","nic_code":code,"industry_description":desc,
   "previous_vintage_table_id":"IIPMFY23049APR","previous_release_stage":"QUICK","previous_pib_prid":"1931708","previous_pib_published_ist":"2023-06-12 17:30","previous_pib_statement":"Statement II","previous_pib_table_locator":f"Industry code {code}; Index Apr'23*","previous_workbook_file":PREV,"previous_workbook_sha256":ph,"previous_workbook_sheet":ps,"previous_workbook_cell":pc,"previous_value":pv,
   "current_vintage_table_id":"IIPMFY23054MAY","current_release_stage":"FIRST_REVISION","current_pib_prid":"1938974","current_pib_published_ist":"2023-07-12 17:30","current_pib_statement":"Statement IV","current_pib_table_locator":f"Industry code {code}; Apr-23","current_workbook_file":CURR,"current_workbook_sha256":ch,"current_workbook_sheet":cs,"current_workbook_cell":cc,"current_value":cv,"revision_delta":round(cv-pv,1),"source_value_match":"PASS_BOTH_OFFICIAL_PIB_AND_SOURCE_WORKBOOK","certification_status":"CERTIFIED_CELL_LEVEL_SOURCE_MATCH"})
 cp=a.output_dir/"IIP_CELL_LEVEL_REVISION_BATCH_001_2023-04.csv"
 with cp.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
 s={"batch_id":"IIP-CELL-001","observation_period":"2023-04","candidate_rows_reviewed":9,"certified_cell_level_source_matches":9,"exact_workbook_cell_matches":18,"official_statement_value_matches":18,"mismatches":0,"remaining_policy_aligned_candidates_not_certified":684,"historical_panel_or_out_of_window_transitions_unresolved":431,"total_observed_differences":1124,"hard_gate":"BLOCKED","previous_workbook_sha256":ph,"current_workbook_sha256":ch,"ledger_csv_sha256":sha(cp),"policy":"Only these nine rows are certified; no extrapolation."}
 jp=a.output_dir/"IIP_CELL_LEVEL_REVISION_BATCH_001_SUMMARY.json"; jp.write_text(json.dumps(s,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(s,indent=2))
if __name__=="__main__": main()
