import unittest


def sum_of_n(n):
    def _get_sum_of_n(num):
        return [(index_ * (index_ + 1)) // 2 for index_ in range(num + 1)]
    if n >= 0:
        return _get_sum_of_n(n)
    n = abs(n)
    return list(map(lambda x: -x, _get_sum_of_n(n)))

    
    
class TestSumOfN(unittest.TestCase):
    def test_sum_of_n_on_n_is_3(self):
        n = 3
        actual = sum_of_n(n)
        self.assertEqual(actual, [0, 1, 3, 6])

    def test_sum_of_n_on_n_is_0(self):
        n = 0
        actual = sum_of_n(n)
        self.assertEqual(actual, [0])

    def test_sum_of_n_on_n_is_negative_4(self):
        n = -4
        actual = sum_of_n(n)
        self.assertEqual(actual, [0, -1, -3, -6, -10])
