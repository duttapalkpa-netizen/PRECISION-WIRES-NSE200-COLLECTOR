import io, unittest
from datetime import datetime
from openpyxl import Workbook
from pipeline.parse_fbil_gsec_archives import parse_workbook

class TestFbilArchiveParser(unittest.TestCase):
    def workbook_bytes(self):
        wb=Workbook()
        ws=wb.active
        ws.title="Par Yield"
        ws.cell(3,1,"FBIL GSec Base/Par Yield")
        ws.cell(3,3,datetime(2026,10,23))
        ws.append([])
        ws.append(["Tenor (Year)","YTM% p.a.(Semi-Annual)","YTM % p.a.(Annualized)"])
        ws.append([10,7.52,7.67])
        out=io.BytesIO()
        wb.save(out)
        return out.getvalue()

    def test_extracts_10y_and_does_not_infer_release_time(self):
        row=parse_workbook(self.workbook_bytes(),"fixture.xlsx")
        self.assertEqual(row["OBSERVATION_DATE"],"2026-10-23")
        self.assertEqual(row["YTM_SEMI_ANNUAL_PCT"],7.52)
        self.assertEqual(row["YTM_ANNUALIZED_PCT"],7.67)
        self.assertEqual(row["PUBLISHED_AT_IST"],"")
        self.assertEqual(row["RELEASED_AT_UTC"],"")

    def test_rejects_duplicate_10y_rows(self):
        wb=Workbook()
        ws=wb.active
        ws.title="Par Yield"
        ws.cell(3,1,"FBIL GSec Base/Par Yield")
        ws.cell(3,3,datetime(2026,10,23))
        ws.append([])
        ws.append(["Tenor (Year)","Semi","Annual"])
        ws.append([10,7.5,7.6])
        ws.append([10,7.51,7.61])
        out=io.BytesIO(); wb.save(out)
        with self.assertRaisesRegex(ValueError,"exactly one"):
            parse_workbook(out.getvalue(),"duplicate.xlsx")

if __name__=="__main__": unittest.main()
