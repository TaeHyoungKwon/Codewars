import unittest


def compare(s1, s2):

    def sum_ascii(s):
        return sum(ord(alpha.upper()) for alpha in s)

    result = _check_none_or_not_alphabet(s1)
    if result:
        s1 = ""

    result = _check_none_or_not_alphabet(s2)
    if result:
        s2 = ""

    return sum_ascii(s1) == sum_ascii(s2)


def _check_none_or_not_alphabet(s):
    return s is None or not s.isalpha()


class TestCompare(unittest.TestCase):
    def test_compare_with_none(self):
        self.assertTrue(compare(s1=None, s2=""))

    def test_compare_with_none_alphabet(self):
        self.assertTrue(compare(s1="!!", s2="7476"))

    def test_compare(self):
        self.assertTrue(compare(s1="AD", s2="BC"))



"""
import re

def ascii_sum(s):
    return sum(map(ord, re.sub('(?=.*[^A-Z]).*', '', (s or '').upper())))

def compare(s1, s2):
    return ascii_sum(s1) == ascii_sum(s2)
"""