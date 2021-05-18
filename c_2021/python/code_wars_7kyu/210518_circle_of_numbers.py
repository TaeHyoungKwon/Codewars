import unittest
from collections import deque


def circle_of_numbers(n: int, fst: int) -> int:
    all_numbers = deque(list(range(fst, n)) + list(range(0, fst - 1)))
    for _ in range(n // 2):
        all_numbers.popleft()
    return all_numbers[0]


class TestCircleOfNumbers(unittest.TestCase):
    def test_circle_of_numbers(self):
        self.assertEqual(circle_of_numbers(n=10, fst=2), 7)


"""
문제
- 반대방향에 있는 숫자를 리턴해라
해결
- 절차에 적힌대로 풀이한다
조건
1. n의 범위는 0 ~ n-1
input -> n: int, fst, int / output -> int
절차
1. fst 기준으로 n-1 만큼 리스트를 생성
2. 0부터 fst-1 까지 생성
3. 1, 2 리스트를 합친다
4. n // 2 만큼 앞부터 pop을 한다
5. 모두 pop 했을 때, 첫번째 ele를 리턴

테스트
* 정상 케이스만 확인
"""