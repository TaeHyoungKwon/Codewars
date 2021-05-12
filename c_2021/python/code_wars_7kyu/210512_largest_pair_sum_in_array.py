import unittest
from typing import List


def largest_pair_sum(numbers: List[int]) -> int:
    sorted_ = sorted(numbers, reverse=True)
    return sorted_[0] + sorted_[1]


class TestLargestPairSum(unittest.TestCase):
    def test_largest_pair_sum(self):
        self.assertEqual(largest_pair_sum(numbers=[10, 14, 2, 23, 19]), 42)




"""
문제
- 가장 큰 두 수를 골라서 더한 값을 리턴한다
해결
- 정렬한 후에 가장 큰 두값을 더해서 리턴한다
조건
- input: numbers: List[int], output: int
절차
1. numbers list를 내림차순 정렬한다
2. 내림차순 정렬한 리스트에서 앞 2개의 element를 뽑아 낸다
3. 더해서 리턴한다
"""