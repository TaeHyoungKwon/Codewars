import unittest


def get_real_floor(n):
    if n <= 0:
        return n
    if n > 13:
        return n - 2
    return n - 1
    
    
class TestRealFloor(unittest.TestCase):
    def test_should_return_0_when_given_n_is_0_th_floor(self):
        actual = get_real_floor(0)
        self.assertEqual(actual, 0)

    def test_should_return_same_minus_floor_when_given_n_is_minus(self):
        actual = get_real_floor(-3)
        self.assertEqual(actual, -3)

    def test_real_floor_when_given_n_is_greater_than_13(self):
        actual = get_real_floor(15)
        self.assertEqual(actual, 13)

    def test_real_floor(self):
        actual = get_real_floor(5)
        self.assertEqual(actual, 4)
