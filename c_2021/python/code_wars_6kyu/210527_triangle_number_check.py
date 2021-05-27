import unittest


def is_triangle_number(number: int) -> bool:
    if isinstance(number, bool) or not isinstance(number, int):
        return False
    if number == 0:
        return True
    for i in range(1, number + 1):
        if i * (i + 1) == 2 * number:
            return True
    return False


class TestIsTriangleNumber(unittest.TestCase):
    def test_is_triangle_number_with_given_number_type_is_str(self):
        self.assertFalse(is_triangle_number(number="abcde"))

    def test_is_triangle_number_with_given_number_type_is_float(self):
        self.assertFalse(is_triangle_number(number=0.123))

    def test_is_triangle_number_with_given_number_type_is_int_and_number_is_not_triangle_number(self):
        self.assertFalse(is_triangle_number(number=5))

    def test_is_triangle_number_with_given_number_type_is_int_and_number_is_triangle_number(self):
        self.assertTrue(is_triangle_number(number=6))

    def test_is_triangle_number_with_boolean_false(self):
        self.assertFalse(is_triangle_number(number=False))

    def test_is_triangle_number_with_boolean_true(self):
        self.assertFalse(is_triangle_number(number=True))

    def test_is_triangle_number_is_0(self):
        self.assertTrue(is_triangle_number(number=0))


"""
문제
* 입력 값이 triangle number인지 판단하여서 True or False를 리턴하여라
해결
* 1, 3, 6, 10, 15 ... --> 다음 수열을 구할 수 있는 식을 만든 후, 맞으면 True, 틀리면 False를 리턴한다
조건
* input -> number: int, output -> bool
* 코드 효율성을 따져서 작성해야한다(큰 숫자가 들어올 수 있음)
절차
1. input이 int만 들어 올 수 있도록 validation 체크 한다
2. triangle_number를 판별하는 수열에 속하는지 확인해서, 있으면 True, 없으면 false를 리턴한다
테스트
1. number가 문자 일 때,
2. number가 int가 아닐 때,
3. number가 int이고, triangle_number가 맞는 경우
4. number가 int이고, triangle_number가 아닌 경우
"""
