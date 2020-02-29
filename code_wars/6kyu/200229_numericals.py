import unittest

"""
* string element각 char가 처음으로 발생하면 1, 그 이상 발생하면 발생한 횟수를 나타낸다.

    * 테스트 케이스
        1. Hello -> 11121
        2. aaaaaaaaaaaa -> 123456789101112
        3. Hey hello -> 111112121   =>  Case-sensitive
"""


def numericals(s):
    mapped_dict = dict.fromkeys(s, 0)
    result = ""
    for ele in s:
        if ele in mapped_dict:
            mapped_dict[ele] += 1
            result += str(mapped_dict[ele])
    return result


class TestNumericals(unittest.TestCase):
    def test_should_return_11121_when_given_s_is_hello(self):
        s = "Hello"
        actual = numericals(s)
        self.assertEqual(actual, "11121")

    def test_should_return_123456789101112_when_given_s_is_aaaaaaaaaaaa(self):
        s = "aaaaaaaaaaaa"
        actual = numericals(s)
        self.assertEqual(actual, "123456789101112")

    def test_should_return_111112121_when_given_s_is_hey_hello(self):
        s = "Hey hello"
        actual = numericals(s)
        self.assertEqual(actual, "111112121")
