import unittest
import string

LOWER_CASE_ALPHABET = string.ascii_letters


def solve(st):
    return "".join(sorted(st)) in LOWER_CASE_ALPHABET


class TestSolve(unittest.TestCase):
    def test_solve_on_duplicated_char(self):
        self.assertFalse(solve(st="aabc"))

    def test_solve_on_no_duplicated_char_with_consecutive_alphabet(self):
        self.assertTrue(solve(st="abc"))


"""
테스트
1. string 중에 겹치는게 문자가 있으면 False 이다
2. 겹치는게 없는데, consecutive 하면 True
"""