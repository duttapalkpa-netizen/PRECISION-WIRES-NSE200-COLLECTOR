#!/usr/bin/env python3
"""Fail-closed QA for the official September 2026 NIC-2025 manufacturing 2-digit table."""
from __future__ import annotations
import csv,hashlib,json,math
from pathlib import Path
SRC=Path('research/data/iip_2026_09_manufacturing_nic2_statement_IIA.csv')
OUT=Path('artifacts/iip_release_qa'); OUT.mkdir(parents=True,exist_ok=True)
if not SRC.exists(): raise SystemExit('BLOCKED: NIC-2 source CSV missing')
raw=SRC.read_bytes(); sha=hashlib.sha256(raw).hexdigest()
with SRC.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
errors=[]; expected=[str(i) for i in range(10,33)]
codes=[r.get('nic_2025_2digit','') for r in rows]
if len(rows)!=23: errors.append(f'ROW_COUNT_{len(rows)}_EXPECTED_23')
if sorted(codes)!=expected: errors.append('NIC2_CODE_COVERAGE_OR_DUPLICATE_MISMATCH')
for n,r in enumerate(rows,2):
    if r.get('reference_month')!='2026-09' or r.get('base_year')!='2022-23' or r.get('estimate_stage')!='QUICK_ESTIMATE': errors.append(f'PERIOD_OR_VINTAGE_MISMATCH_ROW_{n}')
    if r.get('release_timestamp_ist')!='2026-10-28T16:00:00+05:30': errors.append(f'PUBLICATION_CUTOFF_MISMATCH_ROW_{n}')
    if r.get('source_statement')!='II_A' or 'PRID=2329475' not in r.get('source_url',''): errors.append(f'SOURCE_PROVENANCE_MISMATCH_ROW_{n}')
    try:
        prev=float(r['sep_2025_index']); curr=float(r['sep_2026_index']); yoy=float(r['sep_yoy_growth_pct'])
        cprev=float(r['apr_sep_2025_cumulative_index']); ccurr=float(r['apr_sep_2026_cumulative_index']); cyoy=float(r['apr_sep_yoy_growth_pct'])
        if abs(round((curr/prev-1)*100,1)-yoy)>0.1: errors.append(f'SEP_YOY_ARITHMETIC_ROW_{n}')
        if abs(round((ccurr/cprev-1)*100,1)-cyoy)>0.1: errors.append(f'CUMULATIVE_YOY_ARITHMETIC_ROW_{n}')
        float(r['weight_pct'])
    except Exception: errors.append(f'NON_NUMERIC_FIELD_ROW_{n}')
weights=sum(float(r['weight_pct']) for r in rows)
positive=sum(float(r['sep_yoy_growth_pct'])>0 for r in rows)
negative=sum(float(r['sep_yoy_growth_pct'])<0 for r in rows)
zero=sum(float(r['sep_yoy_growth_pct'])==0 for r in rows)
if abs(weights-76.062)>0.005: errors.append(f'MANUFACTURING_WEIGHT_SUM_{weights}_EXPECTED_76.062_TOL_0.005')
if (positive,negative,zero)!=(17,6,0): errors.append(f'BREADTH_MISMATCH_{positive}_{negative}_{zero}')
lookup={r['nic_2025_2digit']:float(r['sep_yoy_growth_pct']) for r in rows}
for code,value in {'11':39.4,'22':19.9,'27':33.9,'29':19.0}.items():
    if lookup.get(code)!=value: errors.append(f'KEY_GROUP_VALUE_MISMATCH_{code}')
report={'status':'PASS_TRANSCRIPTION_STRUCTURE_AND_ARITHMETIC_QA' if not errors else 'BLOCKED_QA_ERRORS','source_csv':str(SRC),'source_csv_bytes':len(raw),'source_csv_sha256':sha,'row_count':len(rows),'unique_nic2_codes':len(set(codes)),'nic2_codes':sorted(codes),'weight_sum_pct':round(weights,3),'official_manufacturing_weight_pct':76.062,'weight_rounding_difference':round(weights-76.062,3),'positive_groups':positive,'negative_groups':negative,'zero_growth_groups':zero,'positive_breadth_pct':round(positive/23*100,4),'derived_breadth_not_separately_published':True,'errors':errors,'source_binary_pdf_sha256':'NOT_ACQUIRED','scope':'September 2026 NIC-2025 Manufacturing 2-digit Statement II-A only; not the full April 2023 onward panel'}
(OUT/'iip_2026_09_nic2_statement_IIA_qa.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
if errors: raise SystemExit(2)
