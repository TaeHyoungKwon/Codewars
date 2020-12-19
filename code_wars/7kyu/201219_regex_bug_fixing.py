import unittest


import re


def filter_words(phrase):
    return re.sub("bad|mean|ugly|horrible|hideous", "awesome", phrase, flags=re.IGNORECASE)


class TestFilterWords(unittest.TestCase):
    def test_filter_words(self):
        self.assertEqual(filter_words("You're Bad! timmy!"), "You're awesome! timmy!")
        self.assertEqual(filter_words("You're MEAN! timmy!"), "You're awesome! timmy!")
