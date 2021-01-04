import unittest


def find_smallest(numbers, to_return):
    return min(numbers) if to_return == 'value' else numbers.index(min(numbers))
    
    
class TestFindSmallest(unittest.TestCase):
    def test_find_smallest_should_return_min_value_in_distinct_numbers(self):
        # Given: Set numbers and to_return
        numbers = [5, 4, 3, 2, 1]
        to_return = 'value'

        # When: Call find_smallest(numbers, to_return)
        actual = find_smallest(numbers, to_return)

        # Then: actual should return 1
        self.assertEqual(actual, 1)

    def test_find_smallest_should_return_index_of_min_value_in_distinct_numbers(self):
        # Given: Set numbers and to_return
        numbers = [5, 4, 3, 2, 1]
        to_return = 'index'

        # When: Call find_smallest(numbers, to_return)
        actual = find_smallest(numbers, to_return)

        # Then: actual should return 1
        self.assertEqual(actual, 4)

    def test_find_smallest_should_return_min_value_in_duplicated_numbers(self):
        # Given: Set numbers and to_return
        numbers = [1, 1, 0, 0, 1, 1]
        to_return = 'value'

        # When: Call find_smallest(numbers, to_return)
        actual = find_smallest(numbers, to_return)

        # Then: actual should return 1
        self.assertEqual(actual, 0)

    def test_find_smallest_should_return_index_of_min_value_in_duplicated_numbers(self):
        # Given: Set numbers and to_return
        numbers = [1, 1, 0, 0, 1, 1]
        to_return = 'index'

        # When: Call find_smallest(numbers, to_return)
        actual = find_smallest(numbers, to_return)

        # Then: actual should return 1
        self.assertEqual(actual, 2)