import unittest


def solution(nums):
    return sorted(nums) if nums else []
    
    
class TestSortNumbers(unittest.TestCase):
    def test_should_return_empty_list_when_nums_is_none(self):
        nums = None
        actual = solution(nums)
        self.assertEqual(actual, [])

    def test_should_return_sorted_list_when_num_is_common_list(self):
        nums = [1, 2, 10, 5]
        actual = solution(nums)
        self.assertEqual(actual, [1, 2, 5, 10])
        