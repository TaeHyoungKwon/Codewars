from functools import reduce
import unittest


def reverse(lst):
    return reduce(lambda acc, x: [x] + acc, lst, [])


class TestReverse(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse(lst=[1, 2, 3]), [3, 2, 1])

    def test_reverse_with_none(self):
        self.assertEqual(reverse(lst=[1, None, 14, "two"]), ["two", 14, None, 1])
