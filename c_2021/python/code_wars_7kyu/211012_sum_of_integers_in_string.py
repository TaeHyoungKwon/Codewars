import re
import unittest


def sum_of_integers_in_string(s):
    return sum(map(int, re.findall(r"\d+", s)))
    
    
class TestSumOfIntegersInString(unittest.TestCase):
    def test_sum_of_integers_in_string(self):
        self.assertEqual(sum_of_integers_in_string(s="h3ll0w0rld"), 3)


"""
문제
* 주어진 s에서, 양수 숫자를 뽑아내서 모두 더한 값을 리턴하자
해결
* 정규표현식으로 양수를 모두 뽑아낸 후, sum 해서 리턴한다
테스트
* happy path
    문장에 숫자가 있는 경우에 해당 숫자를 모두 더한 값을 리턴
"""