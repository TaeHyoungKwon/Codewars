import unittest


def get_average(marks):
    return sum(marks) // len(marks)
    
    
class TestGetAverage(unittest.TestCase):
    def test_get_average(self):
        marks = [2, 2, 2, 2]
        actual = get_average(marks)
        self.assertEqual(actual, 2)
