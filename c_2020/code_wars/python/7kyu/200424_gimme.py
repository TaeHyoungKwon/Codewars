import unittest


def gimme(input_array):
    index_mapped_array = [(ele, idx) for idx, ele in enumerate(input_array)]
    sorted_index_mapped_array = sorted(index_mapped_array)
    return sorted_index_mapped_array[len(index_mapped_array) // 2][1]
    
    
class Test(unittest.TestCase):
    def test_gimme(self):
        input_array = [2, 3, 1]
        actual = gimme(input_array)
        self.assertEqual(actual, 0)
