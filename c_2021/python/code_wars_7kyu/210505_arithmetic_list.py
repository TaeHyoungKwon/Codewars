from typing import List
import unittest


def seqlist(first: int, c: int, l: int) -> List[int]:
    def generate_seqlist(first):
        for _ in range(l):
            yield first
            first += c
    return list(generate_seqlist(first))




class TestSeqlist(unittest.TestCase):
    def test_seq_list(self):
        self.assertEqual(
            seqlist(first=0, c=1, l=20), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        )

    def test_seq_list_with_edge_case(self):
        self.assertEqual(
            seqlist(first=100, c=-5, l=20),
            [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
        )


"""
문제
- 주어진 arg에 따라 시작/간격/개수 조건을 맞춰서 sequence list를 만든다
해결
- 조건에 맞게 append 한다
조건
- input -> first: int, c: int, l: int, output -> List[int]
절차
1. first 부터 시작해서, c 간격으로 l 만큼 루프를돈다
2. 루프를 돌면서 list에 element를 넣는다
"""
