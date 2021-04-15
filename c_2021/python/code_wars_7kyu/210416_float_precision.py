import unittest


def solution(n: float) -> float:
    return round(n, 2)


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(n=2.34), 2.34)
