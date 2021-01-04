import unittest


def process_array(arr, callback):
    return [callback(ele) for ele in arr]
    
    
class TestProcessArray(unittest.TestCase):
    def test_process_array(self):
        self.assertEqual(process_array([-1, 1, 2, 3, 4, 5], lambda val: val ** 3), [-1, 1, 8, 27, 64, 125 ])
