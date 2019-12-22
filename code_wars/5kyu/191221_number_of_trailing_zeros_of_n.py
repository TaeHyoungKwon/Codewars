# https://www.codewars.com/kata/number-of-trailing-zeros-of-n/train/python
import math
import unittest


def zeros(n):
    num = 0
    while n:
        num += n // 5
        n = n // 5
    return num


class TestNumberOfTrailingZeros(unittest.TestCase):
    def test_should_return_0_when_given_n_is_0(self):
        n = 0
        result = zeros(n)
        self.assertEqual(result, 0)

    def test_should_return_0_when_given_n_is_1(self):
        n = 1
        result = zeros(n)
        self.assertEqual(result, 0)

    def test_should_return_1_when_given_n_is_6(self):
        n = 6
        result = zeros(n)
        self.assertEqual(result, 1)

    def test_should_return_7_when_given_n_is_30(self):
        n = 30
        result = zeros(n)
        self.assertEqual(result, 7)

    def test_should_return_2_when_given_n_is_12(self):
        n = 19
        result = zeros(n)
        self.assertEqual(result, 3)
