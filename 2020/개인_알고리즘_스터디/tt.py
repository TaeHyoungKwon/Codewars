from collections import defaultdict
import unittest


def defaultdict_test(s):
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    return d


class TestDefaultDict(unittest.TestCase):
    def test_defaultdict(self):
        s = 'mississippi'
        actual = defaultdict_test(s)
        self.assertEqual(actual['m'], 1)
        self.assertEqual(actual['i'], 4)
        self.assertEqual(actual['p'], 2)
        self.assertEqual(actual['s'], 4)
