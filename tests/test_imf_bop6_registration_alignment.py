import json
import tempfile
import unittest
from pathlib import Path

from qa.audit_imf_bop6_registration_alignment import (
    parse_registration_snapshot, parse_bcb_payload, parse_constraint, coverage
)


class IMFRegistrationAlignmentTests(unittest.TestCase):
    def test_registration_snapshot_identifies_bop6_and_bcb_provider(self):
        snapshot = {
            "source_url": "https://sdmxcentral.imf.org/data/registrations.html",
            "row": {
                "dataflow": "IMF:BOP6(1.0)", "provider": "IMF:BR1",
                "registered_url": "https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml"
            }
        }
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "snapshot.json"
            p.write_text(json.dumps(snapshot))
            row = parse_registration_snapshot(p)
        self.assertEqual(row["row"]["dataflow"], "IMF:BOP6(1.0)")

    def test_wrong_provider_or_url_rejected(self):
        snapshot = {
            "source_url": "https://sdmxcentral.imf.org/data/registrations.html",
            "row": {"dataflow": "IMF:BOP6(1.0)", "provider": "IMF:XX",
                    "registered_url": "https://example.invalid"}
        }
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "snapshot.json"
            p.write_text(json.dumps(snapshot))
            with self.assertRaises(ValueError):
                parse_registration_snapshot(p)

    def test_bcb_payload_extracts_actual_dataflow_namespace(self):
        xml = """<mes:StructureSpecificData xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message">
        <mes:Header><mes:Structure namespace="urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP_BPM6(1.0):ObsLevelDim:TIME_PERIOD"/></mes:Header>
        <mes:DataSet><mes:Series INDICATOR="BFP_BP6_USD"/></mes:DataSet></mes:StructureSpecificData>"""
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bcb.xml"
            p.write_text(xml)
            ref, observed = parse_bcb_payload(p)
        self.assertEqual(ref, {"agencyID": "IMF", "id": "BOP_BPM6", "version": "1.0"})
        self.assertEqual(observed, ["BFP_BP6_USD"])

    def test_constraint_coverage_reports_missing_observed_codes(self):
        xml = """<mes:StructureMessage xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message"
        xmlns:str="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure" xmlns:com="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common">
        <mes:Structures><str:Constraints><str:ContentConstraint id="BOP6_CONSTRAINT" agencyID="IMF" version="1.0">
        <str:CubeRegion include="true"><com:KeyValue id="INDICATOR"><com:Value>A</com:Value></com:KeyValue></str:CubeRegion>
        </str:ContentConstraint></str:Constraints></mes:Structures></mes:StructureMessage>"""
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "constraint.xml"
            p.write_text(xml)
            c = parse_constraint(p, "BOP6_CONSTRAINT")
        self.assertEqual(c["allowed_indicator_count"], 1)
        result = coverage(["A", "B"], c["allowed_indicator_codes"])
        self.assertEqual(result["observed_not_allowed_count"], 1)
        self.assertEqual(result["status"], "FAIL_PARTIAL_COVERAGE")


if __name__ == "__main__":
    unittest.main()
