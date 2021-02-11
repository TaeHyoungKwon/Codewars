import enum
import unittest

POSITIVE_FORMAT = '{} = {}'
NEGATIVE_FORMAT = "{}<0"
ZERO_FORMAT = "0=0"


def show_sequence(n):
    if n == 0:
        return ZERO_FORMAT
    if n < 0:
        return NEGATIVE_FORMAT.format(str(n))

    sequence = range(n + 1)

    return POSITIVE_FORMAT.format('+'.join(map(str, sequence)), str(sum(sequence)))
    
    
class TestSumOfNumbersFrom0ToN(unittest.TestCase):
    def test_given_n_is_positive(self):
        n = 6
        actual = show_sequence(n)
        self.assertEqual(actual, "0+1+2+3+4+5+6 = 21")

    def test_given_n_is_0(self):
        n = 0
        actual = show_sequence(n)
        self.assertEqual(actual, "0=0")

    def test_given_n_is_negative(self):
        n = -6
        actual = show_sequence(n)
        self.assertEqual(actual, "-6<0")
