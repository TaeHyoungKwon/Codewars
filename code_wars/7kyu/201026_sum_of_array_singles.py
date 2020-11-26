from collections import Counter
import unittest


def repeats(arr):
    return sum(key for key, value in Counter(arr).items() if value == 1)
    
    
class TestReapts(unittest.TestCase):
    def test_repeats(self):
        self.assertEqual(repeats([4, 5, 7, 5, 4, 8]), 15)
