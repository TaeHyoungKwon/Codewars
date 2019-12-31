import unittest


def max_multiple(divisor, bound):
    return max(ele for ele in range(1, bound + 1) if ele % divisor == 0)


class TestMaximumMultiple(unittest.TestCase):
    def test_n_should_be_greater_than_0(self):
        # Given: Set divisor, bound
        divisor, bound = 2, 7
        # When: Call max_multiple
        actual = max_multiple(divisor, bound)
        # Then: max_multiple should be greater than 0
        self.assertGreater(actual, 0)

    def test_n_should_be_divisible_by_divisor(self):
        # Given: Set divisor, bound
        divisor, bound = 2, 7
        # When: Call max_multiple
        actual = max_multiple(divisor, bound)
        # Then: max_multiple should be divisible by divisor
        self.assertTrue(actual % divisor == 0)

    def test_n_should_be_less_than_or_equal_to_bound(self):
        # Given: Set divisor, bound
        divisor, bound = 10, 50
        # When: Call max_multiple
        actual = max_multiple(divisor, bound)
        # Then: max_multiple should be less than or eqaul to 50
        self.assertLessEqual(actual, 50)

    def test_should_return_180_when_given_divisor_bound_is_37_200(self):
        # Given: Set divisor, bound
        divisor, bound = 37, 200
        # When: Call max_multiple
        actual = max_multiple(divisor, bound)
        # Then: max_multiple should be eqaul to 185
        self.assertEqual(actual, 185)
