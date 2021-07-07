import unittest
from collections import Counter
from operator import itemgetter


def string_letter_count(s):
    return "".join(
        f"{v}{k.lower()}" for k, v in sorted(Counter(map(str.lower, s)).items(), key=itemgetter(0)) if k.isalpha()
    )


class TestStringLetterCount(unittest.TestCase):
    def test_string_letter_count_on_s_is_empty_string(self):
        self.assertEqual(string_letter_count(s=""), "")

    def test_string_letter_count_on_happy_path(self):
        self.assertEqual(
            string_letter_count(s="The quick brown fox jumps over the lazy dog."),
            "1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z",
        )


"""
조건
1. 알파벳 기준 정렬되어야 한다
2. 각 알파벳 앞에 개수가 표시되어야 한다
3. 알파벳 외는 포함되지 않아야 한다
4. empty string이거나 letter가 없으면 empty string을 리턴한다


절차
1. Counter 알파벳과 개수를 뽑아낸다.
2. 1번의 결과를 for loop를 돌린다,
3. 이중 알파벳 부분만 필터하여서, 답안의 문자열을 만든다
"""