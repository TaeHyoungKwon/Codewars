import unittest
from collections import Counter


def highest_rank(arr):
    c = Counter(arr)
    return sorted(c.items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]


class TestHighestRankNumberInAnArray(unittest.TestCase):
    def test_hightest_rank(self):
        arr = [12, 10, 8, 12, 7, 6, 4, 10, 12]
        actual = highest_rank(arr)
        self.assertEqual(actual, 12)
