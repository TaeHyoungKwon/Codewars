import unittest
import math


def factorial(n):
    if n > 12:
        raise ValueError
    return math.factorial(n)
    
    
class TestFactorial(unittest.TestCase):
    def test_should_raise_value_error_when_given_n_is_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_should_raise_value_error_when_given_n_is_greater_than_12(self):
        with self.assertRaises(ValueError):
            factorial(13)

    def test_factorial(self):
        n = 3
        actual = factorial(n)
        self.assertEqual(actual, 6)
