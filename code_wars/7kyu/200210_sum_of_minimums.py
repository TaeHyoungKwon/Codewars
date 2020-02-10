import unittest


def sum_of_minimums(numbers):
    return sum(min(num_list) for num_list in numbers)
    
    
class TestSumOfMinimums(unittest.TestCase):
    def test_should_return_sum_of_minimum_values_about_each_lists(self):
        numbers = [[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]
        actual = sum_of_minimums(numbers)
        self.assertEqual(actual, 9)
