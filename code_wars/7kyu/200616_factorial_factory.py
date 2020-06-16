import math
import unittest


def factorial(n):
    if n < 0:
        return
    return math.factorial(n)
    
    
class TestFactorial(unittest.TestCase):
    def test_factorial_with_n_is_negative_should_return_none(self):
        self.assertEqual(factorial(-1), None)

    def test_factorial_with_n_is_not_negative_should_return_factorial(self):
        self.assertEqual(factorial(5), 120)
