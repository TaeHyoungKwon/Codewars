import math
import unittest


def find_missing(sequence):
    def get_last_by_diff(diff, last_value):
        if diff < 0:
            last_value -= 1
        else:
            last_value += 1
        return last_value

    first, last = sequence[0], sequence[-1]
    diff = (last - first) // len(sequence)

    last = get_last_by_diff(diff, last)
    return sum(range(first, last, diff)) - sum(sequence)
    
    
class TestFindMissing(unittest.TestCase):
    def test_find_missing(self):
        sequence = [1, 2, 3, 4, 6, 7, 8, 9]
        actual = find_missing(sequence)
        self.assertEqual(actual, 5)

    def test_find_missing_second_case(self):
        sequence = [1, 3, 4, 5, 6, 7, 8, 9]
        actual = find_missing(sequence)
        self.assertEqual(actual, 2)

    def test_find_missing_third_case(self):
        sequence = [1, 3, 5, 9, 11]
        actual = find_missing(sequence)
        self.assertEqual(actual, 7)

    def test_find_missing_with_minus(self):
        sequence = [0, -6, -9, -12, -15, -18, -21, -24, -27]
        actual = find_missing(sequence)
        self.assertEqual(actual, -3)

    def test_find_missing_with_minus_and_plust_mixed(self):
        sequence = [-1, 2, 5, 8, 11, 14, 20, 23, 26]
        actual = find_missing(sequence)
        self.assertEqual(actual, 17)

    def test_find_missing_with_minus_2(self):
        sequence = [-5, -11, -14, -17, -20, -23, -26, -29, -32]
        actual = find_missing(sequence)
        self.assertEqual(actual, -8)


