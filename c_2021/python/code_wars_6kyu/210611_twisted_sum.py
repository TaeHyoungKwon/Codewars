import unittest


def compute_sum(n):
    return sum(sum(map(int, str(ele))) for ele in range(1, n + 1))
    
    
class TestComputeSum(unittest.TestCase):
    def test_compute_sum_with_under_10(self):
        self.assertEqual(compute_sum(n=4), 10)

    def test_compute_sum_with_equal_more_than_10(self):
        self.assertEqual(compute_sum(n=12), 51)


"""
문제
- 주어진 n에 대해서 1~n 까지 수의 각 digit의 합을 구해라

해결
- 1~n 까지의 element 리스트를 구한 다음에 각 digit을 계속 합한다

조건
- 

절차
1. 1 ~ n 까지의 element를 구한다
2. loop를 돌면서, 각 digit을 구해서 더해서 새로운 리스트에 넣는다
3. loop가 끝났을 때, 새로운 리스트에 담긴 element를 모두 더해서 리턴한다

테스트
1. 9 이하 일 때,
2. 10 이상 일 때,

"""