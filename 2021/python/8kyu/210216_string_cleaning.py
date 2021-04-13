import re
import unittest


# def string_clean(s):
#     return ''.join(ele for ele in s if not ele.isnumeric())

def string_clean(s):
    return re.sub(r'[0-9]', '', s)
    
    
class TestStringClean(unittest.TestCase):
    def test_string_clean_with_empty_string(self):
        self.assertEqual(string_clean(s=""), "")

    def test_string_clean_with_special_char(self):
        self.assertEqual(string_clean(s="! !"), "! !")

    def test_string_clean_with_alphabet(self):
        self.assertEqual(string_clean(s="abcde "), "abcde ")

    def test_string_clean_with_alphabet_special_char_and_num(self):
        self.assertEqual(string_clean(s="(E3at m2e2!!)"), "(Eat me!!)")
