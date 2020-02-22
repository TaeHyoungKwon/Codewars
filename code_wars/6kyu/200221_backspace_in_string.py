import unittest


def clean_string(s):
    stack = []
    for ele in s:
        if ele != '#':
            stack.append(ele)
        else:
            if not stack:
                continue
            stack.pop()
    return ''.join(stack)
    
    
class TestCleanString(unittest.TestCase):
    def test_should_return_empty_space_when_given_s_is_empty(self):
        actual = clean_string('')
        self.assertEqual(actual, '')

    def test_clean_string_using_stack_data_structure_with_more_sharp_count(self):
        actual = clean_string('abc####d##c#')
        self.assertEqual(actual, '')

    def test_clean_string_using_stack_data_structure_with_less_sharp_count(self):
        actual = clean_string('abc#d##c')
        self.assertEqual(actual, 'ac')

    def test_clean_string_using_stack_data_structure_with_s_is_alphanumeric(self):
        actual = clean_string('hsk48hjjdfgd')
        self.assertEqual(actual, 'hsk48hjjdfgd')

    def test_clean_string_using_stack_data_structure_with_s_is_alphanumeric_and_special_char_except_sharp(self):
        actual = clean_string('`8#')
        self.assertEqual(actual, '`')
