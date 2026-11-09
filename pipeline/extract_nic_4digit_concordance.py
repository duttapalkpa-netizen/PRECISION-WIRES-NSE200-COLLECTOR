#!/usr/bin/env python3
"""Fail-closed table-cell extraction of MoSPI NIC-2025/NIC-2008 concordance."""
from __future__ import annotations
import csv, hashlib, json, re
from collections import defaultdict
from pathlib import Path
import fitz

ROOT = Path('artifacts/nic_concordance_audit')
PDF = ROOT / 'raw' / 'nic2025_pdf.pdf'
OUT = ROOT / 'concordance'
SOURCE_URL = 'https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf'
HEADING = re.compile(r'CONCORDANCE\s+BETWEEN\s+4-DIGIT\s+INDUSTRY\s+CLASSES\s+OF\s+NIC-2025\s+AND\s+NIC-2008', re.I)
CODE = re.compile(r'^\d{4}$')
TOKEN = re.compile(r'^(\d{4})(\(P\))?$', re.I)

def normalize_expr(raw: str) -> str:
    return re.sub(r'\s+', '', raw).upper()

def parse_components(expr: str):
    canonical = normalize_expr(expr)
    if not canonical or canonical.endswith('+'):
        return None
    result = []
    for part in canonical.split('+'):
        m = TOKEN.fullmatch(part)
        if not m:
            return None
        result.append({'nic2008_class_4d': m.group(1), 'partial': bool(m.group(2))})
    return result

def parse_tables(page_tables, printed_page: int):
    """Read actual PDF 2-column cells; attach blank-code continuation only after trailing '+'."""
    records, pending = [], None
    seen_table = 0
    for table_index, table in enumerate(page_tables):
        if table.col_count != 2:
            raise ValueError(f'page {printed_page} table {table_index}: expected 2 columns, found {table.col_count}')
        extracted = table.extract()
        if not extracted:
            continue
        seen_table += 1
        for row_index, cells in enumerate(extracted):
            left = '' if cells[0] is None else str(cells[0]).strip()
            right = '' if cells[1] is None else str(cells[1]).strip()
            if not left and not right:
                continue
            left_header = re.sub(r'\s+', '', left).upper()
            right_header = re.sub(r'\s+', '', right).upper()
            if 'NIC2025CODE' in left_header or 'NIC2008CODE' in right_header:
                continue
            if CODE.fullmatch(left):
                if pending:
                    raise ValueError(f'unresolved continuation for {pending["nic2025_class_4d"]} before new row on page {printed_page}')
                canonical = normalize_expr(right)
                if not canonical:
                    raise ValueError(f'empty NIC-2008 mapping for NIC-2025 {left} on page {printed_page}')
                is_open = canonical.endswith('+')
                body = canonical[:-1] if is_open else canonical
                parts = body.split('+')
                if not parts or any(not TOKEN.fullmatch(p) for p in parts):
                    raise ValueError(f'malformed NIC-2008 expression for {left}: {right!r}')
                rec = {
                    'nic2025_class_4d': left,
                    'nic2008_expression_raw': right,
                    'nic2008_expression_canonical': canonical,
                    'source_fragments': [{'printed_page': printed_page, 'table_index': table_index, 'row_index': row_index, 'raw': right}]
                }
                if is_open:
                    pending = rec
                else:
                    rec['components'] = parse_components(canonical)
                    records.append(rec)
            elif not left and right:
                if not pending:
                    raise ValueError(f'orphan blank-code table row on page {printed_page}: {right!r}')
                pending['nic2008_expression_raw'] += ' ' + right
                pending['nic2008_expression_canonical'] += normalize_expr(right)
                pending['source_fragments'].append({'printed_page': printed_page, 'table_index': table_index, 'row_index': row_index, 'raw': right})
                if pending['nic2008_expression_canonical'].endswith('+'):
                    continue
                pending['components'] = parse_components(pending['nic2008_expression_canonical'])
                if not pending['components']:
                    raise ValueError(f'invalid reconstructed expression for {pending["nic2025_class_4d"]}')
                records.append(pending)
                pending = None
            else:
                raise ValueError(f'ambiguous table row on page {printed_page}: {cells!r}')
    if pending:
        raise ValueError(f'unresolved trailing plus for NIC-2025 {pending["nic2025_class_4d"]}')
    if not seen_table:
        raise ValueError(f'no 2-column concordance table found on printed page {printed_page}')
    return records

def build_report(records, pdf_bytes, csv_path):
    codes = [r['nic2025_class_4d'] for r in records]
    duplicates = sorted({c for c in codes if codes.count(c) > 1})
    reverse = defaultdict(list)
    for r in records:
        for c in r['components']:
            reverse[c['nic2008_class_4d']].append(r['nic2025_class_4d'])
    return {
        'status': 'PASS' if len(records) == 463 and len(set(codes)) == 463 and not duplicates else 'BLOCKED_WITH_COVERAGE_OR_DUPLICATE_GAP',
        'source_pdf_url': SOURCE_URL,
        'source_pdf_sha256': hashlib.sha256(pdf_bytes).hexdigest(),
        'source_pdf_bytes': len(pdf_bytes),
        'source_printed_pages': [232, 238],
        'rows_extracted': len(records),
        'unique_nic2025_codes': len(set(codes)),
        'duplicate_nic2025_codes': duplicates,
        'expected_nic2025_class_count': 463,
        'partial_rows': sum(any(c['partial'] for c in r['components']) for r in records),
        'aggregation_rows': sum(len(r['components']) > 1 for r in records),
        'reverse_mapping_source_code_count': len(reverse),
        'reverse_mapping_one_to_many_source_codes': {k: sorted(v) for k, v in reverse.items() if len(v) > 1},
        'csv_sha256': hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        'nic2_rollup_status': 'NOT_CERTIFIED: NIC class concordance does not establish IIP item-group or weight correspondence'
    }

def main():
    if not PDF.exists():
        raise SystemExit('BLOCKED: official NIC-2025 PDF binary not acquired')
    pdf_bytes = PDF.read_bytes()
    doc = fitz.open(stream=pdf_bytes, filetype='pdf')
    start = next((i for i, p in enumerate(doc) if HEADING.search(p.get_text('text')) and 'The following table shows links between NIC-2025 and NIC-2008' in p.get_text('text')), None)
    if start is None:
        raise SystemExit('BLOCKED: official concordance table heading not found')
    records = []
    for offset, page_no in enumerate(range(start, start + 7)):
        page = doc[page_no]
        page_text = page.get_text('text')
        printed = [int(x) for x in re.findall(r'^\s*(23[2-8])\s*$', page_text, re.M)]
        expected_page = 232 + offset
        if expected_page not in printed:
            raise SystemExit(f'BLOCKED: expected printed page {expected_page}, observed footer values {printed}')
        records.extend(parse_tables(page.find_tables().tables, expected_page))
    records.sort(key=lambda r: r['nic2025_class_4d'])
    codes = [r['nic2025_class_4d'] for r in records]
    if len(codes) != len(set(codes)):
        duplicates = sorted({c for c in codes if codes.count(c) > 1})
        raise SystemExit(f'BLOCKED: duplicate NIC-2025 classes: {duplicates}')
    OUT.mkdir(parents=True, exist_ok=True)
    csv_path = OUT / 'nic2025_to_nic2008_4digit_concordance.csv'
    fields = ['nic2025_class_4d', 'nic2008_expression_raw', 'nic2008_expression_canonical', 'components', 'source_fragments']
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in records:
            writer.writerow({**row, 'components': json.dumps(row['components'], ensure_ascii=False), 'source_fragments': json.dumps(row['source_fragments'], ensure_ascii=False)})
    report = build_report(records, pdf_bytes, csv_path)
    by_code = {r['nic2025_class_4d']: r for r in records}
    expected = {
        '1512': '1512+2220(P)', '1811': '1811+1313(P)', '2611': '2610(P)', '2619': '2610(P)',
        '3101': '3100(P)', '3102': '3100(P)', '3511': '3510(P)', '3512': '3510(P)',
        '3513': '3510(P)', '4772': '4772(P)+4789(P)+4791(P)+4799(P)'
    }
    report['sentinel_checks'] = {k: (k in by_code and by_code[k]['nic2008_expression_canonical'] == v) for k, v in expected.items()}
    if not all(report['sentinel_checks'].values()):
        report['status'] = 'BLOCKED_WITH_SENTINEL_MISMATCH'
    (OUT / 'nic_concordance_extraction_audit.json').write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if report['status'] != 'PASS':
        raise SystemExit(2)

if __name__ == '__main__':
    main()
