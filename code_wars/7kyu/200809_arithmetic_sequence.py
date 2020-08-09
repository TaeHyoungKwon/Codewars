import unittest


def nthterm(first, n, c):
    return c * (n + 1) - (c - first)
    
    
class TestNthTerm(unittest.TestCase):
    def test_nthterm(self):
        first, n, c = 1, 2, 3
        actual = nthterm(first, n, c)
        self.assertEqual(actual, 7)

    def test_nthterm_second(self):
        first, n, c = 2, 2, 2
        actual = nthterm(first, n, c)
        self.assertEqual(actual, 6)
