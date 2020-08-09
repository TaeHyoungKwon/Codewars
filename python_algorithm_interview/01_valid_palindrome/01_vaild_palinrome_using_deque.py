import unittest
from collections import deque


def is_palindrome(palindrome_string: str) -> bool:

    def _inner_is_palindrome(lower_alphabet_list):
        while len(lower_alphabet_list) > 1:
            if lower_alphabet_list.popleft() != lower_alphabet_list.pop():
                return False
        return True

    lower_case_deque = deque()
    for char in palindrome_string:
        if char.isalnum():
            lower_case_deque.append(char.lower())

    return _inner_is_palindrome(lower_case_deque)


class TestPalindrome(unittest.TestCase):
    def test_is_paldindrome_with_true(self):
        self.assertTrue(is_palindrome('abcba'))

    def test_is_paldindrome_with_false(self):
        self.assertFalse(is_palindrome('abcbaa'))
