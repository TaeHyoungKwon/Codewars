import unittest


def quarter_of(month):
    return (month + 2) // 3
    
    
class TestQuaterOf(unittest.TestCase):
    def test_quarter_of(self):
        self.assertEqual(quarter_of(month=3), 1)
        self.assertEqual(quarter_of(month=4), 2)
        self.assertEqual(quarter_of(month=8), 3)
        self.assertEqual(quarter_of(month=11), 4)
