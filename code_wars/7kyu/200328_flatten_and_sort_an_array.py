import unittest


def flatten_and_sort(array):
    result = []
    for ele in array:
        result += ele
    return sorted(result)
    
    
class TestFalttenAndSort(unittest.TestCase):
    def test_should_return_empty_list_when_given_array_is_empty(self):
        array = []
        actual = flatten_and_sort(array)
        self.assertEqual(actual, [])

    def test_flatten_and_sort(self):
        array = [3, 2, 1], [7, 9, 8], [6, 4, 5]
        actual = flatten_and_sort(array)
        self.assertEqual(actual, [1, 2, 3, 4, 5, 6, 7, 8, 9])

