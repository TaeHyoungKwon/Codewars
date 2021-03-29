import unittest
from math import factorial


def pascals_triangle(n):
    def _calc_pascals_triangle(row, col):
        return factorial(row) // (factorial(row - col) * factorial(col))

    return [_calc_pascals_triangle(n, k) for n in range(n) for k in range(n + 1)]


class TestPascalsTriangle(unittest.TestCase):
    def test_pascals_triangle(self):
        self.assertEqual(pascals_triangle(n=6), [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10, 10, 5, 1])
