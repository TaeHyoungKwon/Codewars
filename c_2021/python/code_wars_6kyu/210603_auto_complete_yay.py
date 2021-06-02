import re
import unittest
from typing import List

MAX_VALUE = 5


def autocomplete(input_: str, dictionary: List[str]) -> List[str]:
    cleaned_input = re.sub(r"[^a-zA-Z]", "", input_)
    return [word for word in dictionary if word.lower().startswith(cleaned_input)][:MAX_VALUE]


class TestAutoComplete(unittest.TestCase):
    def test_autocomplete_with_no_matching(self):
        self.assertEqual(autocomplete(input_="ai", dictionary=["bbq"]), [])

    def test_autocomplete_with_matching_under_5(self):
        self.assertEqual(
            autocomplete(
                input_="ai",
                dictionary=["abnormal", "arm-wrestling", "absolute", "airplane", "airport", "amazing", "apple", "ball"],
            ),
            ["airplane", "airport"],
        )

    def test_autocomplete_with_matching_over_5(self):
        self.assertEqual(
            autocomplete(
                input_="a",
                dictionary=["abnormal", "arm-wrestling", "absolute", "airplane", "airport", "amazing", "apple", "ball"],
            ),
            ["abnormal", "arm-wrestling", "absolute", "airplane", "airport"],
        )

    def test_autocomplete_with_case_insensitive(self):
        self.assertEqual(
            autocomplete(
                input_="ai",
                dictionary=["abnormal", "arm-wrestling", "absolute", "Airplane", "Airport", "amazing", "apple", "ball"],
            ),
            ["Airplane", "Airport"],
        )

    def test_autocomplete_with_input_is_special_char(self):
        self.assertEqual(
            autocomplete(
                input_="ai_",
                dictionary=["abnormal", "arm-wrestling", "absolute", "Airplane", "Airport", "amazing", "apple", "ball"],
            ),
            ["Airplane", "Airport"],
        )


"""
문제
- 자동완성 함수를 완성 시켜라

해결
- startwith를 적절히 사용하여서 필터링을 한다

조건
input -> input_: str, dictionary: List[str] / output -> List[str]

1. 매칭되는 것이 5개 이상 있다면, 처음 5개로 제한
2. 매칭되는 것이 없으면 빈 list를 리턴
3. 기존 순서를 유지한채로 리턴
4. case insensitive 하다 -> ai 일 때, Ai 도 걸러져야함

절차
1. dictionary 를 루프를 돌린다
2. 각 element.lower()가 input_으로 시작하는지 확인한다
3. input_으로 시작하면, 리스트에 넣는다 , 그렇지 않으면 패스 한다
4. 리스트를 리턴한다

테스트
1. 매칭되는 것이 1개도 없을 때,
2. 매칭되는 것이 5개 초과로 있을 때,
3. 매칭되는 것이 5개 이하로 있을 때,
4. case insensitive
5. input_에 알파벳이 아닌 문자가 있을 때 무시
"""
