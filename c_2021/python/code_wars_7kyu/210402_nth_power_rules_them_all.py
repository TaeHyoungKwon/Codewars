import unittest
from typing import List


def modified_sum(a: List[int], n: int) -> int:
    return sum(ele ** n for ele in a) - sum(a)


class TestModifiedSum(unittest.TestCase):
    def test_modified_sum(self):
        self.assertEqual(modified_sum(a=[1, 2, 3], n=3), 30)
