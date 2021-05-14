import unittest
from typing import List, Optional, Union


def solution(
    items: Optional[List[Union[int, str]]], index: int, default_value: Union[int, str]
) -> Optional[List[Union[int, str]]]:
    try:
        return items[index]
    except IndexError:
        return default_value


class TestSolution(unittest.TestCase):
    def test_solution_with_no_index_error_and_positive_int(self):
        self.assertEqual(solution(items=[1, 2, 3], index=1, default_value="a"), 2)

    def test_solution_with_no_index_error_and_negative_int(self):
        self.assertEqual(solution(items=[1, 2, 3], index=-3, default_value="a"), 1)

    def test_solution_with_no_index_error_and_zero(self):
        self.assertEqual(solution(items=[1, 2, 3], index=0, default_value="a"), 1)

    def test_solution_with_index_error_and_positive_int(self):
        self.assertEqual(solution(items=[1, 2, 3], index=4, default_value="a"), "a")

    def test_solution_with_index_error_and_negative_int(self):
        self.assertEqual(solution(items=[1, 2, 3], index=-5, default_value="a"), "a")

    def test_solution_with_items_element_is_none(self):
        self.assertIsNone(solution(items=[None, None], index=1, default_value="a"))


"""
문제
- list와 index가 주어졌을 때, 해당하는 값을 리턴한다, 해당하는 범위를 넘어서면 기본값을 리턴한다
해결
- items list에 해당하는 index로 접근해서 값을 받아오는데, IndexError가 발생하면, default_value를 리턴한다
조건
input -> items: List[Optional[Union[int, str]]], index: int, default_value: Union[int, str]
output -> Optional[Union[int, str]]
절차
1. items list에 index를 대입하여서 값을 리턴한다. 
2. IndexError가 발생하면, default_value를 리턴한다
테스트
1. 정상
- index가 양수
- index가 음수
- index가 0일 때,

2. 실패(대체된 값이 리턴)
- index가 양수 이면서, 범위를 벗어날 떄,
- index가 음수 이면서, 범위를 벗어날 때,

3. 예외
- items가 둘다 None 일 때, -> None을 리턴해야한다
- 
"""
