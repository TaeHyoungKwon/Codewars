import unittest


def last(*args):
    if len(args) == 1 and isinstance(args[0], str):
        return args[0][-1]
    return args[0][-1] if isinstance(args[0], list) else args[-1]


class TestLast(unittest.TestCase):
    def test_last_argument_is_list(self):
        l = [1, 2, 3, 4, 5]
        actual = last(l)
        self.assertEqual(actual, 5)

    def test_last_argument_is_string(self):
        l = "abcde"
        actual = last(l)
        self.assertEqual(actual, "e")

    def test_last_argument_is_mixed(self):
        self.assertEqual(last(1, "b", 3, "d", 5), 5)

    def test_last_argument_is_mixed_only_char(self):
        self.assertEqual(last("a", "b", "c", "z"), "z")
