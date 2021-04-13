import unittest
from math import log2


def strongest_even(n, m):
    if int(log2(m)) > int(log2(n)):
        return 2 ** int(log2(m))

    n += n % 2
    m -= m % 2
    if n == m:
        return n

    return 2 * strongest_even(n // 2, m // 2)


class TestStrongestEven(unittest.TestCase):
    def test_should_return_8_when_given_n_and_m_is_between_5_and_10(self):
        n, m = 5, 10
        result = strongest_even(n, m)
        self.assertEqual(result, 8)

    def test_should_return_48_when_given_n_and_m_is_between_48_and_56(self):
        n, m = 48, 56
        result = strongest_even(n, m)
        self.assertEqual(result, 48)

    def test_should_return_192_when_given_n_and_m_is_between_129_and_193(self):
        n, m = 129, 193
        result = strongest_even(n, m)
        self.assertEqual(result, 192)

    def test_should_return_2_when_given_n_and_m_is_between_1_and_2(self):
        n, m = 1, 2
        result = strongest_even(n, m)
        self.assertEqual(result, 2)
