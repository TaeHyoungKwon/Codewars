import unittest


def first_non_consecutive(arr):
    for ele in list(zip(arr, arr[1:])):
        if ele[1] - ele[0] != 1:
            return ele[1]
    return None


class TestFirstNonConsecutive(unittest.TestCase):
    def test_should_return_none_when_all_of_arr_element_is_consecutive(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        actual = first_non_consecutive(arr)
        self.assertEqual(actual, None)

    def test_should_return_6_when_given_arr_is_1_to_8_without_5(self):
        arr = [1, 2, 3, 4, 6, 7, 8]
        actual = first_non_consecutive(arr)
        self.assertEqual(actual, 6)
