import hashlib
import importlib.util
import tempfile
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "research" / "acquire_nic_concordance_source.py"
SPEC = importlib.util.spec_from_file_location("acquire_nic_concordance_source", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FakeResponse:
    def __init__(self, payload, url=None, content_type="application/pdf"):
        self.payload = payload
        self.offset = 0
        self.headers = {"Content-Type": content_type}
        self.url = url or MODULE.SOURCE_URL

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def geturl(self):
        return self.url

    def read(self, size=-1):
        if size < 0:
            size = len(self.payload) - self.offset
        part = self.payload[self.offset:self.offset + size]
        self.offset += len(part)
        return part


class AcquisitionTests(unittest.TestCase):
    def test_download_archives_pdf_and_records_sha256(self):
        payload = b"%PDF-" + (b"x" * 120000)
        with tempfile.TemporaryDirectory() as td:
            destination = Path(td) / "source.pdf"
            with patch.object(MODULE, "urlopen", return_value=FakeResponse(payload)):
                manifest = MODULE.acquire_pdf(destination)
            self.assertEqual(destination.read_bytes(), payload)
            self.assertEqual(manifest["bytes"], len(payload))
            self.assertEqual(manifest["sha256"], hashlib.sha256(payload).hexdigest())
            self.assertEqual(manifest["final_url"], MODULE.SOURCE_URL)

    def test_rejects_untrusted_redirect_host(self):
        payload = b"%PDF-" + (b"x" * 120000)
        with tempfile.TemporaryDirectory() as td:
            with patch.object(MODULE, "urlopen", return_value=FakeResponse(payload, "https://evil.example/file.pdf")):
                with self.assertRaisesRegex(ValueError, "Unexpected redirect host"):
                    MODULE.acquire_pdf(Path(td) / "source.pdf")

    def test_rejects_wrong_content_type(self):
        payload = b"%PDF-" + (b"x" * 120000)
        with tempfile.TemporaryDirectory() as td:
            response = FakeResponse(payload, content_type="text/html")
            with patch.object(MODULE, "urlopen", return_value=response):
                with self.assertRaisesRegex(ValueError, "Unexpected content type"):
                    MODULE.acquire_pdf(Path(td) / "source.pdf")

    def test_rejects_non_pdf_payload(self):
        payload = b"<!DOCTYPE html>" + (b"x" * 120000)
        with tempfile.TemporaryDirectory() as td:
            with patch.object(MODULE, "urlopen", return_value=FakeResponse(payload)):
                with self.assertRaisesRegex(ValueError, "PDF signature"):
                    MODULE.acquire_pdf(Path(td) / "source.pdf")

    def test_rejects_short_pdf_payload(self):
        payload = b"%PDF-" + b"x" * 100
        with tempfile.TemporaryDirectory() as td:
            with patch.object(MODULE, "urlopen", return_value=FakeResponse(payload)):
                with self.assertRaisesRegex(ValueError, "unexpectedly small"):
                    MODULE.acquire_pdf(Path(td) / "source.pdf")

    def test_extract_requires_exact_seven_pages_and_writes_page_markers(self):
        fake_text = "\f".join([f"page-{n}" for n in range(7)]) + "\f"
        with tempfile.TemporaryDirectory() as td:
            output = Path(td) / "extract.txt"
            completed = type("Completed", (), {"stdout": fake_text})()
            with patch.object(MODULE.subprocess, "run", return_value=completed):
                result = MODULE.extract_pages(Path(td) / "source.pdf", output)
            lines = output.read_text(encoding="utf-8").splitlines()
            self.assertEqual(result["extracted_page_count"], 7)
            self.assertEqual(result["text_line_count"], 7)
            self.assertEqual(lines[0], "L1@P256: page-0")
            self.assertEqual(lines[-1], "L7@P262: page-6")

    def test_extract_rejects_incomplete_page_range(self):
        fake_text = "\f".join(["page-1", "page-2"]) + "\f"
        with tempfile.TemporaryDirectory() as td:
            with patch.object(MODULE.subprocess, "run", return_value=type("Completed", (), {"stdout": fake_text})()):
                with self.assertRaisesRegex(ValueError, "Expected 7 extracted pages"):
                    MODULE.extract_pages(Path(td) / "source.pdf", Path(td) / "extract.txt")


if __name__ == "__main__":
    unittest.main(verbosity=2)
