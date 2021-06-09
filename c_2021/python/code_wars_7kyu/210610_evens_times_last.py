import unittest


def even_last(numbers):
    return sum(numbers[::2]) * numbers[-1] if numbers else 0
    
    
class TestEvenLast(unittest.TestCase):
    def test_even_last(self):
        self.assertEqual(even_last(numbers=[2, 3, 4, 5]), 30)

    def test_even_last_on_numbers_is_empty(self):
        self.assertEqual(even_last(numbers=[]), 0)


"""
문제
- 주어진 숫자 sequence 값을 받아서, 짝수 index 값들을 더하고, 맨마지막 수를 곱한 값을 출력해라
해결
- numbers  index가 짝수인 값들은 더하고, 마지막에 맨마지막 값을 곱한 값을 리턴
조건
- input: List[int], output: int
절차
1. numbers 짝수 index수를 걸러 낸다
2. numbers의 맨 마지막 수를 걸러 낸다
3. 둘을 곱한 값을 리턴한다
테스트
1. 성공 케이스
2. 빈 값일 때는 0
"""