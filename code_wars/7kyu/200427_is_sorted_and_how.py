import unittest

ASCENDING_MSG = 'yes, ascending'
DESCENDING_MSG = 'yes, descending'
NO_MSG = 'no'


def is_sorted_and_how(arr):
    adjacent_element_list = list(zip(arr, arr[1:]))
    if all(second - first > 0 for first,  second in adjacent_element_list):
        return ASCENDING_MSG
    elif all(first - second > 0 for first,  second in adjacent_element_list):
        return DESCENDING_MSG
    else:
        return NO_MSG
    
    
class TestIsSortedAndHow(unittest.TestCase):
    def test_should_return_ascending_message(self):
        arr = [1, 2]
        actual = is_sorted_and_how(arr)
        self.assertEqual(actual, ASCENDING_MSG)

    def test_should_return_descending_message(self):
        arr = [15, 7, 3, -8]
        actual = is_sorted_and_how(arr)
        self.assertEqual(actual, DESCENDING_MSG)

    def test_should_return_no_message(self):
        arr = [4, 2, 30]
        actual = is_sorted_and_how(arr)
        self.assertEqual(actual, NO_MSG)
