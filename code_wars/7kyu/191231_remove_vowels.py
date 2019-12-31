import unittest


def remove_vowels(strng):
    return ''.join(ele for ele in strng
                   if ele not in {'a', 'e', 'i', 'o', 'u'})
    
    
class TestRemoveVowels(unittest.TestCase):
    def test_should_return_without_vowels(self):
        # Given: Set strng
        strng = 'drake'
        # When: Call revmoe_vowels
        actual = remove_vowels(strng)
        # Then: revmoe_vowels should return without vowels
        self.assertEqual(actual, 'drk')
        