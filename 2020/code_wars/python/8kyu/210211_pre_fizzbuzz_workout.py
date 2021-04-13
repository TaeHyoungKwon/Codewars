import unittest


def pre_fizz(n):
    return list(range(1, n + 1))
    
    
class TestPreFizz(unittest.TestCase):
    def test_pre_fizz(self):
        self.assertEqual(pre_fizz(n=1), [1])
