import unittest


def unlucky_number(n):
    return sum(not ('4' in str(ele) or '7' in str(ele)) for ele in list(range(0, n + 1, 13)))


class TestUnLuckyNumber(unittest.TestCase):
    def test_should_return_2_when_given_n_is_20(self):
        n = 20
        actual = unlucky_number(n)
        self.assertEqual(actual, 2)

    def test_should_return_7_when_given_n_is_100(self):
        n = 100
        actual = unlucky_number(n)
        self.assertEqual(actual, 7)

    def test_should_return_21_when_given_n_is_351(self):
        n = 351
        actual = unlucky_number(n)
        self.assertEqual(actual, 21)
