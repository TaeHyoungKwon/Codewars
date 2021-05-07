import unittest
from typing import List


def candies(s: List[int]) -> int:
    if len(s) <= 1:
        return -1
    max_candy_count = max(s)
    return sum(max_candy_count - other_candy_count for other_candy_count in s)


class TestCandies(unittest.TestCase):
    def test_candies(self):
        self.assertEqual(candies(s=[5, 8, 6, 4]), 9)


"""
문제
- 모든 아이들한테 같은 양의 사탕이 분배되어야 한다
- input -> s: List[int], ouput -> int
해결
- 사탕 개수가 가장 많은 것을 찾은 후, 나머지를 거 숫자에 맞춘다
조건
- 빈 값이거나, 1개이면, -1를 리턴한다
절차
1. s 리스트에서 최대값 1개를 찾는다 s.pop(max(s))
2. 루프를 돌면서, 최대값에 대한 차를 구하고 이를 list에 저장한다
3. 리스트에 저장된 값을 모두 합한다
"""
