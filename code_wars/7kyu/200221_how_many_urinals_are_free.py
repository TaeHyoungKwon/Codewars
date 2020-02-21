import unittest

"""
규칙
* 사람과 사람 사이에는 소변기가 최소 1개는 있어야 한다.

구해야 하는 것
* 0-1 digit이 주어졌을 때, 최대 사용할 수 있는 소변기를 구하여라.

Edge Case
1. '1' 일 때는 0개 사용 가능하다.
2. '0' 일 때는 1개 사용 가능하다.
3. '10' 일 때는 0 개 사용 가능하다.

해결
* string 형태의 digit을 받아서, 0을 검사하는데 0 전 후에 1이 있는지 확인해서,
    없으면
        사용할 수 있음
    있으면
        사용할 수 없음
    으로 처리한다.
"""


def get_free_urinals(urinals):
    # 답보고 품
    return -1 if '11' in urinals else sum(((len(l)-1)//2 for l in f'0{urinals}0'.split('1')))


class TestUrinal(unittest.TestCase):
    def test_should_return_1_when_given_urinals_is_0(self):
        self.assertEqual(get_free_urinals('0'), 1)

    def test_should_return_0_when_given_urinals_is_1(self):
        self.assertEqual(get_free_urinals('1'), 0)

    def test_should_return_0_when_given_urinals_is_10(self):
        self.assertEqual(get_free_urinals('10'), 0)

    def test_should_return_0_when_given_urinals_is_01(self):
        self.assertEqual(get_free_urinals('01'), 0)

    def test_should_return_1_when_given_urinals_is_10001(self):
        self.assertEqual(get_free_urinals('10001'), 1)

    def test_should_return_0_when_given_urinals_is_1001(self):
        self.assertEqual(get_free_urinals('1001'), 0)
