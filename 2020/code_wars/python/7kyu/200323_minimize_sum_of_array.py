import unittest


def min_sum(arr):
    sorted_arr = sorted(arr)
    length = len(arr)

    return sum(e1 * e2
               for e1, e2 in [[sorted_arr[idx], sorted_arr[length - 1 - idx]]
                              for idx, ele in enumerate(range(length // 2))])


class TestMinSum(unittest.TestCase):
    def test_min_sum(self):
        arr = [9, 2, 8, 7, 5, 4, 0, 6]
        actual = min_sum(arr)
        self.assertEqual(actual, 74)
