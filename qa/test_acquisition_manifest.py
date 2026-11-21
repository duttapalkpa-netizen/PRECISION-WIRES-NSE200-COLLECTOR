from __future__ import annotations

import hashlib
import tempfile
import unittest
from datetime import date
from pathlib import Path

from collector.nse_download import manifest_entry


class AcquisitionManifestEntryTests(unittest.TestCase):
    def test_cached_file_keeps_provenance_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cached.csv"
            path.write_bytes(b"SYMBOL,CLOSE_PRICE\nABC,123\n")
            row = manifest_entry(date(2026, 11, 20), path)
            self.assertEqual(row["provenance_status"], "UNKNOWN")
            self.assertIsNone(row["source_url"])
            self.assertIsNone(row["retrieved_at_utc"])
            self.assertEqual(row["retained_sha256"], hashlib.sha256(path.read_bytes()).hexdigest())

    def test_fresh_acquisition_records_source_and_retained_hashes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fresh.csv"
            path.write_bytes(b"SYMBOL,CLOSE_PRICE\nABC,123\n")
            source = b"official-source-payload"
            acquisition = {
                "requested_url": "https://example.invalid/request",
                "source_url": "https://example.invalid/final",
                "retrieved_at_utc": "2026-11-21T12:00:00+00:00",
                "source_bytes": len(source),
                "source_sha256": hashlib.sha256(source).hexdigest(),
                "source_content_type": "text/csv",
            }
            row = manifest_entry(date(2026, 11, 20), path, acquisition)
            self.assertEqual(row["provenance_status"], "VERIFIED_AT_ACQUISITION")
            self.assertEqual(row["source_sha256"], hashlib.sha256(source).hexdigest())
            self.assertEqual(row["retained_sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertNotEqual(row["source_sha256"], row["retained_sha256"])


if __name__ == "__main__":
    unittest.main()
