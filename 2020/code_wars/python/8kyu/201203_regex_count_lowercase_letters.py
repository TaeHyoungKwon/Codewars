import re
import unittest


def lowercase_count(strng):
    return len(re.findall('[a-z]', strng))
    
    
class TestLowerCaseCount(unittest.TestCase):
    def test_lowercase_count_case_one(self):
        self.assertEqual(lowercase_count('abc'), 3)
        self.assertEqual(lowercase_count('abcABC123'), 3)
