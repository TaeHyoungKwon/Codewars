import unittest
from typing import List


def normalize(numbers: List[int]):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


class TestNormalize(unittest.TestCase):
    def test_normalize_with_sum(self):
        self.assertEqual(sum(normalize(numbers=[15, 35, 80])), 100.0)
