#!/usr/bin/env python3
"""Independent fail-closed QA for the extracted NIC concordance artifact."""
import csv, hashlib, json, re
from collections import defaultdict
from pathlib import Path

ROOT = Path('artifacts/nic_concordance_audit')
CSV_PATH = ROOT/'concordance'/'nic2025_to_nic2008_4digit_concordance.csv'
REPORT_PATH = ROOT/'concordance'/'nic_concordance_extraction_audit.json'
PDF_PATH = ROOT/'raw'/'nic2025_pdf.pdf'
OUT_PATH = ROOT/'concordance'/'nic_concordance_independent_qa.json'

def fail(message):
    raise SystemExit('BLOCKED: '+message)

if not CSV_PATH.exists() or not REPORT_PATH.exists() or not PDF_PATH.exists():
    fail('required CSV, extraction report, or official PDF missing')
report = json.loads(REPORT_PATH.read_text(encoding='utf-8'))
with CSV_PATH.open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
codes = [r.get('nic2025_class_4d','') for r in rows]
duplicates = sorted({x for x in codes if codes.count(x)>1})
reverse = defaultdict(list)
errors = []
for i, row in enumerate(rows, 2):
    code = row['nic2025_class_4d']
    if not re.fullmatch(r'\\d{4}', code): errors.append(f'row {i}: invalid NIC-2025 code')
    try:
        components = json.loads(row['components'])
        fragments = json.loads(row['source_fragments'])
    except Exception as exc:
        errors.append(f'row {i}: invalid JSON fields: {exc}'); continue
    canonical = re.sub(r'\\s+', '', row['nic2008_expression_raw']).upper()
    if canonical != row['nic2008_expression_canonical']:
        errors.append(f'row {i}: raw/canonical expression mismatch')
    if not components: errors.append(f'row {i}: empty mapping components')
    rebuilt = '+'.join(c['nic2008_class_4d'] + ('(P)' if c['partial'] else '') for c in components)
    if rebuilt != canonical:
        errors.append(f'row {i}: component/marker/aggregation mismatch')
    if not fragments: errors.append(f'row {i}: missing source locator')
    elif any(not 232 <= int(x['printed_page']) <= 238 for x in fragments):
        errors.append(f'row {i}: source page outside concordance')
    for c in components:
        if not re.fullmatch(r'\\d{4}', c['nic2008_class_4d']):
            errors.append(f'row {i}: invalid NIC-2008 component')
        reverse[c['nic2008_class_4d']].append(code)
csv_sha = hashlib.sha256(CSV_PATH.read_bytes()).hexdigest()
pdf_sha = hashlib.sha256(PDF_PATH.read_bytes()).hexdigest()
sentinels = {
 '1512':'1512+2220(P)', '1811':'1811+1313(P)', '2611':'2610(P)', '2619':'2610(P)',
 '3101':'3100(P)', '3102':'3100(P)', '3511':'3510(P)', '3512':'3510(P)',
 '3513':'3510(P)', '4772':'4772(P)+4789(P)+4791(P)+4799(P)'
}
by_code = {r['nic2025_class_4d']:r for r in rows}
sentinel_results = {k:(k in by_code and by_code[k]['nic2008_expression_canonical']==v) for k,v in sentinels.items()}
if report.get('status') != 'PASS': errors.append('extractor report is not PASS')
if report.get('csv_sha256') != csv_sha: errors.append('CSV SHA-256 does not match extractor report')
if report.get('source_pdf_sha256') != pdf_sha: errors.append('PDF SHA-256 does not match extractor report')
if len(rows) != 463: errors.append(f'expected 463 rows, found {len(rows)}')
if len(set(codes)) != 463: errors.append(f'expected 463 unique NIC-2025 codes, found {len(set(codes))}')
if duplicates: errors.append('duplicate NIC-2025 codes: '+','.join(duplicates))
if not all(sentinel_results.values()): errors.append('one or more source sentinel mappings mismatch')
result = {
 'status':'PASS' if not errors else 'BLOCKED_WITH_VALIDATION_ERRORS',
 'rows':len(rows),'unique_nic2025_codes':len(set(codes)),'duplicates':duplicates,
 'csv_sha256':csv_sha,'source_pdf_sha256':pdf_sha,
 'reverse_mapping_source_codes':len(reverse),
 'reverse_mapping_one_to_many':{k:sorted(v) for k,v in reverse.items() if len(v)>1},
 'sentinel_checks':sentinel_results,'errors':errors,
 'nic2_iip_weight_bridge':'UNKNOWN_BLOCKED_NOT_INFERRED'
}
OUT_PATH.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(result,indent=2,ensure_ascii=False))
if result['status'] != 'PASS': raise SystemExit(2)
