import unittest


def longest_palindrome(s):
    def is_palindrome(element):
        return element == element[::-1]

    all_sub_strings = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

    max_value = 0
    for sub_string in all_sub_strings:
        if is_palindrome(sub_string):
            if len(sub_string) > max_value:
                max_value = len(sub_string)
    return max_value
    
    
class TestLongestPalindrome(unittest.TestCase):
    def test_longest_palindrome_with_one_char(self):
        self.assertEqual(longest_palindrome("a"), 1)

    def test_longest_palindrome_with_two_char(self):
        self.assertEqual(longest_palindrome("aa"), 2)

    def test_longest_palindrome_with_three_char(self):
        self.assertEqual(longest_palindrome("aab"), 2)

    def test_longest_palindrome(self):
        self.assertEqual(longest_palindrome("baablkj12345432133d"), 9)

    def test_longest_palindrome_with_edge_case(self):
        self.assertEqual(longest_palindrome("abcdefghba"), 1)
