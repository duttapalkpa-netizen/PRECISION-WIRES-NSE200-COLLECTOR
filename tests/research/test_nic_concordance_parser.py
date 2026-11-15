import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts' / 'research'))
from nic_concordance_parser import parse_source_lines, audit

class ParserTests(unittest.TestCase):
    def parse(self, body):
        lines = ["L10330@P256: CONCORDANCE BETWEEN 4-DIGIT INDUSTRY CLASSES OF NIC-2025 AND NIC-2008"]
        lines += [f"L{10331+i}@P256: {x}" for i, x in enumerate(body.splitlines())]
        return parse_source_lines(lines)


    def test_page_range_marker_retains_provenance_and_stops_at_notes(self):
        lines = [
            "L10330@P256: CONCORDANCE BETWEEN 4-DIGIT INDUSTRY CLASSES OF NIC-2025 AND NIC-2008",
            "L10407@P256-257: 1079 1079(p)",
            "L10408@P257: NIC 2025",
            "L10409@P257: Code",
            "L10410@P257: NIC 2008 Code",
            "L10411@P257: 1080 1080",
            "L10873@P262: EXPLANATORY NOTES",
            "L10874@P262: 1. This is explanatory material"
        ]
        rows = parse_source_lines(lines)
        self.assertEqual([r.nic2025_class_4d for r in rows], ["1079", "1080"])
        self.assertEqual(rows[0].pdf_pages, [256, 257])
        self.assertEqual(rows[0].source_lines, [10407])

    def test_simple_and_partial_aggregation(self):
        rows = self.parse("0113 0113+0128(p)\n0114 0114")
        self.assertEqual(rows[0].components(), [{"code":"0113","partial":False},{"code":"0128","partial":True}])

    def test_wrapped_expression(self):
        rows = self.parse("0330 0311(p)+0312(p)+0321(p)+\n0322(p)\n0510 0510")
        self.assertEqual(rows[0].normalized_expression(), "0311(p)+0312(p)+0321(p)+0322(p)")
        self.assertEqual(len(rows[0].components()), 4)

    def test_4340_three_line_expression(self):
        rows = self.parse("4340 4311(p)+4312(p)+4321(p)+\n4322(p)+4329(p)+4330(p)+\n4390(p)")
        self.assertEqual(len(rows[0].components()), 7)

    def test_4772_blank_key_continuation_after_repeated_header(self):
        rows = self.parse("4772 4772(p)+4789(p)+4791(p)+\nNIC 2025 Code\nNIC 2008 Code\n4799(p)\n4773 4773(p)+4789(p)")
        self.assertEqual(rows[0].normalized_expression(), "4772(p)+4789(p)+4791(p)+4799(p)")
        self.assertEqual(len(rows[0].components()), 4)

    def test_distinct_keys_may_share_expression(self):
        rows = self.parse("4642 4649(p)+4659(p)\n4649 4649(p)+4659(p)")
        self.assertEqual([r.nic2025_class_4d for r in rows], ["4642", "4649"])

    def test_long_expression_all_components_preserved(self):
        expr = "4510(p)+4711(p)+4719(p)+4721(p)+4722(p)+4723(p)+4730(p)+4741(p)+4742(p)+4751(p)+4752(p)+4753(p)+4759(p)+4761(p)+4762(p)+4763(p)+4764(p)+4771(p)+4772(p)+4773(p)+4774(p)+4791(p)+4799(p)"
        rows = self.parse("4790 " + expr)
        self.assertEqual(len(rows[0].components()), 23)

    def test_unresolved_trailing_plus_fails_closed(self):
        with self.assertRaises(ValueError):
            self.parse("4772 4772(p)+4789(p)+")


    def test_audit_blocks_count_match_without_source_provenance(self):
        rows = self.parse("0111 0111")
        report = audit(rows, expected_count=1)
        self.assertEqual(report["row_count"], 1)
        self.assertFalse(report["provenance_complete"])
        self.assertFalse(report["source_bounds_pass"])
        self.assertEqual(report["acceptance"], "UNKNOWN_BLOCKED")

    def test_duplicate_keys_block_acceptance(self):
        rows = self.parse("0111 0111\n0111 0111")
        report = audit(rows, expected_count=2)
        self.assertEqual(report["acceptance"], "UNKNOWN_BLOCKED")
        self.assertEqual(report["duplicate_keys"], ["0111"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
