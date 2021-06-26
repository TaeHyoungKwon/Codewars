import unittest


def f(n, m):
    cycle_ = [i % m for i in range(1, m + 1)]
    quotient, rest = divmod(n, m)
    return sum(cycle_) * quotient if rest == 0 else sum(cycle_) + (quotient * sum(cycle_[:rest]))


class TestF(unittest.TestCase):
    def test_f(self):
        self.assertEqual(f(10, 5), 20)

    def test_f_with_big_large_input(self):
        self.assertEqual(f(16000000000, 10), 72000000000)


"""
문제
* 주어진 수식을 코드로 표현해라
해결
* 일단 performance를 따지지 않고 풀어보자
* 
조건
* performance를 따져야함
절차
1. n을 기준으로 루프를 돌린다
2. i 변화에 따라서, % m 을 했을 때의 결과 값을 temp 리스트에 추가한다
3. temp에 추가된 값들을 더한다

테스트
1. 해피패스
2. large input
"""
