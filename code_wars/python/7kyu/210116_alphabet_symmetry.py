import string
import unittest

POSITIONS = {alphabet: index for index, alphabet in enumerate(string.ascii_lowercase, 1)}


def solve(arr_):
    return [sum(index == POSITIONS[alphabet] for index, alphabet in enumerate(word.lower(), 1)) for word in arr_]


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(arr_=["abode", "ABc", "xyzD"]), [4, 3, 1])

    def test_solve_case_2(self):
        self.assertEqual(solve(arr_=["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"]), [6, 5, 7])
