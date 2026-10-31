import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipeline"))
from collect_mospi_iip_public_release import parse_html, normalize_statement_iv

class TestMospiIipParser(unittest.TestCase):
    def test_extracts_html_tables_and_cells(self):
        html=b"<html><table><tr><th>NIC</th><th>Index</th></tr><tr><td>24</td><td>130.7</td></tr></table></html>"
        _, tables=parse_html(html)
        self.assertEqual(tables, [[["NIC","Index"],["24","130.7"]]])

    def test_normalizes_nic2_monthly_panel_and_keeps_vintage_dimensions(self):
        months=["Sep-25","Oct-25","Nov-25","Dec-25","Jan-26","Feb-26","Mar-26","Apr-26","May-26","Jun-26","Jul-26","Aug-26","Sep-26"]
        header=["NIC 2025","Description","Weight"]+months
        row=["10","Manufacture of food products","5.679"]+[str(90+i) for i in range(13)]
        table_id, data=normalize_statement_iv([ [header,row] ])
        self.assertEqual(table_id,1)
        self.assertEqual(len(data),13)
        self.assertEqual(data[0]["period"],"2025-09")
        self.assertEqual(data[-1]["period"],"2026-09")
        self.assertEqual(data[0]["base_year"],"2022-23")
        self.assertEqual(data[0]["nic_2025"],"10")

    def test_rejects_non_monthly_or_wrong_table(self):
        table_id,data=normalize_statement_iv([[["NIC 2025","Description","Weight"],["10","Food","1"]]])
        self.assertIsNone(table_id)
        self.assertEqual(data,[])

    def test_empty_html_is_empty(self):
        _, tables=parse_html(b"<html><body>No table</body></html>")
        self.assertEqual(tables, [])

if __name__=="__main__": unittest.main()
