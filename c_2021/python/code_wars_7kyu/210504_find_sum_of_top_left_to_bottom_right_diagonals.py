import unittest
from typing import List


def diagonal_sum(array: List[List[int]]) -> int:
    return sum(element[index] for index, element in enumerate(array))


class TestDiagonalSum(unittest.TestCase):
    def test_diagonal_sum(self):
        self.assertEqual(diagonal_sum(array=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 15)



"""
문제
- array가 주어졌을 때, 각 행 index에 해당하는 값들의 합을 구하여라
해결
- array의 길이를 잰 이후, 그 길이만큼 루프를 돌아서, index에 해당하는 값을 뽑아내서, temp에 저장한 후,
그 값들을 더한다.
조건
- input - array: List[List[int]], output: int
절차
1. array를 루프를 돌린다.
2. 각행의 index에 해당하는 값들을 뽑아낸다.
3. 뽑아낸 값들을 temp 리스트에 저아한다.
4. temp list에 저장된 값들을 합한다.
"""