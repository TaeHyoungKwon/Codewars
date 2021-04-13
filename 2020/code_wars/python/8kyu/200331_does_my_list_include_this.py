import unittest


def include(arr, item):
    return item in arr
    
    
class TestInclude(unittest.TestCase):
    def test_should_return_true_when_item_is_belongs_to_arr(self):
        arr, item = [1, 2, 3, 4, 5], 3
        actual = include(arr, item)
        self.assertEqual(actual, True)

    def test_should_return_false_when_item_is_not_belongs_to_arr(self):
        arr, item = [1, 2, 3, 4, 5], 6
        actual = include(arr, item)
        self.assertEqual(actual, False)
