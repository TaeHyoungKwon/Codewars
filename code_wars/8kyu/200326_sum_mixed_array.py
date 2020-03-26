import unittest


def sum_mix(arr):
    return sum(map(int, arr))
    
    
class TestSumMix(unittest.TestCase):
    def test_all_element_is_numeric(self):
        arr = [1, 2, 3, 4, 5]
        actual = sum_mix(arr)
        self.assertEqual(actual, 15)

    def test_mixed_element_string_and_numeric(self):
        arr = [9, 3, '7', '3']
        actual = sum_mix(arr)
        self.assertEqual(actual, 22)
