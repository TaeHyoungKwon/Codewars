import unittest


def has_unique_chars(string):
    return len(string) == len(set(string))
    
    
class TestAllUnique(unittest.TestCase):
    def test_has_unique_chars(self):
        string = 'abcdef'
        actual = has_unique_chars(string)
        self.assertTrue(actual)

    def test_has_unique_chars_with_duplicated_chars(self):
        string = '++-'
        actual = has_unique_chars(string)
        self.assertFalse(actual)
