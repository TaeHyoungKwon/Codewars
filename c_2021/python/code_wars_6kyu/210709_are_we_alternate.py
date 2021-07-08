import unittest

VOWEL = {"a", "e", "i", "o", "u"}


# def is_alt(s):
#     vowel, not_vowel = vowel_or_not(s)
#     return all(ele in VOWEL for ele in vowel) and all(ele not in VOWEL for ele in not_vowel)

from itertools import tee

def is_alt(s):
    xs1, xs2 = tee(map(lambda x: x in 'aeiou', s))
    next(xs2)
    return all(a != b for a, b in zip(xs1, xs2))


# def vowel_or_not(s):
#     return (s[0::2], s[1::2]) if s[0] in VOWEL else (s[1::2], s[0::2])


class TestIsAlt(unittest.TestCase):
    def test_is_all(self):
        self.assertTrue(is_alt(s="amazon"))
