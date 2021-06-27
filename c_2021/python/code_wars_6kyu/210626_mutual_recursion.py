import unittest


def f(n):
    if n == 0:
        return 1
    return n - m(f(n - 1))


def m(n):
    if n == 0:
        return 0
    return n - f(m(n - 1))
    
    
class TestMutualRecursion(unittest.TestCase):
    def test_mutual_recursion(self):
        self.assertEqual(f(0), 1)
        self.assertEqual(m(0), 0)
        self.assertEqual(f(5), 3)
        self.assertEqual(m(5), 3)
        self.assertEqual(m(10), 6)