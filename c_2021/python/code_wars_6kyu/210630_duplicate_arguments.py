import unittest
from collections import Counter


def solution(*args):
    return any(count for count in Counter(args).values() if count != 1)


class TestSolution(unittest.TestCase):
    def test_solution_on_return_value_is_true_with_all_ele_are_num(self):
        self.assertTrue(solution(1, 2, 3, 1, 2))

    def test_solution_on_return_value_is_true_with_all_ele_are_str_num(self):
        self.assertTrue(solution("1", "2", "3", "1", "2"))

    def test_solution_on_return_value_is_false_with_all_ele_are_num(self):
        self.assertFalse(solution(1, 2, 3))

    def test_solution_on_return_value_is_false_with_all_ele_are_str_num(self):
        self.assertFalse(solution("1", "2", "3"))



"""
문제
* 인자로 넘어오는 값이 겹치는지에 따라서 True or False를 리턴해라 -> 겹쳐야 True
해결
* 아래 절차대로 풀이한다
조건
1. element들은 string or number 이다
절차
1. *args로 인자들을 리스트로 받는다
2. Counter를 이용해서 dict를 만든다
3. 2의결과의 values 했을 때 값이 1로 같은지 검사한다
4. 모두 1로 같다면, False, 그렇지 않다면 True 를 리턴한다
테스트
1. True 일 경우,
* 문자
* 숫자
2. False 일 경우,
* 문자
* 숫자
"""