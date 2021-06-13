import itertools
import math
import unittest
from typing import List


def is_prime(num):
    if num < 2:
        return False
    for ele in range(2, int(math.sqrt(num)) + 1):
        if num % ele == 0:
            return False
    return True


def minimum_number(numbers: List[int]) -> int:
    return next(i for i, num in enumerate(itertools.count(sum(numbers))) if is_prime(num))


class TestMinimumNumber(unittest.TestCase):
    def test_minimum_number(self):
        self.assertEqual(minimum_number(numbers=[2, 12, 8, 4, 6]), 5)
