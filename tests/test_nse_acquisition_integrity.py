import hashlib
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from collector.nse_download import atomic_write_bytes, response_provenance, validate_full_delivery


class AcquisitionIntegrityTests(unittest.TestCase):
    def test_response_provenance_hashes_exact_response_bytes_for_http_statuses(self):
        payload = b"sample NSE response payload"
        for status in (200, 403, 429, 500):
            response = SimpleNamespace(
                content=payload,
                status_code=status,
                headers={"Content-Type": "application/octet-stream"},
            )
            item = response_provenance("https://example.test/file", response, attempt=2)
            self.assertEqual(item["http_status"], status)
            self.assertEqual(item["bytes"], len(payload))
            self.assertEqual(item["response_sha256"], hashlib.sha256(payload).hexdigest())
            self.assertEqual(item["attempt"], 2)
            self.assertIsNotNone(item["retrieved_at_utc"])

    def test_response_provenance_records_timeout_without_fake_http_response(self):
        item = response_provenance(
            "https://example.test/file", error="ReadTimeout: timed out", attempt=3
        )
        self.assertIsNone(item["http_status"])
        self.assertIsNone(item["content_type"])
        self.assertEqual(item["bytes"], 0)
        self.assertIsNone(item["response_sha256"])
        self.assertEqual(item["error"], "ReadTimeout: timed out")

    def test_atomic_write_replaces_target_and_leaves_no_part_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "session.csv"
            target.write_bytes(b"old")
            atomic_write_bytes(target, b"new complete payload")
            self.assertEqual(target.read_bytes(), b"new complete payload")
            self.assertFalse((Path(tmp) / "session.csv.part").exists())

    def test_atomic_write_failure_preserves_previous_target_and_cleans_part(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "session.csv"
            target.write_bytes(b"known-good")
            with patch("collector.nse_download.os.replace", side_effect=OSError("simulated replace failure")):
                with self.assertRaises(OSError):
                    atomic_write_bytes(target, b"partial-new")
            self.assertEqual(target.read_bytes(), b"known-good")
            self.assertFalse((Path(tmp) / "session.csv.part").exists())

    def test_full_delivery_rejects_wrong_trade_date(self):
        header = "SYMBOL,SERIES,DATE1,CLOSE_PRICE,DELIV_QTY,DELIV_PER\n"
        rows = "".join(
            f"SYM{i},EQ,30-Oct-2026,100,1000,50\n" for i in range(40)
        )
        self.assertFalse(validate_full_delivery((header + rows).encode(), "29102026"))

    def test_full_delivery_accepts_matching_trade_date(self):
        header = "SYMBOL,SERIES,DATE1,CLOSE_PRICE,DELIV_QTY,DELIV_PER\n"
        rows = "".join(
            f"SYM{i},EQ,29-Oct-2026,100,1000,50\n" for i in range(40)
        )
        self.assertTrue(validate_full_delivery((header + rows).encode(), "29102026"))


if __name__ == "__main__":
    unittest.main()
