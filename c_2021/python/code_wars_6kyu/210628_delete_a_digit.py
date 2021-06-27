import unittest
from itertools import combinations


def delete_digit(n):
    n = str(n)
    return max(int("".join(ele)) for ele in combinations(n, len(n) - 1))


class TestDeleteDigit(unittest.TestCase):
    def test_delete_digit(self):
        self.assertEqual(delete_digit(n=1001), 101)
