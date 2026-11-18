import unittest

from qa.audit_brazil_bop6_portfolio_components import compare, rollup


class PortfolioComponentTests(unittest.TestCase):
    def test_component_parent_sum_passes(self):
        src = {
            "22906": {"2010-01": 10.0},
            "22909": {"2010-01": 2.0},
            "22912": {"2010-01": 3.0},
            "22915": {"2010-01": 5.0},
            "22924": {"2010-01": 7.0},
            "22927": {"2010-01": 1.0},
            "22936": {"2010-01": 2.0},
            "22939": {"2010-01": 4.0},
            "22905": {"2010-01": 3.0},
        }
        r = rollup(src)
        self.assertEqual(r["assets"]["status"], "PASS_WITHIN_TOLERANCE")
        self.assertEqual(r["liabilities"]["status"], "PASS_WITHIN_TOLERANCE")
        self.assertEqual(r["net"]["status"], "PASS_WITHIN_TOLERANCE")

    def test_component_parent_sum_mismatch_fails(self):
        src = {
            "22906": {"2010-01": 11.0},
            "22909": {"2010-01": 2.0},
            "22912": {"2010-01": 3.0},
            "22915": {"2010-01": 5.0},
            "22924": {"2010-01": 7.0},
            "22927": {"2010-01": 1.0},
            "22936": {"2010-01": 2.0},
            "22939": {"2010-01": 4.0},
            "22905": {"2010-01": 4.0},
        }
        r = rollup(src)
        self.assertEqual(r["assets"]["status"], "FAIL")
        self.assertEqual(r["net"]["status"], "PASS_WITHIN_TOLERANCE")

    def test_comparison_detects_post_2010_divergence(self):
        r = compare({"2009-12": 1.0, "2010-01": 2.0},
                    {"2009-12": 1.02, "2010-01": 8.0})
        self.assertEqual(r["mismatch_pre_2010_count"], 0)
        self.assertEqual(r["mismatch_2010_onward_count"], 1)
        self.assertEqual(r["first_mismatch"], "2010-01")


if __name__ == "__main__":
    unittest.main()
