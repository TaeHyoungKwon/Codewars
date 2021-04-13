import unittest


def remove(s, n):
    return s.replace('!', '', n)
    
    
class TestRemove(unittest.TestCase):
    def test_remove(self):
        self.assertEqual(remove("!!!Hi !!hi!!! !hi", 1), "!!Hi !!hi!!! !hi")
        self.assertEqual(remove("!!!Hi !!hi!!! !hi", 3), "Hi !!hi!!! !hi")
