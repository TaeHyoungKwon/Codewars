import unittest


def solve(s: str) -> str:
    reversed_s = iter(s.replace(" ", "")[::-1])
    return ''.join(char if char == " " else next(reversed_s) for char in s)


class TestSolve(unittest.TestCase):
    def test_solve_with_no_space(self):
        self.assertEqual(solve(s="codewars"), "srawedoc")

    def test_solve(self):
        self.assertEqual(solve(s="your code"), "edoc ruoy")

    def test_solve_with_ordering(self):
        self.assertEqual(solve(s="your code rocks"), 'skco redo cruoy')

"""
문제
- 주어진 s를 뒤집어라
해결
- 공백 기준으로 element를 분리하여서 슬라이싱으로 뒤집는다
조건
- input -> s: str, output -> str
절차
1. 문자열을 일단 뒤집고, iter객체로 만든다
2. 기존 포맷을 유지해야기 때문에 문자열의 각 문자들을 루프를 돈다
3. 이때 space이면, space를 리턴하고, space가 아니면, iter 객체의 값 1개를 next로 리턴한다
4. 이를 join으로 감싼 
"""
