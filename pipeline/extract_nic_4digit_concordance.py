#!/usr/bin/env python3
"""Fail-closed extraction of MoSPI's NIC-2025/NIC-2008 4-digit concordance."""
from __future__ import annotations
import csv, hashlib, json, re
from collections import defaultdict
from pathlib import Path
import fitz

ROOT = Path('artifacts/nic_concordance_audit')
PDF = ROOT / 'raw' / 'nic2025_pdf.pdf'
OUT = ROOT / 'concordance'
SOURCE_URL = 'https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf'
HEADING = re.compile(r'CONCORDANCE\\s+BETWEEN\\s+4-DIGIT\\s+INDUSTRY\\s+CLASSES\\s+OF\\s+NIC-2025\\s+AND\\s+NIC-2008', re.I)
CODE_ROW = re.compile(r'^\\s*(\\d{4})\\s+(.+?)\\s*$')
EXPR_ONLY = re.compile(r'^\\s*(\\d{4}(?:\\s*\\(\\s*p\\s*\\))?(?:\\s*\\+\\s*\\d{4}(?:\\s*\\(\\s*p\\s*\\))?)*)\\s*$')
TOKEN = re.compile(r'^(\\d{4})(\\(P\\))?$', re.I)
HEADER_LINES = {'NIC 2025 Code', 'NIC 2008 Code', 'NIC 2025 Code NIC 2008 Code'}

def normalize_expr(raw: str) -> str:
    return re.sub(r'\\s+', '', raw).upper()

def parse_components(expr: str, allow_trailing_plus: bool = False):
    canonical = normalize_expr(expr)
    if allow_trailing_plus and canonical.endswith('+'):
        canonical_body = canonical[:-1]
    else:
        canonical_body = canonical
    if not canonical_body or (not allow_trailing_plus and canonical.endswith('+')):
        return None
    parsed = []
    for part in canonical_body.split('+'):
        token = TOKEN.fullmatch(part)
        if not token:
            return None
        parsed.append({'nic2008_class_4d': token.group(1), 'partial': bool(token.group(2))})
    return parsed

def is_header_or_layout(line: str) -> bool:
    s = re.sub(r'\\s+', ' ', line).strip()
    return not s or s in HEADER_LINES or s.lower() in {'concordance with nic 2008'}

def parse_lines(lines, printed_page: int):
    """Attach a blank-code continuation only to an immediately open trailing '+' row."""
    rows, pending = [], None
    for line_no, line in enumerate(lines, 1):
        raw_line = line.rstrip('\\r\\n')
        if is_header_or_layout(raw_line):
            continue
        m = CODE_ROW.fullmatch(raw_line)
        if m:
            if pending:
                raise ValueError(f"unresolved continuation before next NIC-2025 row at printed page {printed_page}, line {line_no}")
            code, expr = m.groups()
            canonical = normalize_expr(expr)
            components = parse_components(expr, allow_trailing_plus=True)
            if components is None:
                continue
            rec = {'nic2025_class_4d': code, 'nic2008_expression_raw': expr.strip(),
                   'nic2008_expression_canonical': canonical,
                   'source_fragments': [{'printed_page': printed_page, 'line': line_no, 'raw': expr.strip()}]}
            if canonical.endswith('+'):
                pending = rec
            else:
                rec['components'] = parse_components(expr)
                rows.append(rec)
            continue
        if pending:
            cm = EXPR_ONLY.fullmatch(raw_line)
            if not cm:
                raise ValueError(f"ambiguous/non-expression line while NIC-2025 {pending['nic2025_class_4d']} awaits continuation at page {printed_page}, line {line_no}: {raw_line!r}")
            fragment = raw_line.strip()
            pending['nic2008_expression_raw'] += ' ' + fragment
            pending['nic2008_expression_canonical'] += normalize_expr(fragment)
            pending['source_fragments'].append({'printed_page': printed_page, 'line': line_no, 'raw': fragment})
            if pending['nic2008_expression_canonical'].endswith('+'):
                continue
            pending['components'] = parse_components(pending['nic2008_expression_canonical'])
            rows.append(pending)
            pending = None
            continue
        if EXPR_ONLY.fullmatch(raw_line):
            raise ValueError(f'orphan continuation-like row at printed page {printed_page}, line {line_no}: {raw_line!r}')
    if pending:
        raise ValueError(f"unresolved trailing '+' for NIC-2025 {pending['nic2025_class_4d']}")
    return rows

def build_report(records, pdf_bytes: bytes, csv_path: Path):
    codes = [r['nic2025_class_4d'] for r in records]
    duplicates = sorted({c for c in codes if codes.count(c) > 1})
    reverse = defaultdict(list)
    malformed = []
    for r in records:
        comps = r.get('components') or []
        if not comps:
            malformed.append(r['nic2025_class_4d'])
            continue
        for c in comps:
            reverse[c['nic2008_class_4d']].append(r['nic2025_class_4d'])
    return {
        'status': 'PASS' if len(records) == 463 and len(set(codes)) == 463 and not malformed and not duplicates else 'BLOCKED_WITH_COVERAGE_OR_VALIDATION_GAP',
        'source_pdf_url': SOURCE_URL,
        'source_pdf_sha256': hashlib.sha256(pdf_bytes).hexdigest(),
        'source_pdf_bytes': len(pdf_bytes),
        'source_printed_pages': [232, 238],
        'rows_extracted': len(records), 'unique_nic2025_codes': len(set(codes)),
        'duplicate_nic2025_codes': duplicates, 'malformed_rows': malformed,
        'expected_nic2025_class_count': 463,
        'partial_rows': sum(any(x['partial'] for x in r['components']) for r in records),
        'aggregation_rows': sum(len(r['components']) > 1 for r in records),
        'reverse_mapping_source_code_count': len(reverse),
        'reverse_mapping_one_to_many_source_codes': {k: sorted(v) for k,v in reverse.items() if len(v)>1},
        'csv_sha256': hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        'nic2_rollup_status': 'NOT_CERTIFIED: NIC class concordance does not establish IIP item-group or weight correspondence'
    }

# Parser regression checks include the exact documented page/table continuation.
assert parse_components('0113+0128(p)') == [{'nic2008_class_4d':'0113','partial':False},{'nic2008_class_4d':'0128','partial':True}]
assert len(parse_components('0311(p)+0312(p)+0321(p)+0322(p)')) == 4
_test = parse_lines(['4772 4772(p)+4789(p)+4791(p)+', 'NIC 2025 Code', 'NIC 2008 Code', '4799(p)'], 235)
assert len(_test) == 1 and _test[0]['nic2008_expression_canonical'] == '4772(P)+4789(P)+4791(P)+4799(P)'

def main():
    if not PDF.exists():
        raise SystemExit('BLOCKED: official NIC-2025 PDF binary not acquired')
    pdf_bytes = PDF.read_bytes()
    doc = fitz.open(stream=pdf_bytes, filetype='pdf')
    start = next((i for i,p in enumerate(doc) if HEADING.search(p.get_text('text'))), None)
    if start is None:
        raise SystemExit('BLOCKED: official concordance heading not found')
    records = []
    for offset, page_no in enumerate(range(start, min(start + 7, len(doc)))):
        records.extend(parse_lines(doc[page_no].get_text('text', sort=True).splitlines(), 232 + offset))
    if not records:
        raise SystemExit('BLOCKED: no concordance rows extracted; inspect source layout')
    records.sort(key=lambda x: x['nic2025_class_4d'])
    codes = [r['nic2025_class_4d'] for r in records]
    if len(codes) != len(set(codes)):
        dup = sorted({c for c in codes if codes.count(c)>1})
        raise SystemExit(f'BLOCKED: duplicate NIC-2025 codes: {dup}')
    OUT.mkdir(parents=True, exist_ok=True)
    csv_path = OUT/'nic2025_to_nic2008_4digit_concordance.csv'
    fields = ['nic2025_class_4d','nic2008_expression_raw','nic2008_expression_canonical','components','source_fragments']
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in records:
            w.writerow({**r, 'components':json.dumps(r['components'],ensure_ascii=False), 'source_fragments':json.dumps(r['source_fragments'],ensure_ascii=False)})
    report = build_report(records, pdf_bytes, csv_path)
    by_code = {r['nic2025_class_4d']:r for r in records}
    expected = {'1512':'1512+2220(P)', '1811':'1811+1313(P)', '2611':'2610(P)', '2619':'2610(P)', '3101':'3100(P)', '3102':'3100(P)', '3511':'3510(P)', '3512':'3510(P)', '3513':'3510(P)', '4772':'4772(P)+4789(P)+4791(P)+4799(P)'}
    report['sentinel_checks'] = {k: (k in by_code and by_code[k]['nic2008_expression_canonical'] == v) for k,v in expected.items()}
    if not all(report['sentinel_checks'].values()):
        report['status'] = 'BLOCKED_WITH_SENTINEL_MISMATCH'
    (OUT/'nic_concordance_extraction_audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(report,indent=2,ensure_ascii=False))
    if report['status'] != 'PASS':
        raise SystemExit(2)

if __name__ == '__main__':
    main()
