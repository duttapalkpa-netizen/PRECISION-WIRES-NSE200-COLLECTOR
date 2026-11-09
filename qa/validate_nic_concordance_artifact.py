#!/usr/bin/env python3
"""Independent QA against both official NIC workbooks, PDF, CSV and source manifest."""
import csv, hashlib, json, re
from collections import defaultdict
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path('artifacts/nic_concordance_audit')
RAW = ROOT / 'raw'
OUT = ROOT / 'concordance'
CSV_PATH = OUT / 'nic2025_to_nic2008_4digit_concordance.csv'
REPORT_PATH = OUT / 'nic_concordance_extraction_audit.json'
ACQ_PATH = ROOT / 'nic_source_sha256_and_workbook_inventory.json'
PDF_PATH = RAW / 'nic2025_pdf.pdf'
N25_PATH = RAW / 'nic2025_xlsx.xlsx'
N08_PATH = RAW / 'nic2008_xlsx.xlsx'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def fail(message):
    raise SystemExit('BLOCKED: ' + message)

required = [CSV_PATH, REPORT_PATH, ACQ_PATH, PDF_PATH, N25_PATH, N08_PATH]
if any(not p.exists() for p in required):
    fail('required CSV, report, manifest, PDF or official workbook missing')
report = json.loads(REPORT_PATH.read_text(encoding='utf-8'))
acq = json.loads(ACQ_PATH.read_text(encoding='utf-8'))
with CSV_PATH.open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
codes = [r['nic2025_class_4d'] for r in rows]
errors = []
if len(rows) != 463: errors.append(f'expected 463 rows, found {len(rows)}')
if len(set(codes)) != 463: errors.append('NIC-2025 keys are not 463 unique values')
if report.get('status') != 'PASS': errors.append('extractor report is not PASS')
if report.get('csv_sha256') != sha(CSV_PATH): errors.append('CSV SHA-256 mismatch')
if report.get('source_pdf_sha256') != sha(PDF_PATH): errors.append('PDF SHA-256 mismatch')
if acq.get('status') != 'PASS': errors.append('official source acquisition manifest is not PASS')
for key, filename in [('nic2025_xlsx','nic2025_xlsx.xlsx'),('nic2008_xlsx','nic2008_xlsx.xlsx'),('nic2025_pdf','nic2025_pdf.pdf')]:
    source = acq.get('sources', {}).get(key, {})
    if source.get('status') != 'DOWNLOADED' or source.get('sha256') != sha(RAW / filename):
        errors.append(f'{key} source manifest/hash mismatch')

# Independent NIC-2025 class key set from official workbook column B.
w25 = load_workbook(N25_PATH, read_only=True, data_only=True)
if 'All' not in w25.sheetnames:
    errors.append('NIC-2025 official workbook has no All sheet')
    official25 = set()
else:
    official25 = set()
    for row in w25['All'].iter_rows(min_row=2, values_only=True):
        value = row[1] if len(row) > 1 else None
        if value is not None and re.fullmatch(r'\d{4}', str(value).strip()):
            official25.add(str(value).strip())
w25.close()
pdf25 = set(codes)
if official25 != pdf25:
    errors.append(f'NIC-2025 PDF/XLSX code-set mismatch: missing={sorted(official25-pdf25)[:12]}, extra={sorted(pdf25-official25)[:12]}')

# Every referenced NIC-2008 4-digit source code must exist in the official NIC-2008 workbook.
w08 = load_workbook(N08_PATH, read_only=True, data_only=True)
official08 = set()
for row in w08.active.iter_rows(min_row=2, values_only=True):
    value = row[0] if row else None
    if value is not None and re.fullmatch(r'\d{4}', str(value).strip()):
        official08.add(str(value).strip())
w08.close()

reverse = defaultdict(list)
component_set = set()
for line_no, row in enumerate(rows, 2):
    canonical = re.sub(r'\s+', '', row['nic2008_expression_raw']).upper()
    if canonical != row['nic2008_expression_canonical']:
        errors.append(f'row {line_no}: raw/canonical expression mismatch')
    components = json.loads(row['components'])
    fragments = json.loads(row['source_fragments'])
    rebuilt = '+'.join(c['nic2008_class_4d'] + ('(P)' if c['partial'] else '') for c in components)
    if rebuilt != canonical:
        errors.append(f'row {line_no}: component/partial/aggregation marker mismatch')
    if not fragments or any(not 232 <= int(f['printed_page']) <= 238 for f in fragments):
        errors.append(f'row {line_no}: invalid source locator')
    for component in components:
        component_set.add(component['nic2008_class_4d'])
        reverse[component['nic2008_class_4d']].append(row['nic2025_class_4d'])
if component_set != official08:
    errors.append(f'NIC-2008 component/workbook set mismatch: missing={sorted(component_set-official08)[:12]}, extra={sorted(official08-component_set)[:12]}')

sentinels = {
    '1512':'1512+2220(P)', '1811':'1811+1313(P)', '2611':'2610(P)', '2619':'2610(P)',
    '3101':'3100(P)', '3102':'3100(P)', '3511':'3510(P)', '3512':'3510(P)',
    '3513':'3510(P)', '4772':'4772(P)+4789(P)+4791(P)+4799(P)'
}
by_code = {r['nic2025_class_4d']:r for r in rows}
sentinel_results = {k:(k in by_code and by_code[k]['nic2008_expression_canonical']==v) for k,v in sentinels.items()}
if not all(sentinel_results.values()): errors.append('one or more official sentinel mappings mismatch')

result = {
    'status':'PASS' if not errors else 'BLOCKED_WITH_VALIDATION_ERRORS',
    'rows':len(rows), 'unique_nic2025_codes':len(set(codes)),
    'nic2025_pdf_xlsx_code_set_match':official25==pdf25,
    'nic2008_referenced_components':len(component_set),
    'nic2008_components_all_exist_in_official_xlsx':component_set==official08,
    'reverse_mapping_one_to_many_count':sum(len(v)>1 for v in reverse.values()),
    'partial_rows':report.get('partial_rows'), 'aggregation_rows':report.get('aggregation_rows'),
    'sentinel_checks':sentinel_results,
    'csv_sha256':sha(CSV_PATH), 'nic2025_pdf_sha256':sha(PDF_PATH),
    'nic2025_xlsx_sha256':sha(N25_PATH), 'nic2008_xlsx_sha256':sha(N08_PATH),
    'errors':errors,
    'nic2_iip_weight_bridge':'UNKNOWN_BLOCKED_NOT_INFERRED'
}
(OUT / 'nic_concordance_independent_qa.json').write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps(result, indent=2, ensure_ascii=False))
if result['status'] != 'PASS': raise SystemExit(2)
