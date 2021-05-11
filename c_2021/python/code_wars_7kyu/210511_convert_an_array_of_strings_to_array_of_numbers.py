import unittest


# def to_float_array(arr):
#     return [float(ele) for ele in arr]


def to_float_array(arr):
    return list(map(float, arr))


class TestToFloatArray(unittest.TestCase):
    def test_to_float_array(self):
        self.assertEqual(to_float_array(arr=["1.1", "2.2", "3.3"]), [1.1, 2.2, 3.3])


"""
문제
- arr를 받아서 리스트 형태로 나타내는 함수를 만들어라.
해결
- arr를 루프를 돌면서, 문자열로 되어있는 것들을 숫자로 casting 한다
조건
- input -> arr: List[str], output -> List[float]
절차
1. arr를 루프를 돌린다.
2. string으로 되어있는 각 element를 float으로 변경한다
3. 변경한 float를 temp list에 넣는다
4. temp list를 리턴한다
"""
