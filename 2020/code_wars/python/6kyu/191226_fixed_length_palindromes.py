import itertools
import unittest


def check_palin(ele):
    return True if ele == ele[::-1] else False


def palin(a, b):
    temp = []
    cnt = 0
    for x in itertools.product(map(str, range(10)), repeat=a):
        if cnt == b:
            return int(temp[b-1])
        element = ''.join(x)
        if check_palin(element) and element[0] != '0':
            temp.append(element)
            cnt += 1


class TestPalinDrome(unittest.TestCase):
    def test_should_return_22_when_a_is_2_b_is_2(self):
        a, b = 2, 2
        actual = palin(a, b)
        self.assertEqual(actual, 22)

    def test_should_equal_length_between_a_and_actual_value(self):
        a, b = 2, 2
        actual = palin(a, b)
        self.assertEqual(len(str(actual)), 2)

    def test_should_return_palindrone_number_index_of_b_minus_1(self):
        a, b = 4, 5
        actual = palin(a, b)
        self.assertEqual(actual, 1441)

    def test_should_return_palindrone_number_when_a_is_5_b_is_19(self):
        a, b = 5, 19
        actual = palin(a, b)
        self.assertEqual(actual, 11811)