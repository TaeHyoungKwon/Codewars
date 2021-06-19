from typing import List, Union, Callable
import unittest


true_if_even = lambda v, i: v % 2 == 0
never_true = lambda v, i: False
true_if_value_equals_index = lambda v, i: v == i
true_if_length_equals_index = lambda v, i: len(v) == i


def find_in_array(seq: List[Union[str, int]], predicate: Callable):
    try:
        return next(index for index, ele in enumerate(seq) if predicate(ele, index))
    except StopIteration:
        return -1


class TestFindInArray(unittest.TestCase):
    def test_find_in_array_on_return_true(self):
        self.assertEqual(find_in_array(seq=[1, 3, 5, 6, 7], predicate=true_if_even), 3)

    def test_find_in_array_on_return_false(self):
        self.assertEqual(find_in_array(seq=[2, 4, 6, 8], predicate=never_true), -1)



"""
문제
* 인자로 seq, predicate 이 주어질 때,
    1. seq를 루프돌면서 predicate을 실행할 때,
        * True가 나오면, 해당 index를 리턴
        * True가 나오지 않으면 -1을 리턴₩
해결
* 주어진 sequence를 루프를 돌면서, predicate가 참이 나오는지 확인 해서 해당 index를 리턴, 다 False 이면 -1 리턴
조건
input -> seq: List[int], predicate: Callable / output -> int
절차
1. seq를 루프를 돌린다
2. predicate을 seq element를 넘겨서 실행할 때
3. True 가 나오면, 해당 index를 리턴, 전부 False이면, -1을 리턴
테스트
* 아래 주어진 TEST 1가지만 통과하는 것을 확인하면 될 것 같다

"""