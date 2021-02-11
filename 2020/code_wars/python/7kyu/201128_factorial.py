from functools import reduce
import unittest


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
    
    
class TestFactorial(unittest.TestCase):
    def test_factorial_n_with_0(self):
        n = 0
        actual = factorial(n)
        self.assertEqual(actual, 1)

    def test_factorial_n_with_1(self):
        n = 3
        actual = factorial(n)
        self.assertEqual(actual, 6)

    def test_should_fail(self):
        self.fail()

