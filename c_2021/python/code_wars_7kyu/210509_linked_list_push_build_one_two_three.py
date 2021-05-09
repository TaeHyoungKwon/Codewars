# from typing import Optional
# import unittest
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def push(head: Optional[Node], data) -> Node:
#     node = Node(data)
#     if head:
#         node.next = head
#     return node
#
# def build_one_two_three() -> Node:
#     chained = push(None, 3)
#     chained = push(chained, 2)
#     return push(chained, 1)`


from typing import Optional
import unittest


class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


def push(head: Optional[Node], data: int) -> Node:
    return Node(data, head)


def build_one_two_three() -> Node:
    return Node(1, Node(2, Node(3)))


class TestPush(unittest.TestCase):
    def test_push_with_none(self):
        actual = push(None, 1)
        self.assertEqual(actual.data, 1)
        self.assertIsNone(actual.next)

    def test_push_with_not_none(self):
        actual = push(Node(1), 2)
        self.assertEqual(actual.data, 2)
        self.assertEqual(actual.next.data, 1)


class TestBuildOneTwoThree(unittest.TestCase):
    def test_build_one_two_three(self):
        actual = build_one_two_three()
        self.assertEqual(actual.data, 1)
        self.assertEqual(actual.next.data, 2)
        self.assertEqual(actual.next.next.data, 3)
        self.assertIsNone(actual.next.next.next)


"""
문제
- push와 build_one_two_three 메소드를 작성해라.
   - push / input -> head: Optional[Node], data: int, output -> Node
   - build_one_two_three / output -> Node
해결
- 문제를 잘 읽고 조건에 맞춰서 구현한다
조건
1. push
    - 인자로 head와 data parameter를 받는다
    - head는 node or None 이다.
    - head가 None이면 새로운 노드를 생성할 수 있어야 한다
2. build_one_two_trhee 함수는 1 -> 2 -> 3 -> null 로 되도록 노드를 생성하고 출력 해야한다.
절차
1. push 부터 구현
    - head가 None 일 때, -> parameter 로 데이터가 set, next는 None
    - head가 None 이 아닐 때,
2. 구현한 push를 활용하여서 build_one_two_three를 구현
    - paramete + 1 ,2,3 에 대해서 push 하도록 하고, 마지막에 null이 출력 되도록 한다
"""
