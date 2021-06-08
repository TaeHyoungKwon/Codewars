import unittest


def generate_integers(m, n):
    return list(range(m, n + 1))
    
    
class TestGenerateIntegers(unittest.TestCase):
    def test_generate_integers(self):
        self.assertEqual(generate_integers(m=2, n=5), [2, 3, 4, 5])


"""
문제
- m, n을 받아서, m ~ n 사이의 int element를 가지는 리스트를 출력
해결
- m, n 을 받아서, range(m, n + 1)로 처리해준다
조건
input -> m: int, n: int / output -> List[int]
절차
range(m, n + 1) 로 리턴한다
테스트
* 해피패스 케이스 1개만 필요
"""
