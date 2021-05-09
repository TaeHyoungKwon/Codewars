import string
from typing import List, Tuple, Generator
import unittest

ALL_LOWER_ALPHABETS = string.ascii_lowercase


def rank(first_name_with_comma: str, weight: List[int], rank: int) -> str:
    if not first_name_with_comma:
        return "No participants"
    if rank > len(weight):
        return "Not enough participants"

    first_names: List[str] = first_name_with_comma.split(",")
    winning_numbers: Generator = get_winning_numbers(first_names, weight)
    sorted_winning_numbers = sorted(winning_numbers, key=lambda x: (-x[1], x[0]))

    return sorted_winning_numbers[rank - 1][0]


def get_winning_numbers(first_names: List[str], weight: List[int]) -> Generator:
    for index, first_name in enumerate(first_names):
        alphabet_index_sum = 0
        length = len(first_name)
        for letter in first_name:
            alphabet_index_sum += ALL_LOWER_ALPHABETS.index(letter.lower()) + 1
        yield (first_name, weight[index] * (alphabet_index_sum + length))


class TestRank(unittest.TestCase):
    def test_rank_with_no_participants(self):
        self.assertEqual(rank(first_name_with_comma="", weight=[1, 2, 3], rank=1), "No participants")

    def test_rank_with_not_enough_participants(self):
        self.assertEqual(
            rank(
                first_name_with_comma="Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin",
                weight=[4, 2, 1, 4, 3, 1, 2],
                rank=8,
            ),
            "Not enough participants",
        )

    def test_rank(self):
        self.assertEqual(rank(first_name_with_comma="Lagon,Lily", weight=[1, 5], rank=2), "Lagon")


"""
문제
- 경품 추첨 문제이다. 이름 길이와 가중치에 따라서 계산하고, rank에 해당하는 당첨자로 결정
해결
- 조건에 맞춰서 winning number를 계산하고, rank에 맞는 당첨자를 리턴
조건
- Params: first_names_with_comma: str, weight: List[int], rank: int / output -> str
- winning number 기준 내림차순 정렬한다.
- 2명의 사람이 점수가 같으면 알파벳 순서대로 정렬한다
- first_names_with_comma가 empty이면, No participants 를 리턴한다
- 참가자 보다, rank의 숫자가 더 크면 Not enough participants 를 리턴한다
절차

0. first_names, first_name + rank를 통한 예외처리
1. first_names string을 , 기준으로 list로 묶는다
2. 루프를 돌면서 각 first_name의 길이 + 알파벳 index의 합을 구한 후, weight를 곱한 값을 first_name: winning_number 형태의 tuple을 만든다
3. 2번의 결과로 만들어진 튜플 리스트를 winning number 기준 내림 차순, first_name 기준 오름차순으로 정렬한다.
4. rank에 맞는 index에 해당하는 first_name을 리턴한다.

테스트
1. 예외 처리 - No participants
2. 예외 처리 - Not enough participants
3. 정상 케이스
"""
