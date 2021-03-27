import unittest


def sum_cubes(n: int) -> int:
    return sum(i ** 3 for i in range(1, n + 1))


class TestSumCubes(unittest.TestCase):
    def test_sum_cubes(self):
        self.assertEqual(sum_cubes(n=3), 36)
