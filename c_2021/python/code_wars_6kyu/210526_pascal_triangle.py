import unittest
from typing import List


def pascal(p: int) -> List[List[int]]:
    result = []
    initial = [1, 1]
    for index in range(1, p + 1):
        if index == 1:
            result.append([1])
        elif index == 2:
            result.append([1, 1])
        else:
            last_element = result[-1]
            initial[1:1] = list(map(sum, zip(last_element, last_element[1:])))
            result.append(initial)
            initial = [1, 1]
    return result


class TestPascal(unittest.TestCase):
    def test_pascal_with_p_is_1(self):
        self.assertEqual(pascal(p=1), [[1]])

    def test_pascal_with_p_is_2(self):
        self.assertEqual(pascal(p=2), [[1], [1, 1]])

    def test_pascal_with_p_is_equal_greater_than_3(self):
        self.assertEqual(pascal(p=5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])


"""
문제
- 파스칼 삼각형을 나타내도로 nested list를 리턴해라
해결
- index가 늘어 날 때 마다 해당하는 index가 특정 조건에 맞게 증가하는 형태이어야 한다
조건
- input -> p: int, output -> List[List[int]]
절차
1. 입력 받는 p를 기준으로 loop를 돌린다(4 라고 하면 4번 루프를 돈다(1~4))
2. 각 index 마다 주어진 공식에 따른 리스트를 생성하고, result list에 추가한다
테스트
1. 1일 때,
2. 2일 때,
3. 3 이상 일 떄,
"""