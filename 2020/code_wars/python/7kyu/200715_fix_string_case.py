import unittest


def largest(n, xs):
    return sorted(sorted(xs, reverse=True)[:n])
    
    
class TestLargest(unittest.TestCase):
    def test_largest(self):
        n, xs = 2, [10,9,8,7,6,5,4,3,2,1]
        actual = largest(n, xs)
        self.assertEqual(actual, [9, 10])
