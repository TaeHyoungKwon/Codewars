import unittest
from typing import List


def array_leaders(numbers: List[int]) -> List[int]:
    return [ele for index, ele in enumerate(numbers) if ele > sum(numbers[index + 1:])]


class TestArrayLeaders(unittest.TestCase):
    def test_array_leaders_with_positive(self):
        self.assertEqual(array_leaders(numbers=[16, 17, 4, 3, 5, 2]), [17, 5, 2])

    def test_array_leaders_with_negative(self):
        self.assertEqual(array_leaders(numbers=[-1, -29, -26, -2]), [-1])

    def test_array_leaders_with_mixed(self):
        self.assertEqual(array_leaders(numbers=[0, -1, -29, 3, 2]), [0, -1, 3, 2])



"""
문제
- leader element의 리스트를 뽑아라
해결
- 루프를 돌면서, 이하 elements의 합을 구하고, 현재 수와 비교해서, 현재수가 더 크면 result list에 넣는다
조건
input -> numbers: List[int], output -> List[int]
절차
- 루프를 돌면서, 이하 elements의 합을 구하고, 현재 수와 비교해서, 현재수가 더 크면 result list에 넣는다
테스트
1. 양수
2. 음수
3. 양수 + 음수
"""