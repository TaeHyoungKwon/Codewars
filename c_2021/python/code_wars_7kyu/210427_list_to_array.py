import unittest
from typing import Any, List


class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def list_to_array(node: LinkedList) -> List[Any]:
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result


class TestListToArray(unittest.TestCase):
    def test_list_to_array(self):
        self.assertEqual(list_to_array(node=LinkedList(4, LinkedList(25, LinkedList(30)))), [4, 25, 30])


"""
문제
- 미리 구현된 Linked List node를 받아서, 이를 python list 로 변환해서 리턴한다.
해결
- for문을 돌면서, value를 뽑아서 append하고, next가 있으면 이동해서 value를 뽑아낸다. next가 없으면 끝낸다
조건
input - node:LinkedList[Union[int, str, bool], output - List[Union[int, str, bool]]
절차
1. node에서 value를 뽑아내서 append 한다
2. next가 있은지 확인한다
3. 있으면, next의 value를 뽑아서 append 한다
4. 없으면, 루프를 끝낸다.

"""