from functools import reduce
from operator import mul
from typing import List, Optional


def product(numbers: Optional[List[int]]) -> Optional[int]:
    return reduce(mul, numbers) if numbers else None


class TestProduct:
    def test_product_should_return_none(self):
        assert product(None) is None
        assert product([]) is None

    def test_product(self):
        assert product([5, 4, 1, 3, 9]) == 540


"""
문제
* 주어진 숫자 리스트의 곱을 리턴해야한다
해결
* reduce를 활용해서 문제를 풀어보자
조건
1. None 일 때는 None을 리턴한다
2. 빈 리스트 일 때도 None을 리턴한다
테스트
1. None 인 경우,
2. element 1개인 경우, 복수개 인 경우는 같이 테스트
"""