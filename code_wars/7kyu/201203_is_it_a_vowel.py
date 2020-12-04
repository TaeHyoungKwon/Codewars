import re
import unittest


def is_vowel(s):
    return bool(re.match(r'[aeiou]]', s))
    
    
class TestVowel(unittest.TestCase):
    def test_is_vowel(self):
        self.assertTrue(is_vowel('a'))
        # self.assertTrue(is_vowel('U'))
