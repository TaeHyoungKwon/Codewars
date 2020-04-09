import math
import unittest


def square_area(A):
    return round(((2 * A) / math.pi) ** 2, 2)
    
    
class TestSquareArea(unittest.TestCase):
    def test_square_area(self):
        A = 2
        actual = square_area(A)
        self.assertEqual(actual, 1.62)
