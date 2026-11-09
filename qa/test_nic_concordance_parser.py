import importlib.util
import unittest
spec = importlib.util.spec_from_file_location('nic_extract', 'pipeline/extract_nic_4digit_concordance.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class TestNICParser(unittest.TestCase):
    def test_direct(self):
        rows = mod.parse_lines(['0111 0111'], 232)
        self.assertEqual(rows[0]['nic2008_expression_canonical'], '0111')
        self.assertFalse(rows[0]['components'][0]['partial'])
    def test_partial_and_aggregation(self):
        rows = mod.parse_lines(['1512 1512 + 2220 (p)', '1811 1811+1313(p)'], 233)
        self.assertEqual(rows[0]['nic2008_expression_canonical'], '1512+2220(P)')
        self.assertEqual(len(rows[0]['components']), 2)
        self.assertTrue(rows[0]['components'][1]['partial'])
    def test_documented_4772_continuation(self):
        rows = mod.parse_lines(['4772 4772(p)+4789(p)+4791(p)+', 'NIC 2025 Code', 'NIC 2008 Code', '4799(p)'], 235)
        self.assertEqual(rows[0]['nic2008_expression_canonical'], '4772(P)+4789(P)+4791(P)+4799(P)')
        self.assertEqual(len(rows[0]['source_fragments']), 2)
    def test_orphan_continuation_rejected(self):
        with self.assertRaises(ValueError):
            mod.parse_lines(['4799(p)'], 235)
    def test_unresolved_trailing_plus_rejected(self):
        with self.assertRaises(ValueError):
            mod.parse_lines(['4772 4772(p)+'], 235)
    def test_ambiguous_line_rejected(self):
        with self.assertRaises(ValueError):
            mod.parse_lines(['4772 4772(p)+', 'unexpected'], 235)
    def test_duplicate_rows_remain_detectable(self):
        rows = mod.parse_lines(['2611 2610(p)', '2611 2610(p)'], 233)
        self.assertEqual(rows[0]['nic2025_class_4d'], rows[1]['nic2025_class_4d'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
