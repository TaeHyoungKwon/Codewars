import unittest


def get_even_numbers(arr):
    return list(ele for ele in arr if ele % 2 == 0)


class TestEvnNumbers(unittest.TestCase):
    def test_should_return_empty_list_when_given_arr_is_empty(self):
        actual = get_even_numbers([])
        self.assertEqual(actual, [])

    def test_should_return_empty_list_when_given_arr_has_only_one_element(self):
        actual = get_even_numbers([1])
        self.assertEqual(actual, [])

    def test_should_return_even_numbers_when_given_arr_mixed_even_and_odd(self):
        actual = get_even_numbers([1, 2, 3, 4, 5])
        self.assertEqual(actual, [2, 4])

    def test_should_return_even_numbers_when_all_of_given_arr_is_even(self):
        actual = get_even_numbers([2, 4, 6])
        self.assertEqual(actual, [2, 4, 6])

    def test_should_return_empty_list_when_all_of_given_arr_is_odd(self):
        actual = get_even_numbers([1, 3, 5])
        self.assertEqual(actual, [])
