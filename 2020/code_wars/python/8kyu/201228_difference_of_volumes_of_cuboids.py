from functools import reduce
import unittest


def find_difference(a, b):
    def multiply(x, y):
        return x * y
    return abs(reduce(multiply, a) - reduce(multiply, b))


class TestFindDifference(unittest.TestCase):
    def test_find_difference_first_case(self):
        self.assertEqual(find_difference([3, 2, 5], [1, 4, 4]), 14)
