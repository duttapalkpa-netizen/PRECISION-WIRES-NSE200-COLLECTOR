import unittest
from pipeline.build_oea_wpi_release_status_crosswalk import build_crosswalk

class WPIReleaseStatusCrosswalkTests(unittest.TestCase):
    def test_only_officially_labelled_months_promoted(self):
        manifest={"workbook":{"periods":["2026-03","2026-04","2026-05","2026-06","2026-07","2026-08","2026-09"]}}
        evidence={
          "source_url":"https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2323098&lang=1&reg=1",
          "published_date":"2026-10-14",
          "official_month_status":{"2026-04":"FINAL","2026-05":"FINAL","2026-06":"FINAL","2026-07":"FINAL","2026-08":"PROVISIONAL","2026-09":"PROVISIONAL"},
          "release_schedule":{"2026-10":{"status":"NOT_YET_RELEASED_AS_OF_2026-11-01","scheduled_release_date":"2026-11-16"}}
        }
        obs=[{"period":"2026-04","item_code":"01"},{"period":"2026-04","item_code":""},{"period":"2026-09","item_code":"02"}]
        rows=build_crosswalk(manifest,evidence,obs)
        states={r["period"]:r["revision_status"] for r in rows}
        self.assertEqual(states["2026-04"],"FINAL")
        self.assertEqual(states["2026-07"],"FINAL")
        self.assertEqual(states["2026-08"],"PROVISIONAL")
        self.assertEqual(states["2026-09"],"PROVISIONAL")
        self.assertEqual(states["2026-10"],"NOT_YET_RELEASED_AS_OF_2026-11-01")
        self.assertEqual(states["2026-03"],"UNKNOWN_NOT_COVERED_BY_REVIEWED_RELEASE")
        self.assertEqual(next(r for r in rows if r["period"]=="2026-04")["missing_item_code_rows"],1)
        self.assertEqual(next(r for r in rows if r["period"]=="2026-10")["observation_rows"],0)
    def test_refuses_october_observation_before_release(self):
        manifest={"workbook":{"periods":["2026-10"]}}
        evidence={"source_url":"x","published_date":"2026-10-14","official_month_status":{},
          "release_schedule":{"2026-10":{"status":"NOT_YET_RELEASED_AS_OF_2026-11-01","scheduled_release_date":"2026-11-16"}}}
        with self.assertRaises(ValueError):
            build_crosswalk(manifest,evidence,[{"period":"2026-10","item_code":"01"}])
if __name__=="__main__": unittest.main()
