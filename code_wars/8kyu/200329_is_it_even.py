import unittest


def is_even(n):
    return n % 2 == 0
    
    
class TestIsEven(unittest.TestCase):
    def test_should_return_true_when_given_n_is_0(self):
        n = 0
        actual = is_even(n)
        self.assertEqual(actual, True)

    def test_should_return_true_when_given_n_is_float(self):
        n = 1.0
        actual = is_even(n)
        self.assertEqual(actual, False)

    def test_should_return_true_when_given_n_is_even(self):
        n = 2
        actual = is_even(n)
        self.assertEqual(actual, True)

    def test_should_return_true_when_given_n_is_odd(self):
        n = 3
        actual = is_even(n)
        self.assertEqual(actual, False)
