import math
import unittest
from functools import reduce
from typing import List, Optional, Union


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def multiple_args_gcd(*args):
    return reduce(gcd, args)


def sum_fracts(lst: List[List[int]]) -> Union[List[Optional[int]], int]:
    if not lst:
        return None
    denominator_list = [d for _, d in lst]
    denominator_proudction = math.prod(denominator_list)
    denominator_lcm = denominator_proudction // multiple_args_gcd(*denominator_list)

    sum_of_numerator_by_denominator = sum(
        numerator * (denominator_lcm // denominator) for numerator, denominator in lst
    )

    gcd_between_sum_of_numerator_and_denominator_lcm = math.gcd(sum_of_numerator_by_denominator, denominator_lcm)
    sum_of_numerator_by_denominator //= gcd_between_sum_of_numerator_and_denominator_lcm
    denominator_lcm //= gcd_between_sum_of_numerator_and_denominator_lcm

    return (
        sum_of_numerator_by_denominator // denominator_lcm
        if sum_of_numerator_by_denominator % denominator_lcm == 0
        else [sum_of_numerator_by_denominator, denominator_lcm]
    )


class TestSumFracts(unittest.TestCase):
    def test_sum_fracts_with_return_value_is_list_has_int(self):
        self.assertEqual(sum_fracts(lst=[[1, 2], [1, 3], [1, 4]]), [13, 12])

    def test_sum_fracts_with_return_value_is_int(self):
        self.assertEqual(sum_fracts(lst=[[1, 3], [5, 3]]), 2)



"""
문제
* lst를 받아서, 각각을 분자/분모 형태로 만들어서 더한 값을 리턴
해결
* lst를 루프를 돌면서, 분모 부분과 분자 부분 각각을 더해서, 출력하자
조건
input -> lst -> List[List[int]], output -> Union[List[int], int]
절차
1. lst를 루프를 돌린다
2. 분모의 최소공배수를 구한다
3. 분모의 최소공배수에 맞게 분자 값을 맞춰준다
4. 최종 리스트 내 element가 나누어 떨어지면, 나누어 떨어진 값을 리턴, 그렇지 않으면 그대로 리턴한다
조건
1. 최종 리스트가 나누어 떨어지면, 리스트가 아닌 int를 리턴
2. 최종 리스트가 나누어 떨어지지 않으면 리스트 형태로 리턴
테스트
* 별다른 조건이 없어서 해피패스만 처리
"""
