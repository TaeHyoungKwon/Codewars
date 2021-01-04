import unittest


def averages(arr):
    if not arr or len(arr) == 1:
        return []
    return [(num + follower) / 2 for num, follower in zip(arr, arr[1:])]


class TestAverages(unittest.TestCase):
    def test_should_return_empty_list_when_arr_is_empty(self):
        arr = []
        actual = averages(arr)
        self.assertEqual(actual, [])

    def test_should_return_empty_list_when_arr_length_is_one(self):
        arr = [1]
        actual = averages(arr)
        self.assertEqual(actual, [])

    def test_averages(self):
        arr = [2, -2, 2, -2, 2]
        actual = averages(arr)
        self.assertEqual(actual, [0, 0, 0, 0])
