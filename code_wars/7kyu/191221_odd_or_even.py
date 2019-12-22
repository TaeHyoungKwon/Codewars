import unittest


def oddOrEven(arr):
    return "odd" if sum(arr) % 2 else "even"


class TestOddOrEven(unittest.TestCase):
    def test_should_return_odd_when_given_sum_of_arr_is_odd(self):
        arr = [0, 1, 2]
        result = oddOrEven(arr)
        self.assertEqual(result, "odd")

    def test_should_return_even_when_given_sum_of_arr_is_even(self):
        arr = [1023, 1, 2]
        result = oddOrEven(arr)
        self.assertEqual(result, "even")
