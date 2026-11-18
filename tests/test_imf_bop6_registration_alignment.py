import tempfile
import unittest
from pathlib import Path

from qa.audit_imf_bop6_registration_alignment import (
    parse_registration, parse_bcb_payload
)


class IMFRegistrationAlignmentTests(unittest.TestCase):
    def test_registration_row_identifies_bop6_and_bcb_provider(self):
        html = """<table><tr><th>Dataflow</th><th>Data Provider</th><th>URL</th><th>Last Updated</th></tr>
        <tr><td>IMF:BOP6(1.0)</td><td>IMF:BR1</td>
        <td><a href="https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml">BCB</a></td>
        <td>2026-10-26T11:47:29.000Z</td></tr></table>"""
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "registrations.html"
            p.write_text(html)
            row = parse_registration(p)
        self.assertEqual(row["dataflow"], "IMF:BOP6(1.0)")
        self.assertEqual(row["provider"], "IMF:BR1")
        self.assertTrue(any("bcb.gov.br/content/statistics/sddsdocuments" in x for x in row["url_candidates"]))

    def test_missing_registration_row_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "registrations.html"
            p.write_text("<table><tr><td>IMF:BOP_BPM6(1.0)</td><td>IMF:BR1</td><td>x</td></tr></table>")
            with self.assertRaises(ValueError):
                parse_registration(p)

    def test_bcb_payload_extracts_actual_dataflow_namespace(self):
        xml = """<mes:StructureSpecificData xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message">
        <mes:Header><mes:Structure namespace="urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=IMF:BOP_BPM6(1.0):ObsLevelDim:TIME_PERIOD"/></mes:Header>
        </mes:StructureSpecificData>"""
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bcb.xml"
            p.write_text(xml)
            ref = parse_bcb_payload(p)
        self.assertEqual(ref, {"agencyID": "IMF", "id": "BOP_BPM6", "version": "1.0"})


if __name__ == "__main__":
    unittest.main()
