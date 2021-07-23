import unittest


def _factorial(n):
    result = 1
    for num in range(1, n + 1)[::-1]:
        result *= num
    return result


def choose(n, k):
    return _factorial(n) // _factorial(k) * _factorial(n - k)


class TestChoose(unittest.TestCase):
    def test_choose_small_num_case_1(self):
        self.assertEqual(choose(n=1, k=1), 1)

    def test_choose_small_num_case_2(self):
        self.assertEqual(choose(n=5, k=4), 5)
