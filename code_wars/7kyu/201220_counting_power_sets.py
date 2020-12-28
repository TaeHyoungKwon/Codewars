from itertools import combinations
import unittest


def powers(lst):
    return sum(1 for r in range(len(lst) + 1) for _ in combinations(lst, r))


class TestPowers(unittest.TestCase):
    def test_powers(self):
        self.assertEqual(powers([1, 2, 3]), 8)
