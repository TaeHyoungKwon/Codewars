import unittest


def camel_case(string):
    return ''.join(ele[0].upper() + ele[1:] for ele in string.split(' ') if ele)


class TestCamelCase(unittest.TestCase):
    def test_should_return_empty_space_when_given_string_empty(self):
        string = ''
        result = camel_case(string)
        self.assertEqual(result, '')

    def test_should_return_camel_case_string_without_space(self):
        string = ' camel case word'
        result = camel_case(string)
        self.assertEqual(result, 'CamelCaseWord')