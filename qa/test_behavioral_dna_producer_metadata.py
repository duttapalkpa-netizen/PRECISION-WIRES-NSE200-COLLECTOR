import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from pipeline.walk_forward_backtest import build_behavioral_dna_artifact
from pipeline.calibration_gate import validate_calibration_artifact

class BehavioralDnaProducerMetadataTests(unittest.TestCase):
    def test_metadata_uses_real_source_hash_and_preserves_legacy_state_shape(self):
        with tempfile.TemporaryDirectory() as td:
            src=Path(td)/"dataset.csv"
            src.write_bytes(b"official-source-fixture-bytes")
            dna={"CONTINUATION_READY":{
                "samples":10,"hit10_h3_count":2,"hit10_h3":0.2,
                "hit5_h1":0.3,"hit20_h5":0.1,"median_winner_probability":0.4}}
            artifact=build_behavioral_dna_artifact(
                dna,src,"2026-10-01","2026-10-30","2026-11-06",
                "42770000000","a"*40,"2026-11-10T00:00:00+00:00")
            expected=hashlib.sha256(src.read_bytes()).hexdigest()
            self.assertEqual(artifact["dataset_sha256"],expected)
            self.assertEqual(artifact["CONTINUATION_READY"]["hit10_h3"],0.2)
            self.assertEqual(artifact["states"]["CONTINUATION_READY"],{
                "sample_count":10,"hit10_h3_count":2,"hit10_h3_rate":0.2})
            path=Path(td)/"dna.json"
            path.write_text(json.dumps(artifact),encoding="utf-8")
            result=validate_calibration_artifact(path)
            self.assertEqual(result["status"],"VALID")
            self.assertFalse(result["block_selection"])

    def test_missing_github_lineage_remains_unknown(self):
        with tempfile.TemporaryDirectory() as td:
            src=Path(td)/"dataset.csv"; src.write_bytes(b"source")
            artifact=build_behavioral_dna_artifact(
                {"S":{"samples":1,"hit10_h3_count":0,"hit10_h3":0.0}},
                src,"2026-10-01","2026-10-01","2026-10-06",None,None,
                "2026-11-10T00:00:00+00:00")
            path=Path(td)/"dna.json"; path.write_text(json.dumps(artifact),encoding="utf-8")
            self.assertEqual(validate_calibration_artifact(path)["status"],"UNKNOWN_PROVENANCE")

if __name__=="__main__":
    unittest.main(verbosity=2)
