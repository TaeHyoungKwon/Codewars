import string
import unittest


def calc_count(case, s):
    return len(list(filter(lambda x: x in case, s)))


def solve(s):
    return [
        calc_count(string.ascii_uppercase, s),
        calc_count(string.ascii_lowercase, s),
        calc_count(string.digits, s),
        calc_count(string.punctuation, s),
    ]


class TestSimpleStringCharacters(unittest.TestCase):
    def test_simple_string_characters(self):
        s = "Codewars@codewars123.com"
        actual = solve(s)
        self.assertEqual(actual, [1, 18, 3, 2])
