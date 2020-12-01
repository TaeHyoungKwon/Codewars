import unittest


def adjacent_element_product(array):
    return max(first * second for first, second in zip(array, array[1:]))
    
    
class TestAdjacentElementProduct(unittest.TestCase):
    def test_adjacent_element_product(self):
        array = [5, 1, 2, 3, 1, 4]
        actual = adjacent_element_product(array)
        self.assertEqual(actual, 6)
