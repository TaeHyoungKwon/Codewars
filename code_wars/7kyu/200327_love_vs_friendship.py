import string
import unittest


def words_to_marks(s):
    alphabet = {char: idx for idx, char in enumerate(string.ascii_lowercase, 1)}
    return sum(alphabet[ele] for ele in s)
    
    
class TestWordsToMarks(unittest.TestCase):
    def test_should_return_100_when_given_s_is_attitude(self):
        s = 'attitude'
        actual = words_to_marks(s)
        self.assertEqual(actual, 100)
