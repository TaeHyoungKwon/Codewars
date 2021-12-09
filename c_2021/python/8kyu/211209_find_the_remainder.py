import unittest


def remainder(a, b):
    try:
        return a % b if a > b else b % a
    except ZeroDivisionError:
        return None
    
    
class TestRemainder(unittest.TestCase):
    def test_remainder_on_a_is_more_than_b(self):
        self.assertEqual(remainder(17, 5), 2)

    def test_remainder_on_b_is_more_than_a(self):
        self.assertEqual(remainder(5, 17), 2)

    def test_remainder_with_zero(self):
        self.assertIsNone(remainder(1, 0))
        self.assertIsNone(remainder(0, 1))

    def test_remain_with_negative(self):
        self.assertEqual(remainder(-1, 0), 0)

"""
테스트
1. a > b -> a % b 의 결과를 그대로 리턴
2. b > a -> b % a 로 변경해서 결과를 리턴
3. a, b 중 0이 있고, 나머지가 양수일 때 -> None을 리턴
3. a, b 중 0이 있고, 나머지가 음수일 때 -> 0으로 리턴
"""