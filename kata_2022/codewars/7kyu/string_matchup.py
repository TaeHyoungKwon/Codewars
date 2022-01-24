from typing import List

import pytest


def solve(a: List[str], b: List[str]) -> List[int]:
    return [a.count(ele) for ele in b]


class TestSolve:
    @pytest.mark.parametrize(
        "a_values, b_values, expected",
        (
            (["abc", "abc", "xyz", "abcd", "cde"], ["abc", "cde", "uap"], [2, 1, 0]),
            (["abc", "xyz", "abc", "xyz", "cde"], ["abc", "cde", "xyz"], [2, 1, 2]),
        ),
    )
    def test_solve(self, a_values, b_values, expected):
        assert solve(a=a_values, b=b_values) == expected


"""
문제
 - a, b가 주어질 때, b에 있는 각 요소가 a에 몇번 나오는지에 count를 리스트로 리턴해라
해결
 - 아래 절차대로 문제를 해결하자
절차
Workflow
1. b를 루프를 돈다
2. 돌면서, a 리스트에 b 요소가 몇개 존재하는지 개수를 센다
3. 각 index 대로 list에 센 갯수를 리턴한다
테스트
1. 성공
 - common case  아래 케이스 중 1개를 가져와서 작성 
"""
