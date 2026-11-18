import tempfile
import unittest
from pathlib import Path

from qa.audit_brazil_bop_indicator_codes import audit


DATA = """<mes:StructureSpecificData xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message">
 <mes:Header><mes:Structure structureID="IMF_BOP_BPM6_1_0" namespace="urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP_BPM6(1.0):ObsLevelDim:TIME_PERIOD"/></mes:Header>
 <mes:DataSet>
  <mes:Series REF_AREA="BR" INDICATOR="BFP_BP6_USD"><mes:Obs TIME_PERIOD="2026-09" OBS_VALUE="1"/></mes:Series>
  <mes:Series REF_AREA="BR" INDICATOR="BRA_LOCAL_TEST"><mes:Obs TIME_PERIOD="2026-09" OBS_VALUE="2"/></mes:Series>
 </mes:DataSet>
</mes:StructureSpecificData>"""

ECOFIN = """<mes:StructureMessage xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message" xmlns:str="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure" xmlns:com="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common">
 <mes:Structures>
  <str:DataStructures><str:DataStructure id="ECOFIN_DSD" agencyID="IMF" version="1.0">
   <str:DataStructureComponents><str:DimensionList><str:Dimension id="INDICATOR"><str:LocalRepresentation><str:Enumeration><Ref agencyID="IMF" id="CL_INDICATOR" version="1.0"/></str:Enumeration></str:LocalRepresentation></str:Dimension></str:DimensionList></str:DataStructureComponents>
  </str:DataStructure></str:DataStructures>
  <str:Codelists><str:Codelist id="CL_INDICATOR" agencyID="IMF" version="1.0">
   <str:Code id="BFP_BP6_USD"><com:Name xml:lang="en">Portfolio investment</com:Name></str:Code>
  </str:Codelist></str:Codelists>
 </mes:Structures>
</mes:StructureMessage>"""


class IndicatorAuditTests(unittest.TestCase):
    def run_audit(self, data=DATA, ecofin=ECOFIN):
        with tempfile.TemporaryDirectory() as tmp:
            d, e = Path(tmp) / "brazil.xml", Path(tmp) / "ecofin.xml"
            d.write_text(data, encoding="utf-8")
            e.write_text(ecofin, encoding="utf-8")
            return audit(d, e, "BR", "BRA")

    def test_official_and_country_specific_codes_are_distinct(self):
        r = self.run_audit()
        self.assertEqual(r["status"], "PASS_WITH_WARNINGS")
        rows = {x["indicator"]: x for x in r["indicators"]}
        self.assertEqual(rows["BFP_BP6_USD"]["imf_validation_status"], "OFFICIAL_CL_INDICATOR_MATCH")
        self.assertEqual(rows["BRA_LOCAL_TEST"]["semantic_status"], "UNKNOWN_NO_IMF_LABEL")
        self.assertEqual(r["admission"]["portfolio_flow_panel"], "NOT_AUTHORIZED")

    def test_unlisted_non_brazil_code_fails_closed(self):
        r = self.run_audit(data=DATA.replace("BRA_LOCAL_TEST", "BAD_CODE"))
        self.assertEqual(r["status"], "FAIL")
        bad = next(x for x in r["indicators"] if x["indicator"] == "BAD_CODE")
        self.assertEqual(bad["semantic_status"], "UNKNOWN_QUARANTINE")

    def test_wrong_codelist_identity_fails(self):
        with self.assertRaises(ValueError):
            self.run_audit(ecofin=ECOFIN.replace('id="CL_INDICATOR"', 'id="OTHER"'))

    def test_wrong_dataflow_fails(self):
        with self.assertRaises(ValueError):
            self.run_audit(data=DATA.replace("Dataflow=IMF:BOP_BPM6(1.0)", "Dataflow=IMF:OTHER(1.0)"))

    def test_wrong_reference_area_fails(self):
        with self.assertRaises(ValueError):
            self.run_audit(data=DATA.replace('REF_AREA="BR"', 'REF_AREA="IN"'))

    def test_wrong_country_iso3_does_not_whitelist_local_code(self):
        r = self.run_audit()
        # The actual audit call uses BRA; a non-BRA local code is quarantined.
        bad_data = DATA.replace("BRA_LOCAL_TEST", "IND_LOCAL_TEST")
        with tempfile.TemporaryDirectory() as tmp:
            d, e = Path(tmp) / "brazil.xml", Path(tmp) / "ecofin.xml"
            d.write_text(bad_data, encoding="utf-8")
            e.write_text(ECOFIN, encoding="utf-8")
            result = audit(d, e, "BR", "BRA")
        self.assertEqual(result["status"], "FAIL")
        row = next(x for x in result["indicators"] if x["indicator"] == "IND_LOCAL_TEST")
        self.assertEqual(row["semantic_status"], "UNKNOWN_QUARANTINE")

    def test_duplicate_codelist_code_fails(self):
        duplicate = ECOFIN.replace(
            '</str:Codelist>',
            '<str:Code id="BFP_BP6_USD"><com:Name>Duplicate</com:Name></str:Code></str:Codelist>'
        )
        with self.assertRaises(ValueError):
            self.run_audit(ecofin=duplicate)


if __name__ == "__main__":
    unittest.main()
