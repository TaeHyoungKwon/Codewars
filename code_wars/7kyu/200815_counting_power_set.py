import unittest


def powers(lst):
    return
    
    
class TestCountingPowerSets(unittest.TestCase):
    def test_powers(self):
        lst = [1, 2, 3]
        actual = powers(lst)
        self.assertEqual(actual, 8)
