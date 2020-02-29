import unittest

"""
* digit 개수가 가장 많은 숫자를 찾아 리턴해라

    * 테스트 케이스
        1. digit length 가 가장 긴 것을 리턴한다. - 보통 케이스
        2. element의 digit 길이가 같을 때는 첫번째 element를 리턴한다.  
"""


def find_longest(arr):
    max = 0
    max_num = 0
    for ele in arr:
        if len(str(ele)) > max:
            max = len(str(ele))
            max_num = ele
    return max_num
    
    
class TestMostDigits(unittest.TestCase):
    def test_should_return_longest_digit_length(self):
        actual = find_longest([1, 10, 100])
        self.assertEqual(actual, 100)

    def test_should_return_first_element_when_element_digit_length_is_same(self):
        actual = find_longest([10, 20, 200, 30, 300])
        self.assertEqual(actual, 200)
