import math
import unittest


def _is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def num_primorial(n):
    temp = []
    count = 0
    i = 2
    while True:
        if count == n:
            break
        if _is_prime(i):
            temp.append(i)
            count += 1
        i += 1
    return math.prod(temp)


class TestNumPrimorial(unittest.TestCase):
    def test_number_primorial(self):
        self.assertEqual(num_primorial(n=4), 210)


"""
문제
- 주어진 n step 만큼, prime number를 구하고, 그 값들을 모두 곱한 값을 출력 해라.
해결
- prime number를 판별하고, 해당 수를 리스트에 넣고, step 만큼 필터링 되면 모두 곱한다
조건
- input -> n: int, output -> int
절차
1. prime number를 판별하는 is_prime 함수를 통해서 2 부터 시작해서 prime number 를 판별 한다
2. prime number라고 판별 되면, 순서대로 리스트로 넣는다
3. n의 개수가 똑같이 리스트에 들어가게 되면, 해당 리스트의 값들을 모두 곱한다
4. 리턴한다
테스트
1. 딱히 다른 조건이 없어서 성공 케이스만 테스트해도 괜찮을 것 같다
"""
