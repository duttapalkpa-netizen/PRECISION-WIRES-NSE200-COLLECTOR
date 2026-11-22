import hashlib
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from qa.validate_security_master import validate
from unittest.mock import patch
from collector import security_master

class SecurityMasterValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        self.master=self.root/"security_master.csv"
        self.manifest=self.root/"security_master_manifest.json"
        self.payload=b"SYMBOL,ISIN,LISTING_DATE\nABC,INE000A01001,\n"
        self.master.write_bytes(self.payload)
        self.data={
            "source_url":"https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv",
            "retrieved_at_utc":"2026-11-22T00:00:00+00:00",
            "source_family":"LEGACY_EQUITY_L_CSV",
            "daily_mii_equivalence":"NOT_ESTABLISHED",
            "normalized_sha256":hashlib.sha256(self.payload).hexdigest(),
            "source_sha256":"a"*64,"source_bytes":123,"rows":1
        }
        self.manifest.write_text(json.dumps(self.data),encoding="utf-8")
        self.now=datetime(2026,11,22,1,tzinfo=timezone.utc)
    def tearDown(self): self.tmp.cleanup()
    def test_failed_fresh_acquisition_removes_previous_master_and_manifest(self):
        old_out, old_manifest = security_master.OUT, security_master.MANIFEST
        try:
            security_master.OUT = self.master
            security_master.MANIFEST = self.manifest
            class FailedSession:
                headers = {}
                def get(self, url, timeout):
                    raise OSError("simulated network failure")
            with patch.object(security_master.requests, "Session", return_value=FailedSession()):
                with self.assertRaises(SystemExit):
                    security_master.main()
            self.assertFalse(self.master.exists())
            self.assertFalse(self.manifest.exists())
        finally:
            security_master.OUT, security_master.MANIFEST = old_out, old_manifest

    def test_valid_master_passes_without_claiming_mii_equivalence(self):
        result=validate(self.master,self.manifest,self.now)
        self.assertEqual(result["status"],"PASS")
        self.assertEqual(result["daily_mii_equivalence"],"NOT_ESTABLISHED")
    def test_missing_manifest_blocks(self):
        self.manifest.unlink()
        with self.assertRaisesRegex(ValueError,"missing"): validate(self.master,self.manifest,self.now)
    def test_unapproved_host_blocks(self):
        self.data["source_url"]="https://example.com/master.csv"
        self.manifest.write_text(json.dumps(self.data),encoding="utf-8")
        with self.assertRaisesRegex(ValueError,"official NSE"): validate(self.master,self.manifest,self.now)
    def test_stale_master_blocks(self):
        self.data["retrieved_at_utc"]="2026-11-01T00:00:00+00:00"
        self.manifest.write_text(json.dumps(self.data),encoding="utf-8")
        with self.assertRaisesRegex(ValueError,"stale"): validate(self.master,self.manifest,self.now)
    def test_hash_mismatch_blocks(self):
        self.master.write_text("SYMBOL,ISIN,LISTING_DATE\nXYZ,INE000A01002,\n",encoding="utf-8")
        with self.assertRaisesRegex(ValueError,"SHA-256"): validate(self.master,self.manifest,self.now)
    def test_missing_isin_blocks(self):
        self.master.write_text("SYMBOL,ISIN,LISTING_DATE\nABC,,\n",encoding="utf-8")
        self.data["normalized_sha256"]=hashlib.sha256(self.master.read_bytes()).hexdigest()
        self.manifest.write_text(json.dumps(self.data),encoding="utf-8")
        with self.assertRaisesRegex(ValueError,"missing SYMBOL/ISIN"): validate(self.master,self.manifest,self.now)

if __name__=="__main__": unittest.main()
