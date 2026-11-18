import tempfile
import unittest
from pathlib import Path

from qa.build_brazil_bop_indicator_crosswalk import build


BRAZIL = """<mes:StructureSpecificData xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message">
 <mes:Header><mes:Structure structureID="IMF_BOP_BPM6_1_0" namespace="urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP_BPM6(1.0):ObsLevelDim:TIME_PERIOD"/></mes:Header>
 <mes:DataSet>
  <mes:Series DATA_DOMAIN="BOP6" REF_AREA="BR" INDICATOR="BFP_BP6_USD" COUNTERPART_AREA="W1" FREQ="M" UNIT_MULT="6" TIME_FORMAT="P1M">
   <mes:Obs TIME_PERIOD="2026-08" OBS_VALUE="10"/><mes:Obs TIME_PERIOD="2026-09" OBS_VALUE="11"/>
  </mes:Series>
  <mes:Series DATA_DOMAIN="BOP6" REF_AREA="BR" INDICATOR="BIPIP_BP6_USD" COUNTERPART_AREA="W1" FREQ="M" UNIT_MULT="6" TIME_FORMAT="P1M">
   <mes:Obs TIME_PERIOD="2026-08" OBS_VALUE="3"/><mes:Obs TIME_PERIOD="2026-09" OBS_VALUE="4"/>
  </mes:Series>
 </mes:DataSet>
</mes:StructureSpecificData>"""

ECOFIN = """<mes:StructureMessage xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message" xmlns:str="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure" xmlns:com="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common">
 <mes:Structures><str:Codelists><str:Codelist id="CL_INDICATOR" agencyID="IMF" version="1.0">
  <str:Code id="BFP_BP6_USD"><com:Name xml:lang="en">Balance of Payments, Financial Account, Portfolio investment [BPM6], US Dollars</com:Name></str:Code>
  <str:Code id="BIPIP_BP6_USD"><com:Name xml:lang="en">Balance of Payments, Current Account, Primary Income, Investment income, Portfolio investment, Net [BPM6], US Dollars</com:Name></str:Code>
 </str:Codelist></str:Codelists></mes:Structures>
</mes:StructureMessage>"""


class CrosswalkTests(unittest.TestCase):
    def run_build(self, brazil=BRAZIL, ecofin=ECOFIN):
        with tempfile.TemporaryDirectory() as tmp:
            b, e = Path(tmp) / "brazil.xml", Path(tmp) / "ecofin.xml"
            b.write_text(brazil, encoding="utf-8")
            e.write_text(ecofin, encoding="utf-8")
            return build(b, e)

    def test_portfolio_financial_account_separated_from_income(self):
        r = self.run_build()
        self.assertEqual(r["status"], "PASS_CODELIST_CROSSWALK_ONLY")
        self.assertEqual(r["coverage"]["unique_indicator_count"], 2)
        self.assertEqual(r["portfolio_candidates"]["financial_account_portfolio_investment_codes"], ["BFP_BP6_USD"])
        self.assertEqual(r["portfolio_candidates"]["portfolio_investment_income_codes"], ["BIPIP_BP6_USD"])

    def test_quality_absence_remains_unknown(self):
        r = self.run_build()
        self.assertEqual(r["quality_and_units"]["observation_quality_status"], "NOT_PRESENT_IN_CAPTURED_PAYLOAD")
        self.assertEqual(r["quality_and_units"]["quality_gate"], "UNKNOWN_NOT_PASS")
        self.assertEqual(r["admission"]["trading_signal"], "NOT_AUTHORIZED")

    def test_unmapped_code_fails_closed(self):
        with self.assertRaises(ValueError):
            self.run_build(brazil=BRAZIL.replace("BFP_BP6_USD", "UNMAPPED_CODE"))

    def test_wrong_dataflow_fails_closed(self):
        with self.assertRaises(ValueError):
            self.run_build(brazil=BRAZIL.replace("BOP_BPM6(1.0)", "BOP6(1.0)"))

    def test_wrong_ref_area_fails_closed(self):
        with self.assertRaises(ValueError):
            self.run_build(brazil=BRAZIL.replace('REF_AREA="BR"', 'REF_AREA="IN"'))


if __name__ == "__main__":
    unittest.main()
