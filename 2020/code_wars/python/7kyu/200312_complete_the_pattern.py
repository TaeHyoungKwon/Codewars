import unittest

NEW_LINE = "\n"


def pattern(n):
    return NEW_LINE.join([str(ele) * ele for ele in range(1, n + 1)])


class TestPattern(unittest.TestCase):
    def test_should_return_empty_string_when_given_n_is_less_than_1(self):
        actual = pattern(0)
        self.assertEqual(actual, "")

    def test_should_return_1_when_given_n_is_1(self):
        actual = pattern(1)
        self.assertEqual(actual, "1")

    def test_pattern_n_is_more_than_two(self):
        actual = pattern(2)
        self.assertEqual(actual, "1\n22")
