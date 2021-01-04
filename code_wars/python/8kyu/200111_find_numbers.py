import unittest


def divisible_by(numbers, divisor):
    return [ele for ele in numbers if ele % divisor == 0]
    
    
class TestDivisibleBy(unittest.TestCase):
    def test_should_return_2_and_4_and_6_when_given_numbers_1_to_6(self):
        # Given: Set numbers and divisor
        numbers = [1, 2, 3, 4, 5, 6]
        divisor = 2
        # When: Call divisible_by
        result = divisible_by(numbers, divisor)
        # Then: test should return [2, 4, 6]
        self.assertEqual(result, [2, 4, 6])

    def test_should_return_3_and_6_and_6_when_given_numbers_1_to_6(self):
        # Given: Set numbers and divisor
        numbers = [1, 2, 3, 4, 5, 6]
        divisor = 3
        # When: Call divisible_by
        result = divisible_by(numbers, divisor)
        # Then: test should return [3, 6]
        self.assertEqual(result, [3, 6])
