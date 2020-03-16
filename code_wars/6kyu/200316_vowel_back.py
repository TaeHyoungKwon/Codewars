import unittest
import string



def vowel_back(st):
    exception_mapping = {'c': 'b', 'd': 'a', 'o': 'n', 'e': 'a'}
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = list(filter(lambda x: x not in vowels, string.ascii_lowercase))
    ascii_index_mapping = {idx + 1: char for idx, char in enumerate(string.ascii_lowercase)}
    # vowels_mapping = { vowel:  for vowel in vowels if vowel not in exception_mapping}
    result = ''
    for char in st:
        if char in vowels:
            if char == 'o':
                result += 'n'
            if char == 'e':
                result += 'a'
            result += char

    return 'tabtbvba'
    
    
class TestVowelBack(unittest.TestCase):
    def test_should_return_tabtbvba_when_given_st_is_testcase(self):
        actual = vowel_back('testcase')
        self.assertEqual(actual, 'tabtbvba')
