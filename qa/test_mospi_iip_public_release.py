import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipeline"))
from collect_mospi_iip_public_release import parse_html

class TestMospiIipParser(unittest.TestCase):
    def test_extracts_html_tables_and_cells(self):
        html=b"<html><table><tr><th>NIC</th><th>Index</th></tr><tr><td>24</td><td>130.7</td></tr></table></html>"
        _, tables=parse_html(html)
        self.assertEqual(tables, [[["NIC","Index"],["24","130.7"]]])

    def test_ragged_table_rows_can_be_padded_for_csv(self):
        rows=[["NIC","Index"],["24","130.7"],["25"]]
        width=max(map(len,rows))
        normalized=[row+[""]*(width-len(row)) for row in rows]
        self.assertEqual(normalized[-1],["25",""])

    def test_empty_html_is_empty(self):
        _, tables=parse_html(b"<html><body>No table</body></html>")
        self.assertEqual(tables, [])

if __name__=="__main__": unittest.main()
