import unittest


def alternateCase(s):
    temp = ''
    for ele in s:
        if ele.isupper():
            temp += ele.lower()
        elif ele.islower():
            temp += ele.upper()
        else:
            temp += ele

    return temp


class TestAlternateCase(unittest.TestCase):
    def test_alternate_case(self):
        self.assertEqual(alternateCase(s="Hello World"), "hELLO wORLD")
