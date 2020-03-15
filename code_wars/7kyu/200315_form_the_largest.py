import unittest


def max_number(n):
    return int(''.join(sorted(str(n), reverse=True)))
    
    
class TestMaxNumber(unittest.TestCase):
    def test_max_number(self):
        actual = max_number(213)
        self.assertEqual(actual, 321)
