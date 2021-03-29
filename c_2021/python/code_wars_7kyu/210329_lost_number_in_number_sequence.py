import unittest
from typing import List


def find_deleted_number(arr: List[int], mixed_arr: List[int]):
    return sum(arr) - sum(mixed_arr)


class TestFindDeleteNumber(unittest.TestCase):
    def test_find_deleted_number(self):
        self.assertEqual(find_deleted_number(arr=[1, 2, 3, 4, 5], mixed_arr=[3, 4, 1, 5]), 2)
