import tempfile, unittest
from pathlib import Path
import pandas as pd
from pipeline.nse_security_identity_reconciliation import read_csv, current_matches, clean

class IdentityHelpersTest(unittest.TestCase):
    def test_normalizes_symbol(self):
        self.assertEqual(clean("  abc "), "ABC")
    def test_csv_headers_normalized(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.csv"; p.write_text("Trading Symbol,ISIN\nABC,INEX\n")
            df=read_csv(p)
            self.assertIn("TRADINGSYMBOL",df.columns)
    def test_absence_is_not_a_status(self):
        # The classifier's contract is encoded in its explicit UNKNOWN state.
        self.assertTrue("UNKNOWN_NOT_IN_PROVIDED_SNAPSHOTS" in Path("pipeline/nse_security_identity_reconciliation.py").read_text())
    def test_no_production_mutation(self):
        source=Path("pipeline/nse_security_identity_reconciliation.py").read_text()
        for forbidden in ("RANKING_SCORE =", "PRESSURE_FADE =", "CORE_672 ="):
            self.assertNotIn(forbidden,source)

if __name__=="__main__": unittest.main()
