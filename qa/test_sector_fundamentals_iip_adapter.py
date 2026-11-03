import unittest
import pandas as pd
from pipeline.build_sector_fundamentals_from_iip import build_rows

def sample_panel():
    periods=pd.period_range("2023-04","2026-09",freq="M").astype(str)
    rows=[]
    for code in range(10,33):
        for period in periods:
            is_pib=period=="2026-09"
            rows.append({
                "period":period,"nic_2025":str(code),"description":f"NIC group {code}",
                "weight":1.0,"index":100.0,"base_year":"2022-23","frequency":"M","unit":"index",
                "source":"MoSPI September 2026 PIB Statement IV" if is_pib else "MoSPI e-Sankhyiki Data Catalogue",
                "table_id":"PIB_PRID_2329475_STATEMENT_IV" if is_pib else "IIPMFY26018AUG",
                "release_date":"28 Oct 2026" if is_pib else "30 Sep 2026",
                "release_vintage":"2026-09_quick_estimate" if is_pib else "2026-08",
                "source_file":"mospi_iip_release_raw.html" if is_pib else "nic2.xlsx",
                "source_sha256":"a"*64 if is_pib else "b"*64
            })
    return pd.DataFrame(rows)

class SectorFundamentalsIIPAdapterTests(unittest.TestCase):
    def test_builds_complete_provenance_rich_partial_panel(self):
        catalogue=pd.DataFrame([{"file_path":"/catalogue/","file_name":"nic2.xlsx","unique_id":"IIPMFY26018AUG","release_date":"30 Sep 2026","ref_period":"2026-08","sha256":"b"*64}])
        out=build_rows(sample_panel(),catalogue,{"url":"https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475"},"2026-11-03T00:00:00+00:00")
        self.assertEqual(len(out),966)
        self.assertEqual(out["SECTOR"].nunique(),23)
        self.assertEqual(out["DATE"].nunique(),42)
        self.assertEqual(out["METRIC"].unique().tolist(),["IIP_INDEX"])
        self.assertTrue(out["PUBLICATION_TIMESTAMP"].eq("").all())
        self.assertTrue(out["PUBLICATION_TIME_STATUS"].eq("UNKNOWN_NOT_PUBLISHED_IN_SOURCE_METADATA").all())
        self.assertTrue(out["SOURCE_URL"].astype(str).str.startswith("https://").all())

    def test_duplicate_nic_month_keys_are_rejected(self):
        panel=sample_panel()
        panel.loc[1,"period"]=panel.loc[0,"period"]
        panel.loc[1,"nic_2025"]=panel.loc[0,"nic_2025"]
        catalogue=pd.DataFrame([{"file_path":"/catalogue/","file_name":"nic2.xlsx"}])
        with self.assertRaisesRegex(ValueError,"Duplicate NIC-2/month keys"):
            build_rows(panel,catalogue,{},"2026-11-03T00:00:00+00:00")

if __name__=="__main__":
    unittest.main()
