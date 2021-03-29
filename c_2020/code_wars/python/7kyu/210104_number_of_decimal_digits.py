import unittest


def digits(n):
    return len(str(n))


class TestDigits(unittest.TestCase):
    def test_digits(self):
        self.assertEqual(digits(5), 1)
        self.assertEqual(digits(10), 2)
        self.assertEqual(digits(110), 3)
