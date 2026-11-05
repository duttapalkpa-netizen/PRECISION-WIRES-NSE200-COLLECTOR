#!/usr/bin/env python3
"""Extract the official NIC-2025 to NIC-2008 4-digit concordance from the MoSPI PDF."""
from __future__ import annotations
import csv, hashlib, json, re
from pathlib import Path
import fitz

ROOT = Path('artifacts/nic_concordance_audit')
PDF = ROOT / 'raw' / 'nic2025_pdf.pdf'
OUT = ROOT / 'concordance'
OUT.mkdir(parents=True, exist_ok=True)
if not PDF.exists(): raise SystemExit('BLOCKED: official NIC-2025 PDF binary not acquired')
pdf_sha = hashlib.sha256(PDF.read_bytes()).hexdigest()
doc = fitz.open(PDF)
heading = re.compile(r'CONCORDANCE\s+BETWEEN\s+4-DIGIT\s+INDUSTRY\s+CLASSES\s+OF\s+NIC-2025\s+AND\s+NIC-2008', re.I)
row_re = re.compile(r'(?<!\d)(\d{4})\s+((?:\d{4}\s*(?:\(\s*p\s*\))?\s*(?:\+\s*)?)+)(?!\d)', re.I)
token_re = re.compile(r'(\d{4})\s*(\(\s*p\s*\))?', re.I)
start = None
for i, page in enumerate(doc):
    if heading.search(page.get_text('text')):
        start = i
        break
if start is None: raise SystemExit('BLOCKED: concordance heading not found in acquired PDF')
records, seen = [], {}
for page_no in range(start, min(start + 7, len(doc))):
    raw_text = doc[page_no].get_text('text')
    for m in row_re.finditer(raw_text):
        code, expr = m.group(1), re.sub(r'\s+', '', m.group(2)).upper()
        # Reject non-mapping expressions and malformed plus chains.
        tokens = token_re.findall(expr)
        rebuilt = '+'.join(c + ('(P)' if p else '') for c, p in tokens)
        if rebuilt != expr or not tokens: continue
        if code in seen:
            raise SystemExit(f'BLOCKED: duplicate NIC-2025 class {code} on PDF pages {seen[code]} and {page_no+1}')
        seen[code] = page_no + 1
        partial = any(bool(p) for _, p in tokens)
        aggregate = len(tokens) > 1
        mapping_type = 'MIXED_PARTIAL_AGGREGATION' if partial and aggregate else 'PARTIAL' if partial else 'AGGREGATION' if aggregate else 'IDENTITY_OR_DIRECT'
        records.append({'nic2025_4digit':code,'nic2008_expression_raw':expr,'mapping_type':mapping_type,'partial_flag':partial,'aggregation_flag':aggregate,'source_pdf_page_index_1based':page_no+1,'source_pdf_url':'https://www.mospi.gov.in/sites/default/files/main_menu/national_industrial_classification/NIC_2025Final_18112025.pdf','source_pdf_sha256':pdf_sha})
if not records: raise SystemExit('BLOCKED: no concordance rows extracted; inspect PDF text layer before accepting')
records.sort(key=lambda x: x['nic2025_4digit'])
with (OUT/'nic2025_to_nic2008_4digit_concordance.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(records[0])); w.writeheader(); w.writerows(records)
codes = [r['nic2025_4digit'] for r in records]
report = {
 'status':'PASS' if len(records)==463 and len(set(codes))==463 else 'BLOCKED_WITH_COVERAGE_OR_DUPLICATE_GAP',
 'source_pdf_sha256':pdf_sha,'source_pdf_bytes':PDF.stat().st_size,'pdf_pages_scanned':[start+1,min(start+7,len(doc))],
 'rows_extracted':len(records),'unique_nic2025_codes':len(set(codes)),'duplicate_codes':len(codes)-len(set(codes)),
 'expected_nic2025_4digit_class_count':463,
 'partial_rows':sum(r['partial_flag'] for r in records),'aggregation_rows':sum(r['aggregation_flag'] for r in records),
 'mixed_partial_aggregation_rows':sum(r['mapping_type']=='MIXED_PARTIAL_AGGREGATION' for r in records),
 'division_coverage':sorted(set(c[:2] for c in codes)),
 'nic2_rollup_status':'NOT_CERTIFIED: 4-digit class concordance does not by itself prove 2-digit IIP comparability; official IIP linking factors are only sector/general level and NIC class mapping semantics include partial/aggregate rows',
 'csv_sha256':hashlib.sha256((OUT/'nic2025_to_nic2008_4digit_concordance.csv').read_bytes()).hexdigest(),
}
(OUT/'nic_concordance_extraction_audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
if report['status']!='PASS': raise SystemExit(2)
