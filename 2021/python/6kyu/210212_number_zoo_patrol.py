# from itertools import count
import unittest


def find_missing_number(numbers):
    if not numbers:
        return 1
    result = sum(range(1, max(numbers) + 1)) - sum(numbers)
    if result == 0:
        result = max(numbers) + 1
    return result


# def find_missing_number(numbers):
#     n = len(numbers) + 1
#     return sum(range(1, n + 1)) - sum(numbers)

# def find_missing_number(numbers):
#     numbers_set = set(numbers)
#     return next(i for i in count(1) if i not in numbers_set)


class TestFindMissingNumber(unittest.TestCase):
    def test_find_missing_number(self):
        self.assertEqual(find_missing_number(numbers=[2, 3, 4]), 1)

    def test_find_missing_number_with_edge_case(self):
        self.assertEqual(find_missing_number(numbers=[1, 2, 3]), 4)

    def test_find_missing_number_with_empty_list(self):
        self.assertEqual(find_missing_number(numbers=[]), 1)
