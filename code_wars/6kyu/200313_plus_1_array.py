import unittest

LAST_SINGLE_DIGIT = 9
ZERO = 0


def up_array(arr):
    invalid_array = not arr or any(ele for ele in arr if ele < ZERO or ele > LAST_SINGLE_DIGIT)
    return None if invalid_array else list(map(int, str(int("".join(map(str, arr))) + 1)))


class TestUpArray(unittest.TestCase):
    def test_should_return_none_when_given_arr_is_not_sigle_digit(self):
        arr = [10]
        actual = up_array(arr)
        self.assertEqual(actual, None)

    def test_should_return_none_when_given_arr_has_same(self):
        arr = [1, -1]
        actual = up_array(arr)
        self.assertEqual(actual, None)

    def test_should_return_none_when_given_arr_is_empty(self):
        arr = []
        actual = up_array(arr)
        self.assertEqual(actual, None)

    def test_up_array(self):
        arr = [2, 3, 9]
        actual = up_array(arr)
        self.assertEqual(actual, [2, 4, 0])
