import unittest
from collections import deque


def yes_no(arr):
    def _calc_yes_no(yes_no_arr):
        deque_arr = deque(yes_no_arr)
        while deque_arr:
            yield deque_arr.popleft()
            if deque_arr:
                deque_arr.append(deque_arr.popleft())

    return list(_calc_yes_no(arr))


class TestYesNo(unittest.TestCase):
    def test_should_return_empty_list_when_given_arr_is_empty(self):
        arr = []
        actual = yes_no(arr)
        self.assertEqual(actual, [])

    def test_should_return_origin_element_when_given_arr_length_is_1(self):
        arr = ["a"]
        actual = yes_no(arr)
        self.assertEqual(actual, ["a"])

    def test_should_return_origin_element_when_given_arr_length_is_2(self):
        arr = ["a", "b"]
        actual = yes_no(arr)
        self.assertEqual(actual, ["a", "b"])

    def test_yes_no_with_num_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = yes_no(arr)
        self.assertEqual(actual, [1, 3, 5, 7, 9, 2, 6, 10, 8, 4])

    def test_yes_no_with_string_array(self):
        arr = ["this", "code", "is", "right", "the"]
        actual = yes_no(arr)
        self.assertEqual(actual, ["this", "is", "the", "right", "code"])
