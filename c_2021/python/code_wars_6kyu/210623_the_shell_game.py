import unittest
from typing import List, Tuple


def find_the_ball(start: int, swaps: List[Tuple[int]]) -> int:
    last_position = start
    for swap_history in swaps:
        first, second = swap_history
        if last_position in swap_history:
            if last_position == first:
                last_position = second
            else:
                last_position = first
    return last_position


class TestFindTheBall(unittest.TestCase):
    def test_find_the_ball_on_swaps_is_empty(self):
        self.assertEqual(find_the_ball(start=5, swaps=[]), 5)

    def test_find_the_ball(self):
        self.assertEqual(find_the_ball(start=0, swaps=[(0, 1), (2, 1), (0, 1)]), 2)


"""
문제
* start, swaps를 받아서, swaps 히스토리를 보고, 최종 ball의 위치를 찾아라
해결
* last position을 기준으로 swap이 있었는지 확인하고, swap이 있으면, last position을 업데이트 그렇지 않으면 업데이트 하지 않는 방식
조건
1. input -> start: int, swaps: List[Tuple[int]], output -> int
2. cup 개수는 최소 2개이다
절차
1. last_position을 start로 세팅한다 
2. swaps를 루프를 돌린다
3. last_position이 swap ele의 값 중에 존재하면, 나머지 값을 last_position으로 업데이트 한다
4. last_position을 리턴한다
테스트
1. swaps가 빈 값일 때, 주어진 start를 리턴
2. swaps가 빈 값이 아닐 때,
"""