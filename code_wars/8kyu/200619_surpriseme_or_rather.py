import unittest


def super_size(n):
    return int(''.join(sorted(str(n), reverse=True)))
    
    
class TestSuperSize(unittest.TestCase):
    def test_super_size(self):
        n = 513
        actual = super_size(n)
        self.assertEqual(actual, 531)
