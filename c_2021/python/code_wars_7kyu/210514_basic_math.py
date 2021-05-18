import unittest
from typing import List
import re


def calculate(s: str) -> str:
    temp = 0
    formatted: List[str] = re.findall(r"\d+|plus|minus", s)
    for index, ele in enumerate(formatted):
        if ele.isnumeric():
            if index == 0:
                temp += int(ele)
                continue
            if formatted[index - 1] == "plus":
                temp += int(ele)
            else:
                temp -= int(ele)
    return str(temp)


class TestCalculate(unittest.TestCase):
    def test_calculate_with_only_plus(self):
        self.assertEqual(calculate(s="1plus2plus3plus4"), "10")

    def test_calculate_with_only_minus(self):
        self.assertEqual(calculate(s="1minus2minus3minus4"), "-8")

    def test_calculate_with_plus_and_minus_mixed(self):
        self.assertEqual(calculate(s="1plus2plus3minus4"), "2")

    def test_calculate_with_edge(self):
        self.assertEqual(calculate(s="11plus2plus3minus4"), "12")


"""
문제
1. 주어진 s를 받아서, 숫자만 뽑아서 덧셈 혹은 뺄셈을 한다.
해결
1. plus or minus가 각 숫자 사이에 있는 형태이기 때문에, 각 숫자의 직전 element를 검사하여서 덧셈 or 뺄셈을 판단하여 계산한다
조건
1. input s: str, output: -> str
절차
1. [1, plus, 2, minus, 3] 의 형태로 문자열 -> 리스트로 만든다.
2. for loop를 돌면서, 
    if plus or minus 이면, pass
    elif element가 숫자이면, 앞이 plus 인지, minus 인지 보고 result에 + or - 형태로 값을 더한다
테스트
1. plus 만 있는 경우
2. minums 만 있는 경우
3. plus, minus가 섞여있는 경우
4. 숫자가 2자리 이상 일 때,
"""
