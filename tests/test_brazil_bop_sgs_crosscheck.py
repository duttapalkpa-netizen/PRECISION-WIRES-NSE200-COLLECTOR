import json
import tempfile
import unittest
from pathlib import Path

from qa.audit_brazil_bop_sgs_crosscheck import load_sgs, compare


class SGSCrosscheckTests(unittest.TestCase):
    def test_rounding_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "22905.json"
            p.write_text(json.dumps([{"data": "01/01/2010", "valor": "10.0"}]))
            sgs, _ = load_sgs(p, "22905")
        report = compare({"22905": sgs, "22906": {"2010-01": 5.0}, "22924": {"2010-01": -5.0}},
                         {"BFP_BP6_USD": {"2010-01": 10.04},
                          "BFPA_BP6_USD": {"2010-01": 5.0},
                          "BFPL_BP6_USD": {"2010-01": -5.0}})
        self.assertEqual(report["22905"]["mismatch_count"], 0)

    def test_material_source_divergence_flagged(self):
        report = compare({"22905": {"2010-01": -4441.7},
                          "22906": {"2010-01": 332.1},
                          "22924": {"2010-01": 4773.7}},
                         {"BFP_BP6_USD": {"2010-01": 88.383},
                          "BFPA_BP6_USD": {"2010-01": 1194.683},
                          "BFPL_BP6_USD": {"2010-01": 0.007}})
        self.assertEqual(report["22905"]["mismatch_count"], 1)
        self.assertEqual(report["22906"]["mismatch_count"], 1)
        self.assertEqual(report["22924"]["mismatch_count"], 1)

    def test_date_duplicate_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "22905.json"
            p.write_text(json.dumps([{"data": "01/01/2010", "valor": "10"},
                                     {"data": "01/01/2010", "valor": "11"}]))
            with self.assertRaises(ValueError):
                load_sgs(p, "22905")


if __name__ == "__main__":
    unittest.main()
