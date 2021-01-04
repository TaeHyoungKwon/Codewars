import unittest


def max_gap(numbers):
    index = len(numbers) - 1
    sorted_numbers = sorted(numbers)
    max_val = 0
    for _ in sorted_numbers[::-1]:
        diff = sorted_numbers[index] - sorted_numbers[index - 1]
        if index == 0:
            return max_val
        if diff > max_val:
            max_val = diff
        index -= 1
    return max_val
    
    
class TestMaxGap(unittest.TestCase):
    def test_max_gap(self):
        numbers = [13, 10, 2, 9, 5]
        actual = absent_vowel(numbers)
        self.assertEqual(actual, 4)

    def test_max_gap_case_two(self):
        numbers = [1, 1, 1]
        actual = absent_vowel(numbers)
        self.assertEqual(actual, 0)

    def test_max_gap_case_three(self):
        numbers = [12, -5, -7, 0, 290]
        actual = absent_vowel(numbers)
        self.assertEqual(actual, 278)
        