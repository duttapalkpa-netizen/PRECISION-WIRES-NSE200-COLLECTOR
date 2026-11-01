import csv, tempfile, unittest
from pathlib import Path
from pipeline.build_oea_wpi_inflation_components_adapter import FIELDS
class InflationComponentsSchemaTests(unittest.TestCase):
    def test_required_schema_complete_and_provenance_distinct(self):
        required={"DATE","COUNTRY","COMPONENT","VALUE","RELEASED_AT","SOURCE","SOURCE_URL","OBSERVED_AT_UTC"}
        self.assertTrue(required.issubset(set(FIELDS)))
        self.assertIn("REVISION_EVIDENCE_SCOPE",FIELDS)
        self.assertIn("ITEM_CODE",FIELDS)
if __name__=="__main__": unittest.main()
