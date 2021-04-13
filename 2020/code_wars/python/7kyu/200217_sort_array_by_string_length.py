import unittest


def sort_by_length(arr):
    return sorted(arr, key=len)
    
    
class TestSortByLength(unittest.TestCase):
    def test_sorted_array_ordered_from_shortest_to_longest(self):
        arr = ['a', 'bb', 'dddd', 'ccc']
        actual = sort_by_length(arr)
        self.assertEqual(actual, ['a', 'bb', 'ccc', 'dddd'])
