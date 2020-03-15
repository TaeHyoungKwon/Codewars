import unittest
from collections import Counter


def grabscrab(word, possible_words):
    return [possible_word for possible_word in possible_words if Counter(word) == Counter(possible_word)]


class TestGrabScrab(unittest.TestCase):
    def test_should_return_empty_list_when_given_word_is_not_matched_in_possible_words(self):
        word, possible_words = "oo", ["donkey", "pool", "horse", "loop"]
        actual = grabscrab(word, possible_words)
        self.assertEqual(actual, [])

    def test_should_return_first_str_when_given_word_is_matched_in_possible_words(self):
        word, possible_words = "tirsf", ["first", "second"]
        actual = grabscrab(word, possible_words)
        self.assertEqual(actual, ["first"])
