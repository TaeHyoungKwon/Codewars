import unittest
import re

VOWEL = {"a", "e", "i", "o", "u"}


# def vowel_2_index(string: str) -> str:
#     return "".join(str(index) if ele.lower() in VOWEL else ele for index, ele in enumerate(string, 1))


# def vowel_2_index(string):
#     return re.sub("[aeiouAEIOU]", lambda m: str(m.start() + 1), string)

def vowel_2_index(string):
    return re.sub("(?i)[aeiou]", lambda m: str(m.start() + 1), string)

# (?i) 는 case insensitive를 나타내는 옵션 -> https://docs.python.org/3/library/re.html#re.IGNORECASE

class TestVowel2Index(unittest.TestCase):
    def test_vowel_2_index(self):
        self.assertEqual(vowel_2_index(string="this is my string"), "th3s 6s my str15ng")

    def test_vowel_2_index_with_insensitive(self):
        self.assertEqual(vowel_2_index(string="this Is my string"), "th3s 6s my str15ng")


"""
1. 문제
- 문자열을 받아서, vowel이 있으면 index로 변경해라
2. 해결
- 전형적인 구현 문제
3. 조건
- input - string:str, output - str
- case insensitive
4. 절차
    1. string을 받아서, char 를 1개씩 검사한다.
    2. char를 lower 처리한 후, vowel 속하는지 검사한다.
    3. vowel에 속하게 되면, index를 append 한다.
    4. vowel에 속하지 않으면 해당 char를 append 한다.
    5. append 된 리스트를 join으로 문자열로 만든다.
"""
