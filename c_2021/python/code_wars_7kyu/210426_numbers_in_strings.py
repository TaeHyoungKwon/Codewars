import re
import unittest


def solve(s):
    return max(map(int, re.findall(r"[\d]+", s)))


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(s='gh12cdy695m1'), 695)


"""
문제
    - 소문자 문자열 내에서 가장 큰 숫자만 뽑아서 리턴
해결
    - 정규표현식 findall 로 숫자들을 다뽑아낸 후 그 중에서 가장 큰 숫자를 리턴
조건
    - 숫자가 0 부터 시작하는 경우는 없음
절차
    1. 정규표현식 findall을 이용하여서, 숫자만 걸러낸다.
    2. 이중에서 가장 큰 숫자를 리턴한다.
"""