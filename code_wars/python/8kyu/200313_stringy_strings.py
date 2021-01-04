import unittest

"""
* 각 숫자에 맞게 10 을 출력한다.

    - 테스트 케이스
        1. 홀수 일 때, size // 2 + 1 만큼의 1과 그 사이에 0을 넣는다
        2. 짝수 일 때, size // 2 만큼의 1과 그사이에 0을 넣는다 + 맨마지막 0 추가 한다.
"""

ZERO = '0'
ONE = '1'


def stringy(size):
    def handle_stringy_string(size, added_num=0):
        return ZERO.join(ONE for _ in range(size // 2 + added_num))
    if size % 2 == 1:
        return handle_stringy_string(size, added_num=1)
    return handle_stringy_string(size) + ZERO
    
    
class TestStringy(unittest.TestCase):
    def test_stringy_when_size_is_odd(self):
        # Given: Set size that is odd - 3 is one of odd num
        size = 3
        # When: Call stringy
        actual = stringy(size)
        # Then: Should return '101'
        self.assertEqual(actual, '101')

    def test_stringy_when_size_is_even(self):
        # Given: Set size that is even - 12 is one of even num
        size = 12
        # When: Call stringy
        actual = stringy(size)
        # Then: Should return '101010101010'
        self.assertEqual(actual, '101010101010')
