import unittest


def capitalize(s):
    def _make_capitalize_each_element(string, rest):
        return ''.join(char.upper()
                       if idx % 2 == rest
                       else char
                       for idx, char in enumerate(string))
    return [_make_capitalize_each_element(s, 0), _make_capitalize_each_element(s, 1)]
    
    
class TestCapitalize(unittest.TestCase):
    def test_capitalize(self):
        s = 'abcdef'
        actual = capitalize(s)
        self.assertEqual(actual, ['AbCdEf', 'aBcDeF'])