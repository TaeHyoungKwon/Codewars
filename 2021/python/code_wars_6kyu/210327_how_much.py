from typing import List
import unittest

CAR_PRICE = 7
BOAT_PRICE = 9


def howmuch(m: int, n: int) -> List[List[str]]:
    def f():
        for x in range(min(m, n), max(m, n) + 1):
            b, r1 = divmod(x - 2, CAR_PRICE)
            c, r2 = divmod(x - 1, BOAT_PRICE)
            if r1 == r2 == 0:
                yield [f"M: {x}", f"B: {b}", f"C: {c}"]

    return list(f())


class TestHowMuch(unittest.TestCase):
    def test_howmuch(self):
        self.assertEqual(howmuch(m=1, n=100), [["M: 37", "B: 5", "C: 4"], ["M: 100", "B: 14", "C: 11"]])
