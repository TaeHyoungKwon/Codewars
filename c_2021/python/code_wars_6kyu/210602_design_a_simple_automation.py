import unittest
from typing import List

CMD_0_TRANSITION = {
    "q1": "q1",
    "q2": "q3",
    "q3": "q2",
}

CMD_1_TRANSITION = {
    "q1": "q2",
    "q2": "q2",
    "q3": "q2",
}


class Automaton(object):
    def __init__(self):
        self.states = ""

    def read_commands(self, commands: List[int]) -> bool:
        for ele in commands:
            if not self.states:
                self.states = "q1"
            if ele == "0":
                self.states = CMD_0_TRANSITION[self.states]
            else:
                self.states = CMD_1_TRANSITION[self.states]
        return self.states == "q2"


my_automaton = Automaton()


class TestAutomation(unittest.TestCase):
    def test_automation_on_true(self):
        my_automation = Automaton()
        self.assertTrue(my_automation.read_commands(commands=["1"]))

    def test_automation_on_false(self):
        my_automation = Automaton()
        self.assertFalse(my_automation.read_commands(commands=["1", "0", "0", "1", "0"]))


"""
문제
- 주어진 조건에 대해서 FSM를 구현하여라

해결
- 조건을 먼저 정리한 이후에, 조건에 맞춰서 문제를 해결해보자

조건
read_commands: input -> commands: List[str] output -> bool

1. input은 0과 1로만 주어짐
2. 상태는 3개를 가진다
3. q1 == start, q2 == accept(return true) -> 마지막 상태
4. transitions
    1 == q1 -> q2, q2 -> q2, q3 -> q2
    0 == q2 -> q3, q1 -> q1, q3 -> q2

절차
1. 주어진 input list를 받는다
2. 루프를 돌린다
3. q1 상태부터 시작하여서, list의 element에 따라서 상태를 변경한다
4. 루프를 다 돌았을 때, 최종 상태가 q2 이면 True, 아니면 False를 리턴한다

테스트
1. True를 리턴하는 경우
2. False를 리턴하는 경우
"""
