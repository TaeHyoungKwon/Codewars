import unittest


def to_alternating_case(string):
    temp = []
    for ele in string:
        if ele.isupper():
            temp.append(ele.lower())
        elif ele.islower():
            temp.append(ele.upper())
        else:
            temp.append(ele)
    return ''.join(temp)
    
    
class Test(unittest.TestCase):
    def test_to_alternating_case_with_digit(self):
        string = '12345'
        actual = to_alternating_case(string)
        self.assertEqual(actual, '12345')

    def test_to_alternating_case_with_alphabet_mixed_upper_and_lower(self):
        string = 'hello WORLD'
        actual = to_alternating_case(string)
        self.assertEqual(actual, 'HELLO world')
