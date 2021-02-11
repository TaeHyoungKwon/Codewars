import unittest


def is_palindrome(palindrome_string: str) -> bool:
    s = ''.join(char for char in palindrome_string if char.isalnum())
    return s == s[::-1]


class TestPalindrome(unittest.TestCase):
    def test_is_paldindrome_with_true(self):
        self.assertTrue(is_palindrome('abcba'))

    def test_is_paldindrome_with_false(self):
        self.assertFalse(is_palindrome('abcbaa'))
