import unittest

VOWEL = {'a', 'e', 'i', 'o', 'u'}


def shortcut(s):
    return ''.join(filter(lambda char: char not in VOWEL, s))
    
    
class TestShortCut(unittest.TestCase):
    def test_should_delete_all_vowel_in_given_s(self):
        s = 'hello'
        actual = shortcut(s)
        self.assertEqual(actual, 'hll')
