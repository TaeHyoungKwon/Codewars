from typing import List
import unittest


def squares(x: int, n: int) -> List[int]:
    return [x ** 2 ** ele for ele in range(n)]


class TestSquares(unittest.TestCase):
    def test_squares_n_is_0(self):
        self.assertEqual(squares(x=2, n=0), [])

    def test_squares_n_is_negative_4(self):
        self.assertEqual(squares(x=2, n=-4), [])

    def test_squares(self):
        self.assertEqual(squares(x=2, n=5), [2, 4, 16, 256, 65536])
