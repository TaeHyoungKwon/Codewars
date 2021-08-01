import unittest
from itertools import zip_longest


def uniq(seq):
    return [first for first, second in zip_longest(seq, seq[1:]) if first != second]


class TestUniq(unittest.TestCase):
    def test_uniq(self):
        self.assertEqual(uniq(seq=["a", "a", "b", "b", "c", "a", "b", "c", "c"]), ["a", "b", "c", "a", "b", "c"])
