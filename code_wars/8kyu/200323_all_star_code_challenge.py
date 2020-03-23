import unittest


def str_count(strng, letter):
    return strng.count(letter)
    
    
class TestStrCount(unittest.TestCase):
    def test_str_count(self):
        string, letter = 'abcde', 'a'
        actual = str_count(string, letter)
        self.assertEqual(actual, 1)
        