import unittest


def split_and_add(numbers, n):
    for _ in range(n):
        mid = len(numbers) // 2
        front, back = numbers[:mid], numbers[mid:]
        if len(numbers) % 2:
            front.insert(0, 0)
        numbers = [f_ele + b_ele for f_ele, b_ele in zip(front, back)]
    return numbers


class TestSplitAndAdd(unittest.TestCase):
    def test_split_and_add_with_numbers_length_isodd_nunmber(self):
        self.assertEqual(split_and_add(numbers=[1, 2, 3, 4, 5], n=2), [5, 10])

    def test_split_and_add_with_numbers_length_is_even_nunmber(self):
        self.assertEqual(split_and_add(numbers=[23,345,345,345,34536,567,568,6,34536,54,7546,456], n=20), [79327])

    def test_split_and_add_on_n_is_0(self):
        self.assertEqual(split_and_add(numbers=[1, 2, 3, 4, 5], n=0), [1, 2, 3, 4, 5])



"""
문제
* 문제에 주어진 step을 n 번 만큼 반복했을 때, 결과 값을 리턴
해결
* 아래 조건과 절차대로 진행
조건
1. step1 - numbers list를 2개의 파트로 나눈다
2. step2 - 개수가 모자란 리스트를 좌측 패딩(0)을 추가한다
3. step3 - 두 리스트를 더한다
4. 1~3번을 n번 반복한다
절차
* 조건과 동일
테스트
1. n이 0 일 때,
2. n이 1 이상 일 때,
"""