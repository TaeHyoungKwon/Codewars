import unittest


def index_equals_value(arr):
    for idx, ele in enumerate(arr):
        if idx == ele:
            return ele
    return -1
    
    
class TestElementEqualsItsIndex(unittest.TestCase):
    def test_should_return_0_when_arr_has_only_0(self):
        arr = [0]
        actual = index_equals_value(arr)
        self.assertEqual(actual, 0)

    def test_should_return_negative_1_when_arr_has_not_index_equals_value(self):
        arr = [9, 10, 11, 12, 13]
        actual = index_equals_value(arr)
        self.assertEqual(actual, -1)

    def test_should_return_1_when_arr_with_multiple_matches(self):
        arr = [-5, 1, 2, 3, 4, 5, 7, 10, 15]
        actual = index_equals_value(arr)
        self.assertEqual(actual, 1)

    def test_should_return_3_when_small_array(self):
        arr = [-3, 0, 1, 3, 10]
        actual = index_equals_value(arr)
        self.assertEqual(actual, 3)

