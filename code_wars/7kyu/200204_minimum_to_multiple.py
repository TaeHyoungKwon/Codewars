import unittest


def calc_mininum(a, x):
    for idx in range((a - x) + 1):
        if (a + idx) % x == 0:
            return idx
        if (a - idx) % x == 0:
            return idx


def minimum(a, x):
    # TODO: 다 못품..
    return 0 if a == 0 else calc_mininum(max(a, x), min(a, x))


class TestMinimum(unittest.TestCase):
    def test_should_return_0_when_given_a_is_0(self):
        a, x = 0, 6
        actual = minimum(a, x)
        self.assertEqual(actual, 0)

    def test_should_return_2_when_given_a_is_10_x_is_6(self):
        a, x = 10, 6
        actual = minimum(a, x)
        self.assertEqual(actual, 2)

    def test_should_return_15_when_given_a_is_89_x_is_74(self):
        a, x = 89, 74
        actual = minimum(a, x)
        self.assertEqual(actual, 15)
