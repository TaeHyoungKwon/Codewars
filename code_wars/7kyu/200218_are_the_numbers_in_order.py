import unittest


def in_asc_order(arr):
    return sorted(arr) == arr
    
    
class TestInAscOrder(unittest.TestCase):
    def test_should_return_true_when_given_arr_is_sorted_by_asc(self):
        arr = [1, 2, 3, 4, 5]
        actual = in_asc_order(arr)
        self.assertEqual(actual, True)

    def test_should_return_false_when_given_arr_is_not_sorted_by_asc(self):
        arr = [5, 4, 1, 2, 3]
        actual = in_asc_order(arr)
        self.assertEqual(actual, False)
