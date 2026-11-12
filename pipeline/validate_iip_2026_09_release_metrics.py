#!/usr/bin/env python3
"""Validate the manually transcribed September 2026 official IIP release metrics ledger."""
from __future__ import annotations
import csv,hashlib,json
from pathlib import Path
ROOT=Path('research/data')
SRC=ROOT/'iip_new_series_release_2026_09_official_metrics.csv'
OUT=Path('artifacts/iip_release_qa'); OUT.mkdir(parents=True,exist_ok=True)
if not SRC.exists(): raise SystemExit('BLOCKED: source metrics CSV missing')
raw=SRC.read_bytes(); sha=hashlib.sha256(raw).hexdigest()
with SRC.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
required={'reference_month','release_date','base_year','estimate_stage','metric','classification','category','value','unit','comparison','source_url','source_precision'}
errors=[]
if not rows: errors.append('EMPTY_LEDGER')
if rows and set(rows[0])!=required: errors.append('SCHEMA_MISMATCH')
for n,r in enumerate(rows,2):
    if not r.get('source_url','').startswith('https://www.pib.gov.in/'): errors.append(f'NON_OFFICIAL_SOURCE_ROW_{n}')
    if r.get('base_year')!='2022-23': errors.append(f'BASE_YEAR_MISMATCH_ROW_{n}')
    if r.get('release_date')!='2026-10-28': errors.append(f'RELEASE_DATE_MISMATCH_ROW_{n}')
    try: float(r['value'])
    except Exception: errors.append(f'NON_NUMERIC_VALUE_ROW_{n}')
keys=[(r['reference_month'],r['estimate_stage'],r['metric'],r['category']) for r in rows]
if len(keys)!=len(set(keys)): errors.append('DUPLICATE_METRIC_KEYS')
def val(month,stage,metric,category):
    found=[r for r in rows if (r['reference_month'],r['estimate_stage'],r['metric'],r['category'])==(month,stage,metric,category)]
    if len(found)!=1: raise ValueError(f'expected exactly one {month}/{stage}/{metric}/{category}, got {len(found)}')
    return float(found[0]['value'])
try:
    if val('2026-09','QUICK_ESTIMATE','IIP_YOY_GROWTH','ALL_INDIA')!=6.7: errors.append('HEADLINE_GROWTH_MISMATCH')
    if val('2026-09','QUICK_ESTIMATE','POSITIVE_GROWTH_GROUP_COUNT','POSITIVE_GROUPS')!=17: errors.append('POSITIVE_NIC2_GROUP_COUNT_MISMATCH')
    if val('2026-09','QUICK_ESTIMATE','WEIGHTED_RESPONSE_RATE','SEPTEMBER_QUICK')!=86.5: errors.append('SEPTEMBER_RESPONSE_RATE_MISMATCH')
    if val('2026-08','FINAL_REVISION','WEIGHTED_RESPONSE_RATE','AUGUST_FINAL')!=92.0: errors.append('AUGUST_FINAL_RESPONSE_RATE_MISMATCH')
except Exception as exc: errors.append(f'REQUIRED_METRIC_LOOKUP_FAILED:{exc}')
breadth_pct=round(17/23*100,4)
report={'status':'PASS_TRANSCRIPTION_AND_STRUCTURE_QA' if not errors else 'BLOCKED_QA_ERRORS','source_csv':str(SRC),'source_csv_bytes':len(raw),'source_csv_sha256':sha,'row_count':len(rows),'unique_metric_keys':len(set(keys)),'errors':errors,'derived_manufacturing_NIC2_positive_breadth_pct':breadth_pct,'derived_breadth_formula':'17 positive NIC-2 groups / 23 total NIC-2 groups * 100','derived_breadth_is_official_published_metric':False,'source_binary_pdf_sha256':'NOT_AVAILABLE_IN_THIS_LEDGER','source_note':'This validates the transcribed ledger structure and selected values; it does not certify raw PIB PDF bytes or replace row-by-row PDF cell audit.'}
(OUT/'iip_2026_09_release_metrics_qa.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
if errors: raise SystemExit(2)
