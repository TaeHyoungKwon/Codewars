import unittest
from collections import Counter


def duplicate_encode(word):
    lower_word = word.lower()
    counter = Counter(lower_word)
    return ''.join(')' if counter[char] > 1 else '(' for char in lower_word)
    
    
class TestDuplicateEncode(unittest.TestCase):
    def test_duplicate_encode_when_word_is_din(self):
        word = 'din'
        actual = duplicate_encode(word)
        self.assertEqual(actual, '(((')

    def test_duplicate_encode_when_word_is_recede(self):
        word = 'recede'
        actual = duplicate_encode(word)
        self.assertEqual(actual, '()()()')

    def test_duplicate_encode_when_word_is_Success(self):
        word = 'Success'
        actual = duplicate_encode(word)
        self.assertEqual(actual, ')())())')
