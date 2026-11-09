#!/usr/bin/env python3
"""Bounded official NIC source acquisition and workbook inventory; research-only."""
from __future__ import annotations
import hashlib, json, os, time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from openpyxl import load_workbook

OUT = Path('artifacts/nic_concordance_audit')
RAW = OUT / 'raw'
RAW.mkdir(parents=True, exist_ok=True)
SOURCES = {
  'nic2025_xlsx': 'https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763618655097_29a4a622-fa4c-47e9-abba-b549e27a1bbb_NIC_2025.xlsx',
  'nic2008_xlsx': 'https://www.mospi.gov.in/uploads/documents/publicDocuments/1760616763355-NIC_2008.xlsx',
  'nic2025_pdf': 'https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf',
}
def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''): h.update(chunk)
    return h.hexdigest()
manifest = {'purpose':'official NIC source acquisition; no production changes','sources':{},'workbooks':{},'status':'PARTIAL'}
for key, url in SOURCES.items():
    ext = '.xlsx' if key.endswith('xlsx') else '.pdf'
    dest = RAW / f'{key}{ext}'
    rec = {'url':url,'status':'PENDING','path':str(dest)}
    for attempt in range(1, 4):
        try:
            req = Request(url, headers={'User-Agent':'PRECISION-WIRES-research-audit/1.0'})
            with urlopen(req, timeout=35) as resp, dest.open('wb') as out:
                rec['http_status'] = getattr(resp, 'status', None)
                while True:
                    chunk = resp.read(1024 * 1024)
                    if not chunk: break
                    out.write(chunk)
            if dest.stat().st_size < 1024: raise ValueError('download too small; likely error page')
            rec.update({'status':'DOWNLOADED','bytes':dest.stat().st_size,'sha256':sha256(dest),'attempt':attempt})
            break
        except Exception as exc:
            rec.update({'status':'FAILED','attempt':attempt,'error':f'{type(exc).__name__}: {exc}'})
            if dest.exists(): dest.unlink()
            if attempt < 3: time.sleep(attempt * 2)
    manifest['sources'][key] = rec
    if key.endswith('xlsx') and rec['status'] == 'DOWNLOADED':
        try:
            wb = load_workbook(dest, read_only=True, data_only=True)
            sheets = []
            for ws in wb.worksheets:
                first = next(ws.iter_rows(min_row=1, max_row=min(ws.max_row or 1, 5), values_only=True), ())
                sheets.append({'title':ws.title,'max_row':ws.max_row,'max_column':ws.max_column,'first_rows':[list(row) for row in first]})
            manifest['workbooks'][key] = {'sheetnames':wb.sheetnames,'sheets':sheets}
            wb.close()
        except Exception as exc:
            manifest['workbooks'][key] = {'inventory_status':'FAILED','error':f'{type(exc).__name__}: {exc}'}
manifest['status'] = 'PASS' if all(x['status']=='DOWNLOADED' for x in manifest['sources'].values()) else 'BLOCKED_WITH_SOURCE_ACCESS_GAPS'
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'nic_source_sha256_and_workbook_inventory.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False, default=str), encoding='utf-8')
print(json.dumps({k:{'status':v['status'],'bytes':v.get('bytes'),'sha256':v.get('sha256'),'error':v.get('error')} for k,v in manifest['sources'].items()}, indent=2))
print('OVERALL:', manifest['status'])
