import hashlib
import io
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile
from types import SimpleNamespace

from pipeline import collect_fed_h10_raw as collector


def zip_bytes():
    out = io.BytesIO()
    with ZipFile(out, "w") as zf:
        zf.writestr("package/metadata.xml", "<metadata/>")
        zf.writestr("package/data.xml", "<data/>")
    return out.getvalue()


class FakeResponse:
    def __init__(self, raw, url=collector.SOURCE_URL, content_type="application/zip"):
        self.raw, self.url, self.headers = raw, url, {"Content-Type": content_type}
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def geturl(self): return self.url
    def read(self, limit): return self.raw[:limit]


class TestFedH10RawCollector(unittest.TestCase):
    def test_archive_preserves_raw_bytes_and_writes_hash_manifest(self):
        raw = zip_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(collector, "urlopen", return_value=FakeResponse(raw)):
                result = collector.archive(Path(tmp), datetime(2026, 11, 11, tzinfo=timezone.utc))
            saved = Path(result["archive"]).read_bytes()
            manifest = json.loads(Path(result["manifest"]).read_text())
            self.assertEqual(saved, raw)
            self.assertEqual(result["sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(manifest["sha256"], result["sha256"])
            self.assertFalse(manifest["raw_payload_parsed"])
            self.assertFalse(manifest["observation_panel_created"])
            self.assertEqual(len(manifest["series"]), 3)

    def test_rejects_lookalike_hostname_before_request(self):
        with patch.object(collector, "urlopen") as mocked:
            with self.assertRaises(ValueError):
                collector.retrieve("https://www.federalreserve.gov.attacker.example/file.zip")
            mocked.assert_not_called()

    def test_rejects_http_and_nonstandard_port_before_request(self):
        with patch.object(collector, "urlopen") as mocked:
            for url in (
                "http://www.federalreserve.gov/file.zip",
                "https://www.federalreserve.gov:8443/file.zip",
                "https://user@www.federalreserve.gov/file.zip",
            ):
                with self.subTest(url=url), self.assertRaises(ValueError):
                    collector.retrieve(url)
            mocked.assert_not_called()

    def test_rejects_non_federal_redirect(self):
        with patch.object(collector, "urlopen", return_value=FakeResponse(zip_bytes(), "https://example.com/file.zip")):
            with tempfile.TemporaryDirectory() as tmp, self.assertRaises(ValueError):
                collector.archive(Path(tmp))

    def test_rejects_lookalike_redirect(self):
        with patch.object(collector, "urlopen", return_value=FakeResponse(
            zip_bytes(), "https://www.federalreserve.gov.attacker.example/file.zip"
        )):
            with tempfile.TemporaryDirectory() as tmp, self.assertRaises(ValueError):
                collector.archive(Path(tmp))

    def test_rejects_non_zip_payload(self):
        with patch.object(collector, "urlopen", return_value=FakeResponse(b"not a zip")):
            with tempfile.TemporaryDirectory() as tmp, self.assertRaises(ValueError):
                collector.archive(Path(tmp))

    def test_rejects_zip_member_paths_that_escape_or_confuse_platforms(self):
        for name in ("../escape.xml", "folder/../escape.xml", r"folder\escape.xml",
                     "C:/escape.xml", "/absolute.xml", "folder//double.xml"):
            with self.subTest(name=name):
                fake = SimpleNamespace(infolist=lambda: [
                    SimpleNamespace(filename=name, flag_bits=0, file_size=1)
                ])
                with self.assertRaises(ValueError):
                    collector.validate_zip_members(fake)

    def test_rejects_single_member_over_uncompressed_limit(self):
        fake = SimpleNamespace(infolist=lambda: [
            SimpleNamespace(filename="large.xml", flag_bits=0,
                            file_size=collector.MAX_MEMBER_UNCOMPRESSED_BYTES + 1)
        ])
        with self.assertRaisesRegex(ValueError, "member exceeds"):
            collector.validate_zip_members(fake)

    def test_rejects_total_uncompressed_size_over_limit(self):
        each = collector.MAX_MEMBER_UNCOMPRESSED_BYTES
        fake = SimpleNamespace(infolist=lambda: [
            SimpleNamespace(filename=f"part-{i}.xml", flag_bits=0, file_size=each)
            for i in range(3)
        ])
        with self.assertRaisesRegex(ValueError, "total uncompressed"):
            collector.validate_zip_members(fake)

    def test_rejects_excessive_member_count_and_encrypted_members(self):
        many = SimpleNamespace(infolist=lambda: [
            SimpleNamespace(filename=f"part-{i}.xml", flag_bits=0, file_size=0)
            for i in range(collector.MAX_ZIP_MEMBERS + 1)
        ])
        with self.assertRaisesRegex(ValueError, "member count"):
            collector.validate_zip_members(many)
        encrypted = SimpleNamespace(infolist=lambda: [
            SimpleNamespace(filename="secret.xml", flag_bits=1, file_size=1)
        ])
        with self.assertRaisesRegex(ValueError, "encrypted"):
            collector.validate_zip_members(encrypted)

    def test_rejects_duplicate_zip_member_names(self):
        duplicate = SimpleNamespace(infolist=lambda: [
            SimpleNamespace(filename="data.xml", flag_bits=0, file_size=1),
            SimpleNamespace(filename="data.xml", flag_bits=0, file_size=1),
        ])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            collector.validate_zip_members(duplicate)

    def test_append_only_collision_fails(self):
        raw = zip_bytes()
        stamp = datetime(2026, 11, 11, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(collector, "urlopen", return_value=FakeResponse(raw)):
                collector.archive(Path(tmp), stamp)
                with self.assertRaises(FileExistsError):
                    collector.archive(Path(tmp), stamp)


if __name__ == "__main__":
    unittest.main()
