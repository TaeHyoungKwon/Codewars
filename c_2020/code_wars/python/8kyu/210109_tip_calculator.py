from enum import Enum
import math
import unittest

"""
문제: amount와 서비스 기준으로 팁을 얼마나 줘야하는지 계산
조건:    
    1. Terrible: tip 0% / Good: tip 10% / Great: tip 15% / Excellent: tip 20% 에 따라서 tip 퍼센트를 곱해서 return
    2. case insentitive
    3. 만약 없을 시, "Rating not recognised" 리턴
    4. 소수점 일 때는 round up
"""

NOT_RECOGNISED = "Rating not recognised"


class TIP(Enum):
    TERRIBLE = 0
    POOR = 0.05
    GOOD = 0.1
    GREAT = 0.15
    EXCELLENT = 0.2

    @classmethod
    def get_tip(cls, amount, rating):
        try:
            origin = amount * cls[rating.upper()].value
            return math.ceil(origin) if origin > 1 else origin
        except KeyError:
            return NOT_RECOGNISED


def calculate_tip(amount, rating):
    return TIP.get_tip(amount, rating)


class TestCalculateTip(unittest.TestCase):
    def test_calculate_tip_with_not_matching(self):
        self.assertEqual(calculate_tip(20, "great!"), "Rating not recognised")

    def test_calculate_tip_with_rating_is_terrible(self):
        self.assertEqual(calculate_tip(10, "terrible"), 0)

    def test_calculate_tip_with_rating_is_good(self):
        self.assertEqual(calculate_tip(10, "good"), 1)

    def test_calculate_tip_with_rating_is_excellent(self):
        self.assertEqual(calculate_tip(10, "excellent"), 2)

    def test_calculate_tip_with_rating_is_poor(self):
        self.assertEqual(calculate_tip(10, "poor"), 0.5)

    def test_calculate_tip_with_rating_is_great(self):
        self.assertEqual(calculate_tip(10, "great"), 2)

    def test_calculate_tip_with_case_in_sensitive(self):
        self.assertEqual(calculate_tip(10, "Great"), 2)
