import unittest

# TODO: 테스트케이스 1개 통과 안됨

def two_sum(numbers, target):
    for idx, ele in enumerate(numbers):
        if target - ele in numbers:
            return [idx, numbers.index(target - ele)]

    # return next([idx, numbers.index(target - ele)] for idx, ele in enumerate(numbers) if target - ele in numbers)
    # return next([idx, numbers.index(target - ele)]
    #             for idx, ele in enumerate(numbers) if target - ele in numbers)
    
    
class TestTwoSum(unittest.TestCase):
    def test_should_return_list_type(self):
        # Given: Set numbers and target
        numbers, target = [1, 2, 3], 4
        # When: Call two_sum
        actual = two_sum(numbers, target)
        # Then: two_sum should return type is tuple
        self.assertIsInstance(actual, list)

    def test_success_case_one(self):
        # Given: Set numbers and target
        numbers, target = [1, 2, 3], 4
        # When: Call two_sum
        actual = two_sum(numbers, target)
        # Then: two_sum should return type is tuple
        self.assertEqual(actual, [0, 2])

    def test_success_case_two(self):
        # Given: Set numbers and target
        numbers, target = [1234, 5678, 9012], 14690
        # When: Call two_sum
        actual = two_sum(numbers, target)
        # Then: two_sum should return type is tuple
        self.assertEqual(actual, [1, 2])

    def test_success_case_three(self):
        # Given: Set numbers and target
        numbers, target = [2, 2, 3], 4
        # When: Call two_sum
        actual = two_sum(numbers, target)
        # Then: two_sum should return type is tuple
        self.assertEqual(actual, [0, 1])