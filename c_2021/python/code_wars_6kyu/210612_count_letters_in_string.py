from collections import Counter
import unittest


def letter_count(s):
    return Counter(s)
    
    
class TestLetterCount(unittest.TestCase):
    def test_letter_count(self):
        self.assertEqual(letter_count(s="codewars"), {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1})


"""
문제
* 주어진 s 각 알파벳 letter의 빈도를 value 나타내는데, key를 기준으로 정렬되어있어야 한다
해결
* 일단 Count로 해본, key 정렬하는 것을 어떻게 구현할지가 중요
* sorted를 이용해서 일단은 list의 튜플형태로 만들고 다시 dict로 변환
테스트
* 다른 조건이 없어서, 성공케이스만 확인
"""