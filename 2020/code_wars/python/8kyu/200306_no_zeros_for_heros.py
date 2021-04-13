import unittest


def no_boring_zeros(n):
    return int(str(n).strip("0")) if n else n
    
    
class TestNoBoringZeros(unittest.TestCase):
    def test_should_return_0_when_given_n_is_0(self):
        actual = no_boring_zeros(0)
        self.assertEqual(actual, 0)

    def test_last_zero_count_is_only_one(self):
        actual = no_boring_zeros(150)
        self.assertEqual(actual, 15)

    def test_last_zero_count_is_more_than_two(self):
        actual = no_boring_zeros(1500)
        self.assertEqual(actual, 15)

    def test_last_zero_count_is_more_than_two_is_negative(self):
        actual = no_boring_zeros(-1500)
        self.assertEqual(actual, -15)

    def test_last_zero_count_is_more_than_two_num_by_num(self):
        actual = no_boring_zeros(-10500)
        self.assertEqual(actual, -105)
