import unittest
from itertools import zip_longest


def dup(arry):
    def generate_dup():
        for ele in arry:
            temp = ""
            consecutive_elements = list(zip_longest(ele, ele[1:]))
            for index, (first, second) in enumerate(consecutive_elements):
                if index == len(consecutive_elements) - 1:
                    temp += first
                    break
                if first != second:
                    temp += first
            yield temp

    return list(generate_dup())


class TestDup(unittest.TestCase):
    def test_dup(self):
        self.assertEqual(
            dup(arry=["ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo"]),
            ["codewars", "picaniny", "hubububo"],
        )


"""
문제
- 주어진 arr를 받아서, 루프를 돌면서, 각 string의 consecutive 하게 연속으로 나와있을 때 모두 제거 한채로 리턴
해결
- 루프를 돌면서, 각 string의 element가 consecutive 하게 중복되어있는지 확인하여서 중복되면 넘어가고 중복되지 않으면 맨앞의 string을 리턴한다, 마지막에는 무조건 리턴한다
조건
- 모두 lowercase 임
절차
1. 주어진 arr를 루프를 돌린다
2. 각 element들이 consecutive 하게 중복되어있는지 확인하여서(zip_longest 활용) 중복되면 넘어가고 중복되지 않으면 맨앞의 element를 리턴한다, 마지막에는 무조건 맨 앞의 element를 리턴한다
4. 결과 리스트에 추가해준다
테스트
- 1가지 성공 케이스 만으로 충분
"""