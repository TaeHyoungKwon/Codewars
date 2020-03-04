import unittest
"""
1. 홀수 일 때, 문자열을 2개씩 나누는데, 맨마지막은 '_' 를 추가해준다.
2. 짝수 일 때는 문자열을 2개씩 나눈다.

edge
1. 빈 스트링 -> 빈 리스트
"""

TWO_STEP = 2


def solution(s):
    length = len(s)
    last_idx = length - 1

    def _make_split_string_list():
        for idx in range(0, length, TWO_STEP):
            split_string = s[idx: idx + 2]
            yield split_string + '_' if idx == last_idx else split_string

    return list(_make_split_string_list())
    
    
class TestSplitString(unittest.TestCase):
    def test_should_return_empty_list_when_given_s_is_empty(self):
        actual = solution("")
        self.assertEqual(actual, [])

    def test_string_length_is_odd_should_return_list_divided_by_two_char_with_underscore(self):
        actual = solution("asdfads")
        self.assertEqual(actual, ['as', 'df', 'ad', 's_'])

    def test_string_length_is_even_should_return_list_divided_by_two_char(self):
        actual = solution("asdfadsf")
        self.assertEqual(actual, ['as', 'df', 'ad', 'sf'])
