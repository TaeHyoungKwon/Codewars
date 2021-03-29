import unittest


def is_palindrome(s):
    lower_s = s.lower()
    return lower_s == lower_s[::-1]


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_should_return_false(self):
        self.assertFalse(is_palindrome(s="nope"))

    def test_palindrome_should_return_true(self):
        self.assertTrue(is_palindrome(s="Yay"))
