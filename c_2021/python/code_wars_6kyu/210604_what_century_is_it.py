import unittest

ORDINAL_NUMBER_MAP = {"1": "st", "2": "nd", "3": "rd"}


def what_century(year: str):
    ordinal_expression = "th"
    front_part = year[:2]
    back_part = year[2:]
    century = str(int(front_part)) if back_part == "00" else str(int(front_part) + 1)
    century_with_padding = century.rjust(2, "0")
    if century_with_padding[1] in ORDINAL_NUMBER_MAP.keys() and not (10 <= int(century) <= 19):
        ordinal_expression = ORDINAL_NUMBER_MAP[century_with_padding[1]]
    return f"{century}{ordinal_expression}"


class TestWhatCentury(unittest.TestCase):
    def test_century_with_year_is_0111(self):
        self.assertEqual(what_century(year="0111"), "2nd")

    def test_century_with_year_is_0011(self):
        self.assertEqual(what_century(year="0011"), "1st")

    def test_century_with_year_is_0001(self):
        self.assertEqual(what_century(year="0001"), "1st")

    def test_century_with_year_is_2011(self):
        self.assertEqual(what_century(year="2011"), "21st")

    def test_century_with_year_is_1011(self):
        self.assertEqual(what_century(year="1011"), "11th")

    def test_century_with_year_is_2000(self):
        self.assertEqual(what_century(year="2000"), "20th")


"""
문제
- year 값을 받았을 때, 알맞은 `세기` 를 리턴하도록 해라
해결
- 각 year 일 때, `세기` 표기를 어떻게 하는지 로직을 도출한 이후에 뒤 서수 표현은 1, 2, 3 만 예외로 처리해준다
조건
- input -> year: str, output -> str
절차
1. year 앞 두자리를 떼어온다
2. 1번의 결과를 int로 바꿔서 1을 더한다
3. 2번의 결과를 str로 변경하고, 첫번째 index의 값이 1, 2, 3 이면, 매핑 테이블의 서수 표현을 써주고, 그 이외는 th를 붙여준다
4. 숫자 2자리와 서수 표현을 붙여서 리턴한다
테스트
1. 0001 -> 1세기
2. 0011 -> 1세기
3. 0111 -> 2세기
4. 1111 -> 12세기
"""
