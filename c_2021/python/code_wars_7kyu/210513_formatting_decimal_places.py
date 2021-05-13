import unittest


def two_decimal_places(number: float) -> float:
    int_part, float_part = str(number).split(".")
    return float(f"{int_part}.{float_part[:2]}")
    
    
class TestTwoDecimalPlaces(unittest.TestCase):
    def test_two_decimal_places(self):
        self.assertEqual(two_decimal_places(number=10.1289767789), 10.12)


"""
문제
- two_decimal_places 함수를 통해서, 소수점 둘째자리 까지만 표현되도록 해라
해결
- formatting으로 해결
조건
- 반올림하지 말고, 물리적으로 2개를 끊어서 표현하도록 한다
절차
- 주어진 Number를 바로 f-string으로 바로 리턴한다.
"""