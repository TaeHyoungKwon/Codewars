import unittest


def digitize(n):
    return [int(char) for char in str(n)]


class TestDigitize(unittest.TestCase):
    def test_digitize(self):
        self.assertEqual(digitize(123), [1, 2, 3])
