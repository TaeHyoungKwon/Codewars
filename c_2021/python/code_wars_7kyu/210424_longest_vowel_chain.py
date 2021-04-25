import unittest

VOWEL = {"a", "e", "i", "o", "u"}


# def solve(s: str) -> int:
#     return len(max("".join(char if char in VOWEL else " " for char in s).split(), key=len))

def solve(s: str) -> int:
    return max(map(len, "".join(char if char in VOWEL else " " for char in s).split()))


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(s="codewarriors"), 2)
