#!/usr/bin/env python3
"""Create a content-addressed, immutable manifest for a validated NSE raw snapshot."""
from __future__ import annotations
import argparse, csv, hashlib, json, os
from datetime import date, datetime, timezone
from pathlib import Path

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''): h.update(chunk)
    return h.hexdigest()

def atomic_write(path: Path, payload: bytes) -> None:
    tmp = path.with_name(path.name + '.part')
    with tmp.open('wb') as handle:
        handle.write(payload); handle.flush(); os.fsync(handle.fileno())
    os.replace(tmp, path)

def _key(value: str) -> str:
    return ''.join(ch for ch in str(value).strip().upper() if ch.isalnum())

def _parse_trade_date(value: str):
    value = str(value or '').strip()
    for fmt in ('%Y-%m-%d', '%Y%m%d', '%d-%m-%Y', '%d/%m/%Y', '%d-%b-%Y'):
        try: return datetime.strptime(value, fmt).date()
        except ValueError: pass
    return None

def validate_session_csv(path: Path, expected_date: date) -> dict:
    """Validate actual EQ row dates and downstream-required OHLCV schema."""
    with path.open('r', encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames: raise RuntimeError(f'empty CSV header: {path.name}')
        cols = {_key(name): name for name in reader.fieldnames}
        def find(*aliases):
            return next((cols[_key(name)] for name in aliases if _key(name) in cols), None)
        symbol_col, series_col = find('SYMBOL','TCKRSYMB'), find('SERIES','SCTYSRS')
        date_col = find('DATE1','TRADDT','TRADGDATE','DATE')
        numeric_cols = {
            'OPEN_PRICE': find('OPEN_PRICE','OPEN','OPNPRIC'),
            'HIGH_PRICE': find('HIGH_PRICE','HIGH','HG HPRIC'.replace(' ','')),
            'LOW_PRICE': find('LOW_PRICE','LOW','LWPRIC'),
            'CLOSE_PRICE': find('CLOSE_PRICE','CLOSEPRICE','CLSPRIC','CLOSE'),
            'TTL_TRD_QNTY': find('TTL_TRD_QNTY','TOTTRDQTY','TTLTRADGVOL','TTLTTRADQTY'),
        }
        missing = [n for n,c in [('symbol',symbol_col),('series',series_col),('trade_date',date_col)] if not c]
        missing += [n for n,c in numeric_cols.items() if not c]
        if missing: raise RuntimeError(f'{path.name}: missing required schema fields: {missing}')
        count, dates = 0, set()
        valid = {n:0 for n in numeric_cols}; positive = {n:0 for n in numeric_cols}
        for row in reader:
            if str(row.get(series_col,'')).strip().upper() != 'EQ': continue
            if not str(row.get(symbol_col,'')).strip(): raise RuntimeError(f'{path.name}: blank EQ symbol')
            count += 1
            parsed = _parse_trade_date(row.get(date_col,''))
            if parsed is None: raise RuntimeError(f'{path.name}: unparseable EQ trade date')
            dates.add(parsed)
            for name,col in numeric_cols.items():
                try: number = float(str(row.get(col,'')).replace(',','').strip())
                except (TypeError,ValueError): continue
                if number == number and abs(number) != float('inf'):
                    valid[name] += 1
                    if number > 0: positive[name] += 1
        if not count: raise RuntimeError(f'{path.name}: no EQ rows')
        if dates != {expected_date}:
            raise RuntimeError(f'{path.name}: trade-date mismatch expected={expected_date} observed={sorted(dates)}')
        for name in numeric_cols:
            if valid[name] < max(10,int(count*0.80)) or positive[name] != valid[name]:
                raise RuntimeError(f'{path.name}: invalid {name}; numeric={valid[name]}/{count}, positive={positive[name]}')
        return {'eq_rows':count,'schema_validation':'validated'}

def build_snapshot(raw_dir: Path, expected_sessions: int) -> dict:
    sessions_path, diagnostics_path = raw_dir/'sessions.txt', raw_dir/'acquisition_diagnostics.json'
    if not sessions_path.is_file() or not diagnostics_path.is_file():
        raise RuntimeError('sessions.txt or acquisition_diagnostics.json missing')
    sessions = [x.strip() for x in sessions_path.read_text().splitlines() if x.strip()]
    if len(sessions) != expected_sessions or len(set(sessions)) != len(sessions):
        raise RuntimeError(f'expected {expected_sessions} unique sessions, got {len(sessions)}')
    diagnostics = json.loads(diagnostics_path.read_text())
    diagnostic_by_date = {x['date']:x for x in diagnostics.get('diagnostics',[])}
    status_by_date = {k:v.get('status','UNKNOWN') for k,v in diagnostic_by_date.items()}
    records = []
    for session in sorted(sessions):
        d = date.fromisoformat(session); filename=f"sec_bhavdata_full_{d.strftime('%d%m%Y')}.csv"; path=raw_dir/filename
        if not path.is_file() or path.stat().st_size < 1000: raise RuntimeError(f'missing or undersized session file: {filename}')
        validation = validate_session_csv(path,d)
        acquisition = diagnostic_by_date.get(session, {})
        status = status_by_date.get(session,'UNKNOWN')
        if status in ('MISS','UNKNOWN'): raise RuntimeError(f'no successful acquisition provenance for {session}: {status}')
        attempts = acquisition.get('attempts', [])
        source_url = acquisition.get('source_url')
        if status != 'CACHED' and not source_url:
            raise RuntimeError(f'missing successful source URL for network-acquired session {session}')
        successful_attempt = next((x for x in reversed(attempts)
            if x.get('url') == source_url and x.get('http_status') == 200), {})
        if status != 'CACHED' and not successful_attempt:
            raise RuntimeError(f'missing HTTP 200 provenance record for {session}')
        source_map = {
            'CACHED':'validated-existing-cache (original network source not recoverable from legacy cache)',
            'OK_FULL_BHAVCOPY_DELIVERY':'NSE CM Full Bhavcopy + Security Deliverable report',
            'OK':'NSE UDiFF or legacy fallback; exact endpoint not persisted by legacy collector',
        }
        records.append({'trade_date':session,'file':filename,'bytes':path.stat().st_size,'sha256':sha256_file(path),
            'eq_rows':validation['eq_rows'],'schema_validation':validation['schema_validation'],
            'acquisition_status':status,'source_provenance':source_map.get(status,'unresolved'),
            'source_url':source_url,'cache_origin':acquisition.get('cache_origin'),
            'successful_response':successful_attempt or None,'attempts':attempts,
            'retrieved_at_utc':(successful_attempt.get('retrieved_at_utc') if successful_attempt else None)
                or datetime.fromtimestamp(path.stat().st_mtime,timezone.utc).isoformat()})
    canonical=''.join(json.dumps(r,sort_keys=True,separators=(',',':'))+'\n' for r in records).encode()
    snapshot_id=hashlib.sha256(canonical).hexdigest()
    manifest={'schema_version':2,'snapshot_id':snapshot_id,'created_at_utc':datetime.now(timezone.utc).isoformat(),
        'expected_sessions':expected_sessions,'actual_sessions':len(records),'first_session':records[0]['trade_date'],
        'last_session':records[-1]['trade_date'],'records':records,'provenance_limitations':[
        'For pre-existing legacy cache files, the original network source and retrieval time are unavailable.',
        'Pre-existing legacy cache records have no original URL or authoritative network retrieval timestamp.',
        'File mtime is recorded as a local retrieval proxy, not as an authoritative server publication timestamp.']}
    output=raw_dir/f'nse_snapshot_manifest_{snapshot_id[:16]}.json'
    if output.exists():
        existing=json.loads(output.read_text())
        if existing.get('snapshot_id') != snapshot_id or existing.get('records') != records:
            raise RuntimeError(f'content-addressed manifest path collision: {output.name}')
    else: atomic_write(output,(json.dumps(manifest,indent=2,sort_keys=True)+'\n').encode())
    return {'snapshot_id':snapshot_id,'manifest':output.name,'sessions':len(records),'sha256':sha256_file(output)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--raw-dir',default='data/raw'); ap.add_argument('--sessions',type=int,default=200)
    args=ap.parse_args(); print(json.dumps(build_snapshot(Path(args.raw_dir),args.sessions),indent=2,sort_keys=True))

if __name__=='__main__': main()
