import unittest


def reverse_string(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        s = ["a", "b", "c", "d", "e"]
        actual = reverse_string(s)
        self.assertEqual(actual, ["e", "d", "c", "b", "a"])
