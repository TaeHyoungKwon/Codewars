import unittest

VOWEL = {'a', 'e', 'i', 'o', 'u'}


def replace_exclamation(s):
    return ''.join('!' if char.lower() in VOWEL else char for char in s)


class TestReplaceExclamation(unittest.TestCase):
    def test_replace_exclamation(self):
        s = 'aeiou'
        actual = replace_exclamation(s)
        self.assertEqual(actual, '!!!!!')

    def test_replace_exclamation_when_s_is_upper_case(self):
        s = 'ABCDE'
        actual = replace_exclamation(s)
        self.assertEqual(actual, '!BCD!')
