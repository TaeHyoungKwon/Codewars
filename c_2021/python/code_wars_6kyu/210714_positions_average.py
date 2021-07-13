import unittest
from itertools import combinations
from typing import List


def pos_average(s: str):
    element_list: List[str] = s.split(", ")
    n = len(element_list)
    common_count = sum(c == d for a, b in combinations(element_list, 2) for c, d in zip(a, b))
    return round(common_count / ((n * (n - 1) / 2) * len(element_list[0])) * 100, 10)


class TestPosAverage(unittest.TestCase):
    def test_post_average(self):
        self.assertEqual(
            pos_average(s="466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"),
            26.6666666667,
        )


"""
주어진 s에 대해서, pos_average 를 구하여라

각 숫자로 뭉친 문자열 각각을 비교 해서 같은 index에 같은 값이 나올 확률을 구해라


1. 조합으로 2개씩 묶는다
2. 각 조합을 루프를 돌린다
    1. 공통부분 개수를 찾는 함수를 돌린다
    2. 루프 돌 때마다 더한다
    3. 최종적으로 공통으로 나온 개수 / 검사한 각 문자열의 길이 를하고, 100을 곱한다
"""