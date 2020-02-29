import unittest

"""
* 문자열이 주어졌을 떄, non-alphabet 캐릭터를 생략한채 문자열을 뒤집는다

    * 테스트 케이스
        1. non-alphabet이 포함된 경우
        2. non-alphabet이 포함되지 않은 경우
"""


def reverse_letter(string):
    return ''.join(ele for ele in string if ele.isalpha())[::-1]
    
    
class TestReverseString(unittest.TestCase):
    def test_string_with_only_alphabet(self):
        self.assertEqual(reverse_letter('krishan'), 'nahsirk')

    def test_string_with_non_alphabet(self):
        self.assertEqual(reverse_letter('ab23c'), 'cba')
