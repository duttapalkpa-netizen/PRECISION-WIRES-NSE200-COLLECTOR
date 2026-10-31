import json
import tempfile
import unittest
from pathlib import Path

from collector.nse_snapshot_manifest import build_snapshot


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
        for stamp in ('29102026', '30102026'):
            (raw / f'sec_bhavdata_full_{stamp}.csv').write_bytes(b'SYMBOL,SERIES,DATE1,CLOSE_PRICE\n' + b'A,EQ,2026-10-30,100\n' * 80)
        return raw

    def test_manifest_hashes_files_and_records_limitation(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = self._fixture(Path(tmp))
            # Fix fixture date contents so the file-date provenance is explicit in the manifest.
            result = build_snapshot(raw, 2)
            manifest = json.loads((raw / result['manifest']).read_text())
            self.assertEqual(result['sessions'], 2)
            self.assertEqual(len(manifest['records']), 2)
            self.assertTrue(all(len(row['sha256']) == 64 for row in manifest['records']))
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


if __name__ == '__main__':
    unittest.main()