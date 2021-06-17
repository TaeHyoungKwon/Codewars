import unittest
from typing import List, Union


def bingo(ticket: List[List[Union[str, int]]], win: int) -> str:
    return "Winner!" if sum(chr(ascii_code) in string for string, ascii_code in ticket) >= win else "Loser!"
    
    
class TestBingo(unittest.TestCase):
    def test_bingo_with_winner(self):
        self.assertEqual(bingo(ticket=[['ABC', 65], ['HGR', 74], ['BYHT', 74]], win=1), "Winner!")

    def test_bingo_with_loser(self):
        self.assertEqual(bingo(ticket=[['ABC', 65], ['HGR', 74], ['BYHT', 74]], win=2), "Loser!")


"""
문제
* 로또를 얼만큼 맞췄는지에 대해서 계산해서 리턴한다
해결
* 2차원 배열인 티켓 내부의 eleemtn의 아스키 코드와 문자가 일치한지를 확인하고, 그 개수를 주어진 win과 비교해서 Loser or Winner 를 리턴한다
조건
* input -> ticket: List[List[str, int]], win: int / output -> str
절차
1. ticket을 루프를 돈다
2. 루프 내에서, ticket의 두번째 element(아스키 코드)에 해당하는 문자열이 있는지 확인한다
3. 있으면, True 없으면 False로 temp 리스트에 추가한다.
4. 위 리스트의 True의 개수와 win을 비교해서 같거나 더 크면 Winner를 그렇지 않으면 Loser를 리턴
테스트
1. Loser 케이스
2. Winner 케이스
"""