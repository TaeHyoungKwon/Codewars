import unittest

import unittest


def sum_arrays(array1, array2):
    if not (array1 or array2):
        return []
    first_array = "".join(map(str, array1))
    second_array = "".join(map(str, array2))

    if not first_array:
        first_array = "0"

    if not second_array:
        second_array = "0"

    result = int(first_array) + int(second_array)
    if result < 0:
        result = list(map(int, str(result)[1:]))
        result[0] *= -1
        return result
    return list(map(int, str(result)))


class TestSumArrays(unittest.TestCase):
    def test_sum_arrays_on_empty(self):
        self.assertEqual(sum_arrays(array1=[], array2=[]), [])

    def test_sum_arrays_on_happy_path(self):
        self.assertEqual(sum_arrays(array1=[3, 2, 9], array2=[1, 2]), [3, 4, 1])

    def test_sum_arrays_on_minus_operator_in_first_array_first_index(self):
        self.assertEqual(sum_arrays(array1=[-3, 4, 2], array2=[3, 4, 4]), [2])

    def test_sum_arrays_on_minus_operator_in_second_array_first_index(self):
        self.assertEqual(sum_arrays(array1=[3, 2, 6, 6], array2=[-7, 2, 2, 8]), [-3, 9, 6, 2])


"""
조건
1. empty는 empty를 리턴
2. 주어지는 각 list를 문자열로 이은 다음에 num으로 바꾸고 더한 값을 다시 리스트로 리턴한다
3. 1번째 or 2번째 array list의 첫번째 index가 - 일경우는 - 연산이되도록 한다

테스트
1. empty 일 때,
2. -연산
    1번째 array
    2번째 array
3. 정상케이스
"""
