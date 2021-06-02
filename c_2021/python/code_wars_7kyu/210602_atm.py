import unittest

NOMINAL_VALUE = [10, 20, 50, 100, 200, 500]


def solve(n):
    count = 0
    for ele in NOMINAL_VALUE[::-1]:
        quotient, rest = divmod(n, ele)
        if ele == 10 and rest != 0:
            return -1
        count += quotient
        n -= quotient * ele
    return count


class TestSolve(unittest.TestCase):
    def test_solve_on_success(self):
        self.assertEqual(solve(n=770), 4)

    def test_solve_on_fail(self):
        self.assertEqual(solve(n=126), -1)



"""
문제
- 주어진 돈의 조합으로 주어진 n을 만들 수 있다면, 몇개가 사용되었는지를 리턴하고, 그렇지 안핟면 -1을 리턴한다

해결
- 주어진 돈 조합으로 n을 만들수 있는지 모든 경우의 수를 찾아보고 없으면 -1, 경우의 수가 있다면, 몇개 사용되었는지 최소 수를 찾아라

조건
- n의 크기는 1 ~ 1500

절차
1. 최소 경우를 찾아야 하기 때문에, 가장 큰 500 달러부터 대입해 본다
2. 주어진 돈의 조합으로 루프를 돌면서, 나누었을 때 몫을 구한다
3. 맨 마지막 루프에서는 나누어 떨어지는지 확인한다
4. 나누어 떨어진다면, 각 주어진 돈의 몫의 총합을 리턴한다 , 나누어 떨어지지 않으면 -1을 리턴한다

테스트
1. -1인 경우
2. 주어진 돈으로 n 값을 만들 수 있는 경우
"""