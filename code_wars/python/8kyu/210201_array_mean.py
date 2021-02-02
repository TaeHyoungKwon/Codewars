import unittest


def find_average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)


class TestFindAverage(unittest.TestCase):
    def test_find_average(self):
        self.assertEqual(find_average(nums=[1, 3, 5, 7]), 4)

    def test_find_average_with_return_value_is_float(self):
        self.assertEqual(find_average(nums=[5, 7, 3, 7]), 5.5)
