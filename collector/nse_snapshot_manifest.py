#!/usr/bin/env python3
"""Create a content-addressed, immutable manifest for the NSE raw session snapshot."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def atomic_write(path: Path, payload: bytes) -> None:
    tmp = path.with_name(path.name + '.part')
    with tmp.open('wb') as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)

def build_snapshot(raw_dir: Path, expected_sessions: int) -> dict:
    sessions_path = raw_dir / 'sessions.txt'
    diagnostics_path = raw_dir / 'acquisition_diagnostics.json'
    if not sessions_path.is_file() or not diagnostics_path.is_file():
        raise RuntimeError('sessions.txt or acquisition_diagnostics.json missing')
    sessions = [x.strip() for x in sessions_path.read_text().splitlines() if x.strip()]
    if len(sessions) != expected_sessions or len(set(sessions)) != len(sessions):
        raise RuntimeError(f'expected {expected_sessions} unique sessions, got {len(sessions)}')
    diagnostics = json.loads(diagnostics_path.read_text())
    status_by_date = {x['date']: x['status'] for x in diagnostics.get('diagnostics', [])}
    records = []
    for session in sorted(sessions):
        from datetime import date
        d = date.fromisoformat(session)
        filename = f"sec_bhavdata_full_{d.strftime('%d%m%Y')}.csv"
        path = raw_dir / filename
        if not path.is_file() or path.stat().st_size < 1000:
            raise RuntimeError(f'missing or undersized session file: {filename}')
        digest = sha256_file(path)
        status = status_by_date.get(session, 'UNKNOWN')
        if status == 'MISS' or status == 'UNKNOWN':
            raise RuntimeError(f'no successful acquisition provenance for {session}: {status}')
        source_map = {
            'CACHED': 'validated-existing-cache (original network source not recoverable from legacy cache)',
            'OK_FULL_BHAVCOPY_DELIVERY': 'NSE CM Full Bhavcopy + Security Deliverable report',
            'OK': 'NSE UDiFF or legacy fallback; exact endpoint not persisted by legacy collector',
        }
        records.append({
            'trade_date': session,
            'file': filename,
            'bytes': path.stat().st_size,
            'sha256': digest,
            'acquisition_status': status,
            'source_provenance': source_map.get(status, 'unresolved'),
            'source_url': None,
            'retrieved_at_utc': datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
        })
    canonical = ''.join(json.dumps(r, sort_keys=True, separators=(',', ':')) + '\n' for r in records).encode()
    snapshot_id = hashlib.sha256(canonical).hexdigest()
    manifest = {
        'schema_version': 1,
        'snapshot_id': snapshot_id,
        'created_at_utc': datetime.now(timezone.utc).isoformat(),
        'expected_sessions': expected_sessions,
        'actual_sessions': len(records),
        'first_session': records[0]['trade_date'],
        'last_session': records[-1]['trade_date'],
        'records': records,
        'provenance_limitations': [
            'For pre-existing legacy cache files, the original network source and retrieval time are unavailable.',
            'The current collector does not persist the exact URL chosen for UDiFF versus legacy fallback; source_url is null for those records.',
            'File mtime is recorded as a local retrieval proxy, not as an authoritative server publication timestamp.',
        ],
    }
    output = raw_dir / f'nse_snapshot_manifest_{snapshot_id[:16]}.json'
    if output.exists():
        existing = json.loads(output.read_text())
        if existing.get('snapshot_id') != snapshot_id or existing.get('records') != records:
            raise RuntimeError(f'content-addressed manifest path collision: {output.name}')
    else:
        atomic_write(output, (json.dumps(manifest, indent=2, sort_keys=True) + '\n').encode())
    return {'snapshot_id': snapshot_id, 'manifest': output.name, 'sessions': len(records), 'sha256': sha256_file(output)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw-dir', default='data/raw')
    ap.add_argument('--sessions', type=int, default=200)
    args = ap.parse_args()
    result = build_snapshot(Path(args.raw_dir), args.sessions)
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()