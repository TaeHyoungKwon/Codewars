import unittest


def is_palindrome(palindrome_string: str) -> bool:

    def _inner_is_palindrome(alphabet_list: list) -> bool:
        while len(alphabet_list) > 1:
            if alphabet_list.pop(0) != alphabet_list.pop():
                return False
        return True

    return _inner_is_palindrome([char for char in palindrome_string if char.isalnum()])


class TestPalindrome(unittest.TestCase):
    def test_is_paldindrome_with_true(self):
        self.assertTrue(is_palindrome('abcba'))

    def test_is_paldindrome_with_false(self):
        self.assertFalse(is_palindrome('abcbaa'))
