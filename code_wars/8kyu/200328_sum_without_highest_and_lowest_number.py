import unittest


def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0

    arr.remove(min(arr))
    arr.remove(max(arr))

    return sum(arr)


class TestSumArrays(unittest.TestCase):
    """TestSumArrays"""

    def test_should_return_zero_when_given_arr_is_none(self):
        arr = None
        result = sum_array(arr)
        self.assertEqual(result, 0)

    def test_should_return_zero_when_given_arr_is_empty_list(self):
        arr = []
        result = sum_array(arr)
        self.assertEqual(result, 0)

    def test_should_return_zero_when_given_arr_has_only_one_element_is_positive(self):
        arr = [1]
        result = sum_array(arr)
        self.assertEqual(result, 0)

    def test_should_return_zero_when_given_arr_has_only_one_element_is_negative(self):
        arr = [-1]
        result = sum_array(arr)
        self.assertEqual(result, 0)

    def test_should_return_zero_when_given_arr_has_only_two_element_is_positive(self):
        arr = [-1, -2]
        result = sum_array(arr)
        self.assertEqual(result, 0)

    def test_should_return_zero_when_given_arr_has_only_two_element_is_negative(self):
        arr = [1, 2]
        result = sum_array(arr)
        self.assertEqual(result, 0)

    def test_success_case(self):
        arr = [6, 2, 1, 8, 10]
        result = sum_array(arr)
        self.assertEqual(result, 16)

    def test_sum_array_edge_case(self):
        arr = [6, 0, 1, 10, 10]
        result = sum_array(arr)
        self.assertEqual(result, 17)
