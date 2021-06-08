import unittest


def finance(n):
    return sum(sum(range(i, i * 2 + 1)) for i in range(n + 1))
    
    
class TestFinance(unittest.TestCase):
    def test_finance(self):
        self.assertEqual(finance(n=6), 168)


"""
문제
- 문제에 주어진 표대로 나온 모든 값을 더해라
해결
- 표에 적힌 규칙을 찾아서 각 n 마다 적절한 규칙을 적용한 값을 리턴하도록 해야한다
조건
- 이중포문을 사용하지 않는다
절차
1. 0 부터 n 까지의 각 range 합을 더해서 리턴한다
테스트
* 성공케이스 한번만 테스트 만들면 됨
"""