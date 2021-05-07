import math
from typing import Optional, List
import unittest


def is_prime(num):
    if num < 2:
        return False
    for ele in range(2, int(math.sqrt(num)) + 1):
        if num % ele == 0:
            return False
    return True


def step(g: int, m: int, n: int) -> Optional[List[int]]:
    try:
        return next([num, num + g] for num in range(m, n + 1) if is_prime(num) and is_prime(num + g) and num < n)
    except StopIteration:
        return None


class TestStep(unittest.TestCase):
    def test_step(self):
        self.assertEqual(step(2, 100, 110), [101, 103])

    def test_step_with_none(self):
        self.assertIsNone(step(2, 5, 5))


"""
문제
- 주어진 수가 2개 있을 때, step 만큼 차이나는 pair primenumber를 리턴해라
- input -> g: int, m: int, n: int output -> List[int]
해결
- 주어진 범위에서의 prime_number를 구한다
- 구해진 ele 마다 g 만큼 더해진 값이 존재하는지 확인하고 있으면 두 값을 리스트에 넣어서 리턴한다
조건
- g는 2보다 같거나 크다
- m은 2보다 같거나 크다
- n 은 m 보다 같거나 크다
- 범위 내에 pair가 존재하지 않으면 None을 리턴한다
절차
- 주어진 범위에서의 prime_number를 구한다
- 구해진 ele 마다 g 만큼 더해진 값이 존재하는지 확인하고 있으면 두 값을 리스트에 넣어서 리턴한다
"""
