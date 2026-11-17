import hashlib,tempfile,unittest
from pathlib import Path
from pipeline.build_macro_indicator_evidence_snapshot import digest,load_source
class EvidenceTests(unittest.TestCase):
 def test_digest_is_sha256(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"raw"; p.write_bytes(b"source")
   self.assertEqual(digest(p),hashlib.sha256(b"source").hexdigest())
 def test_tamper_changes_digest(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"raw"; p.write_bytes(b"source"); a=digest(p); p.write_bytes(b"changed")
   self.assertNotEqual(a,digest(p))
 def test_missing_source_fails_closed(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(FileNotFoundError): load_source("gdp",Path(d))
if __name__=="__main__": unittest.main()
