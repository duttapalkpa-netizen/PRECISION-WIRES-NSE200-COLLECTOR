import json
import tempfile
import unittest
from pathlib import Path

from collector.nse_snapshot_manifest import build_snapshot

HEADER = 'SYMBOL,SERIES,DATE1,OPEN_PRICE,HIGH_PRICE,LOW_PRICE,CLOSE_PRICE,TTL_TRD_QNTY\n'

class SnapshotManifestTests(unittest.TestCase):
    def _fixture(self, root: Path):
        raw = root / 'raw'
        raw.mkdir()
        dates = ['2026-10-29', '2026-10-30']
        (raw / 'sessions.txt').write_text('\n'.join(dates) + '\n')
        (raw / 'acquisition_diagnostics.json').write_text(json.dumps({
            'requested_sessions': 2, 'valid_sessions': 2,
            'diagnostics': [{'date': d, 'status': 'CACHED'} for d in dates]
        }))
        for d, stamp in zip(dates, ('29102026', '30102026')):
            rows = ''.join(f'A{i},EQ,{d},100,105,95,102,10000\n' for i in range(80))
            (raw / f'sec_bhavdata_full_{stamp}.csv').write_text(HEADER + rows)
        return raw

    def test_manifest_hashes_files_and_records_limitations(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = self._fixture(Path(tmp))
            result = build_snapshot(raw, 2)
            manifest = json.loads((raw / result['manifest']).read_text())
            self.assertEqual(result['sessions'], 2)
            self.assertEqual(len(manifest['records']), 2)
            self.assertTrue(all(len(row['sha256']) == 64 for row in manifest['records']))
            self.assertTrue(all(row['schema_validation'] == 'validated' for row in manifest['records']))
            self.assertTrue(all(row['eq_rows'] == 80 for row in manifest['records']))
            self.assertTrue(all(row['source_url'] is None for row in manifest['records']))
            self.assertTrue(manifest['provenance_limitations'])

    def test_manifest_is_idempotent_for_same_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = self._fixture(Path(tmp))
            first = build_snapshot(raw, 2)
            second = build_snapshot(raw, 2)
            self.assertEqual(first['snapshot_id'], second['snapshot_id'])

    def test_rejects_duplicate_sessions(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = self._fixture(Path(tmp))
            (raw / 'sessions.txt').write_text('2026-10-29\n2026-10-29\n')
            with self.assertRaises(RuntimeError):
                build_snapshot(raw, 2)

    def test_rejects_filename_with_wrong_trade_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = self._fixture(Path(tmp))
            path = raw / 'sec_bhavdata_full_29102026.csv'
            rows = ''.join(f'A{i},EQ,2026-10-30,100,105,95,102,10000\n' for i in range(80))
            path.write_text(HEADER + rows)
            with self.assertRaisesRegex(RuntimeError, 'trade-date mismatch'):
                build_snapshot(raw, 2)

    def test_rejects_missing_required_schema(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = self._fixture(Path(tmp))
            path = raw / 'sec_bhavdata_full_29102026.csv'
            path.write_text('SYMBOL,SERIES,DATE1\n' + ''.join(f'A{i},EQ,2026-10-29\n' for i in range(80)))
            with self.assertRaisesRegex(RuntimeError, 'missing required schema'):
                build_snapshot(raw, 2)

if __name__ == '__main__':
    unittest.main()
