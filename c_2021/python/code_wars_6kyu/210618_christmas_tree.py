import unittest
from typing import Generator


def christmas_tree(height: int) -> str:
    def generate_christmas_tree() -> Generator:
        row = ""
        for i in range(1, height + 1):
            for j1 in range(1, -i + (height + 1)):
                row += " "
            for j2 in range(0, 2 * i - 1):
                row += "*"
            for j3 in range(1, -i + (height + 1)):
                row += " "
            yield row
            row = ""

    return "\n".join(list(generate_christmas_tree()))


class TestChristmasTree(unittest.TestCase):
    def test_christmas_tree_on_height_is_0(self):
        self.assertEqual(christmas_tree(height=0), "")

    def test_christmas_tree_on_height_is_1(self):
        self.assertEqual(christmas_tree(height=1), "*")

    def test_christmas_tree_on_height_is_5(self):
        self.assertEqual(christmas_tree(height=5), "    *    \n   ***   \n  *****  \n ******* \n*********")


"""
문제
* 주어진 height에 따라서 크리스마스 트리를 출력 해라

해결
* space로 padding 되어있는 부분과, *로 찍혀 있는 부분의 규칙을 찾아낸다

조건
1. height는 0 ~ 100
2. 맨마지막 라인에는 공백이 없다

절차
1. * 부분 부터 규칙을 찾아낸다(1, 3, 5, 7 ...)
2. " " 부분의 규칙을 찾아낸다 -> 역순
3. 1, 2번의 for loop를 합친다

테스트
1. 0일 때,
2. 1일 때,
3. 2 이상 일 때,
"""