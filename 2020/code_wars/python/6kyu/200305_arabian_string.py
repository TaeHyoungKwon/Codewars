import unittest


def camelize(str_):
    def _make_new_string(string):
        return ''.join(ele if ele.isalnum() else ' ' for ele in string)
    return ''.join(ele.capitalize() for ele in _make_new_string(str_).split())
    
    
class TestCamelize(unittest.TestCase):
    def test_string_with_lowercase(self):
        actual = camelize('java script')
        self.assertEqual(actual, 'JavaScript')

    def test_string_with_mixed_lowercase_and_uppercase(self):
        actual = camelize('cODE warS')
        self.assertEqual(actual, 'CodeWars')

    def test_string_with_mixed_no_alphabet_and_numeric(self):
        actual = camelize("your-NaMe-here")
        self.assertEqual(actual, 'YourNameHere')

    def test_string_with_mixed_no_alphabet_and_numeric_more_than_two(self):
        actual = camelize("your>NaMe=here")
        self.assertEqual(actual, 'YourNameHere')
