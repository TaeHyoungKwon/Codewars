import unittest


def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)
    
    
class TestArrayPlusArray(unittest.TestCase):
    def test_array_plus_array(self):
        self.assertEqual(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)
        