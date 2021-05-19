from typing import List, Callable, Union, Any
import unittest


def reject(seq: List[Union[str, int]], predicate: Callable[[Any], bool]):
    return [ele for ele in seq if not predicate(ele)]


class TestReject(unittest.TestCase):
    def test_reject_with_seq_has_only_int(self):
        self.assertEqual(reject(seq=[1, 2, 3, 4, 5, 6], predicate=lambda x: x % 2 == 0), [1, 3, 5])

    def test_reject_with_seq_has_only_str(self):
        self.assertEqual(reject(seq=["a", "b", "c", "d"], predicate=lambda x: type(x) == int), ["a", "b", "c", "d"])

    def test_reject_with_seq_has_element_mixed_by_str_and_int(self):
        self.assertEqual(reject(seq=["a", "b", 3, "d"], predicate=lambda x: type(x) == str), [3])


"""
문제
- 인자로 주어진 seq와 predicate 에 따라서 필터링 된 결과 값이 나오도록 한다
해결
- lamda의 인자로 seq를 넘겨줘서 결과가 나오도록 한다
조건
input -> seq: List[int, str], predicate -> Callable[[Any], bool]
절차
1. seq를 loop를 돌면서, predicate lambda 조건에 해당되지 않는 요소를 필터링 한다
테스트
1. 숫자만 있을 때,
2. 문자만 있을 때,
3. 숫자, 문자 섞여 있을 때,
"""
