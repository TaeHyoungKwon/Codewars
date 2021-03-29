import unittest
import string

NOT_FIRE_MSG = "That was close!"
FIRE_MSG = "Fire!"

ALPHABET = string.ascii_lowercase


def cake(candles, debris):
    if candles == 0:
        return NOT_FIRE_MSG
    result = sum(ALPHABET.index(char) + 1 if index % 2 else ord(char) for index, char in enumerate(debris))
    return FIRE_MSG if result > candles * 0.7 else NOT_FIRE_MSG


class TestCake(unittest.TestCase):
    def test_cake_on_fire(self):
        self.assertEqual(cake(candles=12, debris="jaam"), FIRE_MSG)

    def test_cake_on_fire_case_2(self):
        self.assertEqual(cake(candles=333, debris="jfmgklfhglbe"), FIRE_MSG)

    def test_cake_on_not_fire(self):
        self.assertEqual(cake(candles=900, debris="abcdef"), NOT_FIRE_MSG)

    def test_cake_on_edge(self):
        self.assertEqual(cake(candles=709, debris="yfajooerb"), FIRE_MSG)

    def test_cake_on_edge_case_2(self):
        self.assertEqual(cake(candles=0, debris="jpipe"), NOT_FIRE_MSG)
