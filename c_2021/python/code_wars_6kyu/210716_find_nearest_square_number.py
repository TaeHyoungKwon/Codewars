import math
import unittest
from itertools import count


def _is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2


def nearest_sq(n):
    return next(i for i in count(n - 1) if _is_square(i)) if n != 1 else 1


class TestNearestSq(unittest.TestCase):
    def test_nearest_sq(self):
        self.assertEqual(nearest_sq(n=111), 121)
        self.assertEqual(nearest_sq(n=2), 1)
        self.assertEqual(nearest_sq(n=1), 1)
