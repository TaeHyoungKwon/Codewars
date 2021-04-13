import unittest


def palindrome_chain_length(n):
    cnt = 0

    def _is_palindrome(number):
        return str(number) == str(number)[::-1]

    while not _is_palindrome(n):
        n = n + int(str(n)[::-1])
        cnt += 1

    return cnt
    

class TestPalindromeChainLength(unittest.TestCase):
    def test_palindrome_chain(self):
        n = 87
        actual = palindrome_chain_length(n)
        self.assertEqual(actual, 4)
