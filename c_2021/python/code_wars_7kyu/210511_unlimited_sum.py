import unittest


# def sum(*args) -> int:
#     result = 0
#     for num in args:
#         if isinstance(num, int):
#             result += num
#     return result


def sum(*args) -> int:
    return __builtins__["sum"](num for num in args if isinstance(num, int))


class TestSum(unittest.TestCase):
    def test_sum_with_string_in_args(self):
        self.assertEqual(sum(1, "2", 3), 4)

    def test_sum_with_string(self):
        self.assertEqual(sum(1, 2, 3), 6)


"""
문제
- sum 함수를 만들어라
해결
- 전달 받은 인자를 풀어서, 각 element를 검사해서, int 일경우 더한다
조건
- *args 는 num의 제한은 없다
- 인자중에 문자열이 있으면 무시한다
절차
1. args를 루프를 돌린다
2. 이중에서 int 인 값만 더한다
3. 리턴한다

"""
