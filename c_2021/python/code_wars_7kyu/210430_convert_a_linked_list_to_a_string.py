import unittest
from typing import Optional


class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


def stringify(node: Optional[Node]) -> str:
    def generate_linked_node(node):
        while node:
            yield str(node.data)
            node = node.next

    if node is None:
        return "None"

    return f"{' -> '.join(generate_linked_node(node))} -> None"


class TestStringify(unittest.TestCase):
    def test_stringify(self):
        self.assertEqual(stringify(node=Node(0, Node(1, Node(2, Node(3))))), "0 -> 1 -> 2 -> 3 -> None")

    def test_stringify_node_is_none(self):
        self.assertEqual(stringify(node=None), "None")


"""
문제
- stringify 함수를 작성해라
input - node: Optional[Node], output - str
해결
- 전달받은 node의 값을 None 이 아닐 경우에 체크해서, value를 뽑아내고, 알맞은 문자열을 출력하도록 한다
조건
1. 현재 값 기준으로 보여준다.
2. 화살표 사이에는 공백이있다.
3. 맨끝은 None으로 끝나야 한다.
절차
1. node를 None 이 아닐 때까지 루프를 돌린다.
2. 각 루프를 돌 때마다, value를 뽑아서, temp 리스트에 append 한다
3. None일 경우에는 루프를 빠져나온다
4. ' -> '.join(temp) + -> None 을 리턴한다
"""
