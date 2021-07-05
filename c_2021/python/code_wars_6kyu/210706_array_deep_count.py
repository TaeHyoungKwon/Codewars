import unittest


def deep_count(a):
    return len(a) + sum(deep_count(ele) for ele in a if isinstance(ele, list))


class TestDeepCount(unittest.TestCase):
    def test_deep_count(self):
        self.assertEqual(deep_count(a=[1, 2, [3, 4, [5]]]), 7)

    def test_deep_count_on_edge_case(self):
        self.assertEqual(deep_count(a=['cat', [['dog']], ['[bird]']]), 6)
