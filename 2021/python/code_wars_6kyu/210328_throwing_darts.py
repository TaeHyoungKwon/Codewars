from enum import IntEnum
from typing import List, Union
import unittest


class Score(IntEnum):
    TEN_POINT = 10
    FIVE_POINT = 5
    ZERO_POINT = 0


def score_throws(radii: List[Union[int, float]]) -> int:
    if not radii:
        return 0
    score = _get_score_by_radii(radii)
    return _get_score_with_bonus(radii, score)


def _get_score_with_bonus(radii, score):
    has_bonus_score = score == len(radii) * 10
    if has_bonus_score:
        score += 100
    return score


def _get_score_by_radii(radii):
    score = 0
    for radius in radii:
        if 0 <= radius < 5:
            score += Score.TEN_POINT
        elif 5 <= radius <= 10:
            score += Score.FIVE_POINT
        else:
            score += Score.ZERO_POINT
    return score


class TestScoreThrows(unittest.TestCase):
    def test_score_throws_with_empty_list(self):
        self.assertEqual(score_throws(radii=[]), 0)

    def test_score_throws_with_no_bonus(self):
        self.assertEqual(score_throws(radii=[1, 5, 11]), 15)

    def test_score_throws_with_bonus(self):
        self.assertEqual(score_throws(radii=[1, 2, 3, 4]), 140)

    def test_score_throws_with_float(self):
        self.assertEqual(score_throws(radii=[0, 5, 10, 10.5, 4.5]), 30)
