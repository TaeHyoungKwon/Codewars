import unittest

MAX_MINUTES = 60
MAX_SECONDS = 60


def solution(hour):
    return sum(
        True
        for h in range(hour + 1)
        for m in range(MAX_MINUTES)
        for s in range(MAX_SECONDS)
        if "3" in "".join(map(str, [h, m, s]))
    )


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(hour=5), 11475)
