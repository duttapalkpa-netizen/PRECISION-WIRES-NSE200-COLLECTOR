"""Offline unit tests for the isolated NSE FII/DII capture utility."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[2] / "capture_nse_fii_dii.py"
spec = importlib.util.spec_from_file_location("capture_nse_fii_dii", MODULE_PATH)
capture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture)

class CaptureUtilityTests(unittest.TestCase):
    def test_https_official_hosts_allowed(self):
        self.assertTrue(capture.safe_nse_url("https://www.nseindia.com/reports/x"))
        self.assertTrue(capture.safe_nse_url("https://archives.nseindia.com/file.csv"))
        self.assertTrue(capture.safe_nse_url("https://www.nseindia.in/file.csv"))

    def test_non_https_and_non_official_hosts_rejected(self):
        for url in (
            "http://www.nseindia.com/file.csv",
            "https://nseindia.com.evil.example/file.csv",
            "https://evilnseindia.com/file.csv",
            "https://example.com/?next=nseindia.com",
            "javascript://nseindia.com/file.csv",
            "https://user:pass@nseindia.com/file.csv",
            "https://nseindia.com:444/file.csv",
            "not-a-url",
        ):
            with self.subTest(url=url):
                self.assertFalse(capture.safe_nse_url(url))

    def test_invalid_port_does_not_raise(self):
        self.assertFalse(capture.safe_nse_url("https://nseindia.com:bad/file.csv"))

    def test_manifest_url_drops_query_and_fragment(self):
        self.assertEqual(
            capture.manifest_url("https://www.nseindia.com/file.csv?token=secret&date=2026-11-13#x"),
            "https://www.nseindia.com/file.csv",
        )

    def test_sha256_known_vector(self):
        self.assertEqual(
            capture.sha(b"abc"),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        )

    def test_anchor_parser_preserves_label_and_href(self):
        parser = capture.AnchorParser()
        parser.feed('<a href="/one.csv">FII/DII activity on NSE in Capital Market Segment</a>')
        self.assertEqual(parser.items, [
            ("/one.csv", "FII/DII activity on NSE in Capital Market Segment")
        ])

    def test_write_bytes_returns_hash_and_length(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "payload.bin"
            result = capture.write_bytes(path, b"payload")
            self.assertEqual(path.read_bytes(), b"payload")
            self.assertEqual(result["bytes"], 7)
            self.assertEqual(result["sha256"], capture.sha(b"payload"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
