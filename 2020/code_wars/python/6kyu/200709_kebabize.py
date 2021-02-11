import unittest


def kebabize(string):
    new_string = ''.join('-' + ele if ele.isupper() else ele for ele in string if not ele.isdigit())
    return '-'.join(ele.lower() for ele in new_string.split('-') if ele != '')
    
    
class TestKebabize(unittest.TestCase):
    def test_kebabize(self):
        string = 'myCamelCasedString'
        actual = kebabize(string)
        self.assertEqual(actual, 'my-camel-cased-string')

    def test_kebabize_edge_case(self):
        string = 'SOS'
        actual = kebabize(string)
        self.assertEqual(actual, 's-o-s')
