import unittest


def triangular(n):
    return 0 if n <= 0 else n * (n + 1) / 2


class TestTriangularTreasure(unittest.TestCase):
    def test_should_return_zero_when_given_n_is_negative(self):
        n = -10
        result = triangular(n)
        self.assertEqual(result, 0)

    def test_should_return_zero_when_given_n_is_zero(self):
        n = 0
        result = triangular(n)
        self.assertEqual(result, 0)

    def test_should_return_fourty_five_when_given_n_is_nine(self):
        n = 9
        result = triangular(n)
        self.assertEqual(result, 45)
