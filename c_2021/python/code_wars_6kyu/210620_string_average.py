import unittest

STRING_NUM_MAP = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def average_string(s: str) -> str:
    if not s:
        return "n/a"

    converted = []
    for ele in s.split():
        if STRING_NUM_MAP.get(ele) is None:
            return "n/a"
        converted.append(STRING_NUM_MAP[ele])
    return next(k for k, v in STRING_NUM_MAP.items() if v == sum(converted) // len(converted))


class TestAverageString(unittest.TestCase):
    def test_average_string(self):
        self.assertEqual(average_string(s="zero nine five two"), "four")

    def test_average_string_with_invalid_input_on_empty_string(self):
        self.assertEqual(average_string(s=""), "n/a")

    def test_average_string_with_invalid_input(self):
        self.assertEqual(average_string(s="ten"), "n/a")


"""
문제
* 주어진 s를 받아서, 값의 평균을 구한다
해결
* 0~9에 매핑하는 문자열 dict를 만들어서, 문제 해결
조건
input -> s: str, output -> str

1. 빈값이거나, 0~9 범위를 벗어나거나, 엉뚱한 단어가 들어오면, "n/a" 를 리턴한다
절차
1. 0~9에 매핑하는 문자열: 숫자 값 dict를 만든다
2. s.split() 하고, 루프를 돌린다
3. 각 값에 대한 평균을 구하고, 문자열 형태로 리턴한다
테스트
1. 정상 해피패스 케이스
2. "n/a"를 리턴하는 경우
"""