import re
import unittest


REGEX = re.compile(r'^\s*$')


def whitespace(string):
    return bool(re.match(REGEX, string))


class TestPowers(unittest.TestCase):
    def test_whitespace(self):
        self.assertEqual(whitespace(""), True)
        self.assertEqual(whitespace(" "), True)
        self.assertEqual(whitespace("\n\r\n\r "), True)
        self.assertEqual(whitespace("a"), False)
        self.assertEqual(whitespace("w\n"), False)
        self.assertEqual(whitespace("\t"), True)
        self.assertEqual(whitespace(" a\n"), False)
        self.assertEqual(whitespace("\t \n\r\n  "), True)
        self.assertEqual(whitespace("\n\r\n\r 3"), False)
