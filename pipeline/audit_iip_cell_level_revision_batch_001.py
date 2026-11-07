#!/usr/bin/env python3
"""Reproduce IIP Apr-2023 Quick -> First Revision cell-level source matching.

Inputs are the two official MoSPI catalogue XLSX payloads from the 41-vintage
source audit artifact. This bounded batch certifies only the nine rows listed
below; it does not infer certification for any other candidate.
"""
from pathlib import Path
import argparse, csv, hashlib, json
import openpyxl

PREV_ID = "IIPMFY23049APR"
CURR_ID = "IIPMFY23054MAY"
PREV_NAME = "IIPMFY23049APR__IndicesIIP2011-12Monthly_annual_apr23_NIC2d_sectoralmonthly.xlsx"
CURR_NAME = "IIPMFY23054MAY__IndicesIIP2011-12Monthly_annual_may23_NIC2d_sectoralmonthly.xlsx"
PREV_SHA = "7cff38f066509e007c980a4267fd1753aa1fcae560438ad3df424d78d49ec30e"
CURR_SHA = "6530370f75fa24997f98b760f336b70533a058e1a0a0f464bf1c26a10985425a"
# Exact values transcribed from official PIB Statement II (PRID 1931708)
# and Statement IV (PRID 1938974), both for April 2023.
ROWS = [
    ("10", "Manufacture of food products", 135.2, 136.1),
    ("11", "Manufacture of beverages", 106.8, 106.7),
    ("13", "Manufacture of textiles", 106.9, 106.8),
    ("14", "Manufacture of wearing apparel", 91.8, 91.7),
    ("15", "Manufacture of leather and related products", 99.5, 97.8),
    ("16", "Manufacture of wood and products of wood and cork; straw and plaiting materials", 89.3, 89.6),
    ("17", "Manufacture of paper and paper products", 79.4, 80.6),
    ("19", "Manufacture of coke and refined petroleum products", 128.9, 128.8),
    ("20", "Manufacture of chemicals and chemical products", 126.9, 126.2),
]

def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def cell_for(path, code, expected):
    wb=openpyxl.load_workbook(path,data_only=True,read_only=True)
    try:
        for ws in wb.worksheets:
            header=None; col=None
            for row in ws.iter_rows(min_row=1,max_row=min(40,ws.max_row)):
                if str(row[0].value).strip().upper() in ("NIC 2008","NIC-2008"):
                    header=row[0].row
                    for c in row:
                        v=c.value
                        if getattr(v,"strftime",None) and v.strftime("%Y-%m")=="2023-04": col=c.column
                        elif isinstance(v,str) and v[:7]=="2023-04": col=c.column
                    break
            if not header or not col: continue
            for ridx in range(header+1,ws.max_row+1):
                if str(ws.cell(ridx,1).value).strip()==str(code):
                    c=ws.cell(ridx,col)
                    if float(c.value)!=float(expected):
                        raise ValueError(f"{path.name} {ws.title}!{c.coordinate}: {c.value} != {expected}")
                    return ws.title,c.coordinate
        raise ValueError(f"NIC-2008 Apr-2023 row {code} not found in {path.name}")
    finally:
        wb.close()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--raw-dir",required=True,type=Path,help="Directory containing original raw XLSX files")
    ap.add_argument("--output-dir",required=True,type=Path)
    a=ap.parse_args(); a.output_dir.mkdir(parents=True,exist_ok=True)
    prev=a.raw_dir/PREV_NAME; curr=a.raw_dir/CURR_NAME
    if not prev.is_file() or not curr.is_file(): raise FileNotFoundError("Both exact vintage XLSX payloads are required")
    psha,csha=sha(prev),sha(curr)
    if psha!=PREV_SHA or csha!=CURR_SHA: raise ValueError("Source workbook SHA-256 mismatch; refusing certification")
    out=[]
    for code,desc,pval,cval in ROWS:
        ps,pc=cell_for(prev,code,pval); cs,cc=cell_for(curr,code,cval)
        out.append({"base_year":"2011-12","classification":"NIC-2008","observation_period":"2023-04","nic_code":code,"industry_description":desc,
          "previous_vintage_table_id":PREV_ID,"previous_release_stage":"QUICK","previous_pib_prid":"1931708","previous_pib_published_ist":"2023-06-12 17:30","previous_pib_statement":"Statement II","previous_pib_table_locator":f"Industry code {code}; Index Apr'23*","previous_workbook_file":PREV_NAME,"previous_workbook_sha256":psha,"previous_workbook_sheet":ps,"previous_workbook_cell":pc,"previous_value":pval,
          "current_vintage_table_id":CURR_ID,"current_release_stage":"FIRST_REVISION","current_pib_prid":"1938974","current_pib_published_ist":"2023-07-12 17:30","current_pib_statement":"Statement IV","current_pib_table_locator":f"Industry code {code}; Apr-23","current_workbook_file":CURR_NAME,"current_workbook_sha256":csha,"current_workbook_sheet":cs,"current_workbook_cell":cc,"current_value":cval,"revision_delta":round(cval-pval,1),"source_value_match":"PASS_BOTH_OFFICIAL_PIB_AND_SOURCE_WORKBOOK","certification_status":"CERTIFIED_CELL_LEVEL_SOURCE_MATCH"})
    csvp=a.output_dir/"IIP_CELL_LEVEL_REVISION_BATCH_001_2023-04.csv"
    with csvp.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    summary={"batch_id":"IIP-CELL-001","observation_period":"2023-04","previous_vintage":PREV_ID,"current_vintage":CURR_ID,"previous_release_stage":"QUICK","current_release_stage":"FIRST_REVISION","candidate_rows_reviewed":9,"official_pib_statement_pair":"1931708 Statement II -> 1938974 Statement IV","source_workbooks_verified":2,"previous_workbook_sha256":psha,"current_workbook_sha256":csha,"exact_workbook_cell_matches":18,"official_statement_value_matches":18,"certified_cell_level_source_matches":9,"mismatches":0,"remaining_policy_aligned_candidates_not_certified":684,"historical_panel_or_out_of_window_transitions_unresolved":431,"total_observed_differences":1124,"hard_gate":"BLOCKED","ledger_csv_sha256":sha(csvp),"policy":"Certification applies only to these nine exact observation rows; no extrapolation."}
    jp=a.output_dir/"IIP_CELL_LEVEL_REVISION_BATCH_001_SUMMARY.json"
    jp.write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"summary":summary,"summary_sha256":sha(jp)},indent=2))
if __name__=="__main__": main()
