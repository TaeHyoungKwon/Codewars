import unittest


def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


class TestAnagram(unittest.TestCase):
    def test_should_return_true_when_test_and_original_is_anagram(self):
        self.assertTrue(is_anagram(test='Creative', original='Reactive'))

    def test_should_return_false_when_test_and_original_is_not_anagram(self):
        self.assertFalse(is_anagram(test='apple', original='pple'))
