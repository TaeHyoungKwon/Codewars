import unittest
from collections import Counter


def ordered_count(inp):
    c = Counter(inp)
    return [(ele,c[ele]) for ele in c]

    
class TestOrderedCount(unittest.TestCase):
    def test_ordered_count(self):
        inp = 'abracadabra'
        actual = ordered_count(inp)
        self.assertEqual(actual, [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)])
