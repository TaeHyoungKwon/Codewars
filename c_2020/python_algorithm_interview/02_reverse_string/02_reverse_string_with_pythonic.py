import unittest


def reverse_string(s):
    s.reverse()
    return s


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        s = ["a", "b", "c", "d", "e"]
        actual = reverse_string(s)
        self.assertEqual(actual, ["e", "d", "c", "b", "a"])
