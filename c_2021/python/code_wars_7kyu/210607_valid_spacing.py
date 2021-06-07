import unittest


def valid_spacing(s: str) -> bool:
    if not s:
        return True
    return s[0] != " " and s[-1] != " " and len(s.split()) == s.count(" ") + 1


class TestValidSpacing(unittest.TestCase):
    def test_valid_spacing_with_true(self):
        self.assertTrue(valid_spacing(s="codewars"))

    def test_valid_spacing_with_true_case_2(self):
        self.assertTrue(valid_spacing(s="c o d e w a r s"))

    def test_valid_spacing_with_true_case_3(self):
        self.assertTrue(valid_spacing(s=""))

    def test_valid_spacing_with_false(self):
        self.assertFalse(valid_spacing(s=" Hello World"))

    def test_valid_spacing_with_false_case_2(self):
        self.assertFalse(valid_spacing(s="codewars "))

    def test_valid_spacing_with_false_case_3(self):
        self.assertFalse(valid_spacing(s="cod  ewars"))


"""
문제
- 주어진 s가 valid하 spacing 인지 판단해라
해결
- 조건에 맞게 검사해서 모두 통과하면 True를 리턴한다
조건
1. 중간에만 공백이 있어야 한다
2. 아예 공백이 없어도 된다
절차
1. True가 되는 조건을 명시해주고, 모두 일치하면 True 하나라도 안맞으면 False를 리턴한다
테스트
1. True 일 때,
2. False 일 때,
"""
