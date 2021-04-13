import math
import unittest


def square_or_square_root(arr):
    def _is_integer_on_square_root(number):
        return math.sqrt(number).is_integer()
    return [math.sqrt(num) if _is_integer_on_square_root(num) else num**2 for num in arr ]
    
    
class TestSquareOrSquareRoot(unittest.TestCase):
    def test_square_or_square_root(self):
        arr = [4, 3, 9, 7, 2, 1]
        actual = square_or_square_root(arr)
        self.assertEqual(actual, [2, 9, 3, 49, 4, 1])
