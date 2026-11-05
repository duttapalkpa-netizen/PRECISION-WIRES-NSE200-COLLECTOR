#!/usr/bin/env python3
"""Fail-closed, line-scoped extraction of the official NIC-2025/NIC-2008 4-digit concordance."""
from __future__ import annotations
import csv, hashlib, json, re
from pathlib import Path
import fitz

ROOT = Path('artifacts/nic_concordance_audit')
PDF = ROOT / 'raw' / 'nic2025_pdf.pdf'
OUT = ROOT / 'concordance'
OUT.mkdir(parents=True, exist_ok=True)
SOURCE_URL = 'https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf'
HEADING = re.compile(r'CONCORDANCE\s+BETWEEN\s+4-DIGIT\s+INDUSTRY\s+CLASSES\s+OF\s+NIC-2025\s+AND\s+NIC-2008', re.I)
ROW = re.compile(r'^\s*(\d{4})\s+((?:\d{4}\s*(?:\(\s*p\s*\))?\s*(?:\+\s*\d{4}\s*(?:\(\s*p\s*\))?\s*)*))\s*$', re.I)
TOKEN = re.compile(r'^(\d{4})(\(P\))?$', re.I)

def parse_row(line: str):
    """Parse one visual text line only; never let whitespace cross a PDF row boundary."""
    m = ROW.fullmatch(line)
    if not m: return None
    nic25, raw_expr = m.groups()
    expr = re.sub(r'\s+', '', raw_expr).upper()
    parts = expr.split('+')
    parsed = []
    for part in parts:
        token = TOKEN.fullmatch(part)
        if not token: return None
        parsed.append((token.group(1), bool(token.group(2))))
    if not parsed: return None
    partial = any(p for _, p in parsed)
    aggregation = len(parsed) > 1
    kind = 'MIXED_PARTIAL_AGGREGATION' if partial and aggregation else 'PARTIAL' if partial else 'AGGREGATION' if aggregation else 'DIRECT'
    return {'nic2025_4digit':nic25,'nic2008_expression_raw':expr,'mapping_type':kind,'partial_flag':partial,'aggregation_flag':aggregation}

if not PDF.exists(): raise SystemExit('BLOCKED: official NIC-2025 PDF binary not acquired')
pdf_bytes = PDF.read_bytes()
pdf_sha = hashlib.sha256(pdf_bytes).hexdigest()
doc = fitz.open(stream=pdf_bytes, filetype='pdf')
start = next((i for i,p in enumerate(doc) if HEADING.search(p.get_text('text'))), None)
if start is None: raise SystemExit('BLOCKED: official concordance heading not found')
records, seen = [], {}
for page_no in range(start, min(start + 7, len(doc))):
    page = doc[page_no]
    for line_no, line in enumerate(page.get_text('text', sort=True).splitlines(), 1):
        row = parse_row(line)
        if row is None: continue
        code = row['nic2025_4digit']
        if code in seen: raise SystemExit(f'BLOCKED: duplicate NIC-2025 code {code}; first page {seen[code]}, repeated page {page_no+1}')
        seen[code] = page_no + 1
        row.update({'source_pdf_page_index_1based':page_no+1,'source_pdf_text_line':line_no,'source_pdf_url':SOURCE_URL,'source_pdf_sha256':pdf_sha})
        records.append(row)
if not records: raise SystemExit('BLOCKED: no row-shaped table lines extracted; inspect PDF layout rather than guessing')
records.sort(key=lambda x:x['nic2025_4digit'])
csv_path = OUT/'nic2025_to_nic2008_4digit_concordance.csv'
with csv_path.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(records[0])); w.writeheader(); w.writerows(records)
codes=[r['nic2025_4digit'] for r in records]
report={'status':'PASS' if len(records)==463 and len(set(codes))==463 else 'BLOCKED_WITH_COVERAGE_OR_DUPLICATE_GAP','source_pdf_sha256':pdf_sha,'source_pdf_bytes':len(pdf_bytes),'pdf_pages_scanned':[start+1,min(start+7,len(doc))],'rows_extracted':len(records),'unique_nic2025_codes':len(set(codes)),'duplicate_codes':len(codes)-len(set(codes)),'expected_nic2025_4digit_class_count':463,'partial_rows':sum(r['partial_flag'] for r in records),'aggregation_rows':sum(r['aggregation_flag'] for r in records),'mixed_partial_aggregation_rows':sum(r['mapping_type']=='MIXED_PARTIAL_AGGREGATION' for r in records),'csv_sha256':hashlib.sha256(csv_path.read_bytes()).hexdigest(),'nic2_rollup_status':'NOT_CERTIFIED: class-level partial/aggregate mapping does not prove NIC-2 IIP comparability; only the official new-series NIC-2 publication can be used for that purpose'}
(OUT/'nic_concordance_extraction_audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
if report['status']!='PASS': raise SystemExit(2)
