import unittest
from math import gcd


def nbr_of_laps(x, y):
    gcd_ = gcd(x, y)
    return y // gcd_, x // gcd_


class TestNbr(unittest.TestCase):
    def test_nbr_of_laps(self):
        self.assertEqual(nbr_of_laps(5, 3), (3, 5))
        self.assertEqual(nbr_of_laps(4, 6), (3, 2))
        self.assertEqual(nbr_of_laps(5, 5), (1, 1))
