import unittest
from typing import List


def max_tri_sum(numbers: List[int]) -> int:
    return sum(sorted(set(numbers), reverse=True)[:3])


class TestMaxTriSum(unittest.TestCase):
    def test_max_tri_sum(self):
        self.assertEqual(max_tri_sum(numbers=[3, 2, 6, 8, 2, 3]), 17)
