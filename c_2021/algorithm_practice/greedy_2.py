# 숫자 카드 게임 p.92

import unittest
from typing import List


def number_card_game(l: List[List[int]]) -> int:
    return max(min(row) for row in l)


class TestNumberCardGame(unittest.TestCase):
    def test_number_card_game(self):
        self.assertEqual(number_card_game(l=[[3, 1, 2], [4, 1, 4], [2, 2, 2]]), 2)
