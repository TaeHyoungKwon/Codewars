from typing import List
import unittest


def find_missing_number(sequence: str) -> int:
    sequence = sorted(sequence.split())
    if not sequence:
        return 0
    if len(sequence) == 1:
        return 1
    for front, back in zip(sequence, sequence[1:]):
        if not (front.isdigit() and back.isdigit()):
            return 1
    sequence: List[int] = list(map(int, sequence))
    if list(range(1, max(sequence) + 1)) == sequence:
        return 0

    return min(set(range(1, max(sequence) + 1)) - set(sequence))


class TestFindMissingNumber(unittest.TestCase):
    def test_find_missing_number_on_return_0(self):
        self.assertEqual(find_missing_number(sequence="1 2 3 4 5"), 0)

    def test_find_missing_number_on_return_0_with_empty_space(self):
        self.assertEqual(find_missing_number(sequence=""), 0)

    def test_find_missing_number_on_return_1(self):
        self.assertEqual(find_missing_number(sequence="2 6 4 5 3"), 1)

    def test_find_missing_number_on_return_1_with_non_digit_case_1(self):
        self.assertEqual(find_missing_number(sequence="1 2 3 4 A"), 1)

    def test_find_missing_number_on_return_1_with_non_digit_case_2(self):
        self.assertEqual(find_missing_number(sequence="_______"), 1)

    def test_find_missing_number_on_return_n(self):
        self.assertEqual(find_missing_number(sequence="1 2 3 5"), 4)