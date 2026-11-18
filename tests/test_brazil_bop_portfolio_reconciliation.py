import tempfile
import unittest
from pathlib import Path

from qa.audit_brazil_bop_portfolio_reconciliation import read_series, reconcile


XML = """<StructureSpecificData>
<Series REF_AREA="BR" FREQ="M" UNIT_MULT="6" INDICATOR="BFP_BP6_USD">
<Obs TIME_PERIOD="2009-12" OBS_VALUE="3"/><Obs TIME_PERIOD="2010-01" OBS_VALUE="7"/>
</Series>
<Series REF_AREA="BR" FREQ="M" UNIT_MULT="6" INDICATOR="BFPA_BP6_USD">
<Obs TIME_PERIOD="2009-12" OBS_VALUE="5"/><Obs TIME_PERIOD="2010-01" OBS_VALUE="10"/>
</Series>
<Series REF_AREA="BR" FREQ="M" UNIT_MULT="6" INDICATOR="BFPL_BP6_USD">
<Obs TIME_PERIOD="2009-12" OBS_VALUE="2"/><Obs TIME_PERIOD="2010-01" OBS_VALUE="1"/>
</Series>
</StructureSpecificData>"""


class PortfolioReconciliationTests(unittest.TestCase):
    def test_balanced_period_passes_and_divergent_period_is_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "brazil.xml"
            p.write_text(XML, encoding="utf-8")
            values = read_series(p, ["BFP_BP6_USD", "BFPA_BP6_USD", "BFPL_BP6_USD"])
        r = reconcile(values)
        self.assertEqual(r["matched_period_count"], 1)
        self.assertEqual(r["mismatch_count"], 1)
        self.assertEqual(r["first_mismatch_period"], "2010-01")
        self.assertEqual(r["status"], "FAIL_RECONCILIATION")
        self.assertEqual(r["admission"], "NOT_AUTHORIZED")

    def test_wrong_country_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "brazil.xml"
            p.write_text(XML.replace('REF_AREA="BR"', 'REF_AREA="IN"', 1), encoding="utf-8")
            with self.assertRaises(ValueError):
                read_series(p, ["BFP_BP6_USD", "BFPA_BP6_USD", "BFPL_BP6_USD"])

    def test_wrong_unit_multiplier_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "brazil.xml"
            p.write_text(XML.replace('UNIT_MULT="6"', 'UNIT_MULT="3"', 1), encoding="utf-8")
            with self.assertRaises(ValueError):
                read_series(p, ["BFP_BP6_USD", "BFPA_BP6_USD", "BFPL_BP6_USD"])


if __name__ == "__main__":
    unittest.main()
