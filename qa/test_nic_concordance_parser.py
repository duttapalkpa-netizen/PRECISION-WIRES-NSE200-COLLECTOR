import importlib.util
import unittest
spec = importlib.util.spec_from_file_location('nic_table', 'pipeline/extract_nic_4digit_concordance.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class FakeTable:
    col_count = 2
    def __init__(self, rows): self.rows = rows
    def extract(self): return self.rows

HEADER = ['NIC2025\nCode', 'NIC2008Code']

class TestNICTableParser(unittest.TestCase):
    def test_direct_and_partial(self):
        rows = mod.parse_tables([FakeTable([HEADER,['0111','0111'],['0113','0113+0128(p)']])], 232)
        self.assertEqual(len(rows), 2)
        self.assertTrue(rows[1]['components'][1]['partial'])
    def test_aggregation(self):
        rows = mod.parse_tables([FakeTable([HEADER,['0330','0311(p)+0312(p)+0321(p)+0322(p)']])], 232)
        self.assertEqual(len(rows[0]['components']), 4)
    def test_4772_continuation_across_table(self):
        rows = mod.parse_tables([
            FakeTable([HEADER,['4772','4772(p)+4789(p)+4791(p)+']]),
            FakeTable([HEADER,['','4799(p)'],['4773','4773(p)+4789(p)']])
        ], 235)
        self.assertEqual(rows[0]['nic2008_expression_canonical'], '4772(P)+4789(P)+4791(P)+4799(P)')
        self.assertEqual(len(rows[0]['source_fragments']), 2)
        self.assertEqual(rows[1]['nic2025_class_4d'], '4773')
    def test_orphan_continuation_fails(self):
        with self.assertRaises(ValueError):
            mod.parse_tables([FakeTable([HEADER,['','4799(p)']])], 235)
    def test_unresolved_continuation_fails(self):
        with self.assertRaises(ValueError):
            mod.parse_tables([FakeTable([HEADER,['4772','4772(p)+']])], 235)
    def test_duplicate_keys_remain_detectable(self):
        rows = mod.parse_tables([FakeTable([HEADER,['0111','0111'],['0111','0111']])], 232)
        self.assertEqual(rows[0]['nic2025_class_4d'], rows[1]['nic2025_class_4d'])
    def test_bad_table_shape_fails(self):
        class BadTable:
            col_count = 3
            def extract(self): return []
        with self.assertRaises(ValueError):
            mod.parse_tables([BadTable()], 232)

if __name__ == '__main__':
    unittest.main(verbosity=2)
