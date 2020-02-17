import unittest
from collections import Counter


def calc_triple_double(num, cnt):
    return [digit
            for idx, digit in enumerate(str(num))
            if Counter(str(num)[idx: idx + cnt])[digit] == cnt]


def triple_double(num1, num2):
    triple = calc_triple_double(num1, 3)
    double = calc_triple_double(num2, 2)
    return 1 if set(triple) & set(double) else 0


class TestTripleDouble(unittest.TestCase):
    def test_should_return_0_on_not_triple_double(self):
        num1, num2 = 1222345, 12345
        actual = triple_double(num1, num2)
        self.assertEqual(actual, 0)

    def test_should_return_1_on_triple_double(self):
        num1, num2 = 451999277, 41177722899
        actual = triple_double(num1, num2)
        self.assertEqual(actual, 1)

    def test_should_return_1_on_triple_double_case_two(self):
        num1, num2 = 10560002, 100
        actual = triple_double(num1, num2)
        self.assertEqual(actual, 1)
