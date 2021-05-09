import re
from typing import List, Tuple


REPLACEMENTS: List[Tuple[str, str]] = [
    (r"probably", "prolly"),
    (r"i am", "i'm"),
    (r"instagram", "insta"),
    (r"do not", "don't"),
    (r"going to", "gonna"),
    (r"combination", "combo"),
]


def gym_slang(phrase):
    for element in REPLACEMENTS:
        phrase = re.sub(element[0], r"\1" + element[1], phrase)
    return phrase


"""
문제
- 주어진 조건에 대한 특정 문자열을 regex를 이용해 변경해라
- input: phrase: str, output -> str
해결
- 제시된 조건들에 대한 문자열을 특정 문자열로 변경한다(re.sub)
조건
1. case-sensitive
2. instagram -> insta , Instagram -> Insta로 변경해야한다.
절차
1. 주어진 문자열에서, re.sub를 이용해서 특정 문자열로 변경되도록 한다.
2. 대소문자도 구분해서 처리해줘야한다
"""
