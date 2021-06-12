from itertools import zip_longest
from typing import Tuple
import unittest


def add(num1, num2):
    num1, num2 = _check(str(num1), str(num2))
    return int("".join(str(int(first) + int(second)) for first, second in zip_longest(num1, num2)))


def _check(num1: str, num2: str) -> Tuple[int, int]:
    if len(num1) > len(num2):
        num1 = str(num1)
        num2 = str(num2).zfill(len(num1))
    elif len(num2) > len(num1):
        num2 = str(num2)
        num1 = str(num1).zfill(len(num2))

    return num1, num2
    
    
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(num1=122, num2=81), 1103)


"""
문제
* 두개의 수를 더하는데, 흔히 아는 덧셈이 아닌 각 digit을 오른쪽 끝으로 맞춰서 더한다
해결
* 문자열로 바꿨을 때 길이가 작은 좌측에 길이를 맞출 만큼의 패딩을 추가해준후, zip_longest로 더한 값을 join하고 int로 변경
조건
* input -> num1: int, num2: int, output -> int
절차
1. num1, num2를 str로 변경
2. 변경한 각 num1, num2의 길이를 뺀 절대 값을 구한다
3. 더 길이가 작은 값에 길이 만큼 0 패딩을 넣어준다
4. zip_longest로 두 값의 digit을 묶는다
5. 묶인 각 digit을 더한다
6. 더한 값을 문자열로 만들어서 join 한다
7. 6번 값을 int로 변경
"""