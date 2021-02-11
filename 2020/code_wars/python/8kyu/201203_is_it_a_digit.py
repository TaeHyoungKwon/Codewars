import re
import unittest


def is_digit(n):
    return len(n) == 1 and bool(re.match(r'^\d$', n))


class TestDigit(unittest.TestCase):
    def test_is_digit_with_empty_string(self):
        self.assertFalse(is_digit(''))

    def test_is_digit_with_digit(self):
        self.assertTrue(is_digit('7'))
