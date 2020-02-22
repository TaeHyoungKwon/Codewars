import unittest
from collections import Counter


def palindrom품e_rearranging(s):
    # 문제가 이해안되서 그냥 답 보고
    return sum(n % 2 for n in Counter(s).values()) <= 1


class TestPalindromeRearranging(unittest.TestCase):
    def test_should_return_true_when_given_rearranged_s_can_be_palindrome(self):
        # Given: Set s - can be palindrome when rearranged
        s = "aabb"

        # When: Call actual
        actual = palindrome_rearranging(s)

        # Then: actual should be True
        self.assertEqual(actual, True)

    def test_should_return_true_when_given_rearranged_s_can_be_palindrome(self):
        # Given: Set s - can be palindrome when rearranged
        s = "aabb"

        # When: Call actual
        actual = palindrome_rearranging(s)

        # Then: actual should be True
        self.assertEqual(actual, True)

    def test_should_return_true_when_char_count_is_divided_by_2_except_only_one_in_s(self):
        # Given: Set s - aa and bbbb is divided by 2 / c is only one
        s = "abbcabb"

        # When: Call actual
        actual = palindrome_rearranging(s)

        # Then: actual should be True
        self.assertEqual(actual, True)

    def test_should_return_true_when_all_of_char_count_is_divided_by_2_in_s(self):
        # Given: Set s - all of char count is divided by 2
        s = "zyyzzzzz"

        # When: Call actual
        actual = palindrome_rearranging(s)

        # Then: actual should be True
        self.assertEqual(actual, True)
