import unittest
from typing import List


def word_search(query: str, seq:List[str]) -> List[str]:
    searched = [word for word in seq if query.lower() in word.lower()]
    return searched or ["None"]


"""
def word_search(query, seq):
    query = query.casefold()
    return [x for x in seq if query in x.casefold()] or ['None']
"""


class TestWordSearch(unittest.TestCase):
    def test_word_search(self):
        self.assertEqual(word_search(query="ab", seq=["za", "ab", "abc", "zab", "zbc"]), ["ab", "abc", "zab"])

    def test_word_search_with_empty(self):
        self.assertEqual(word_search(query="aabbccdd", seq=["za", "ab", "abc", "zab", "zbc"]), ["None"])

    def test_word_search_with_edgecase(self):
        self.assertEqual(word_search(query="aB", seq=["za", "ab", "abc", "zab", "zbc"]), ["ab", "abc", "zab"])




"""
문제
- query와 일치하거나 substring인 seq의 element를 찾아서 리턴해라
해결
- seq 를 루프를 돌면서, ab가 일치 혹은 subset 인지 체크해서, 리스트에 append 한다
조건
- input - query: str, seq: List[str], output - List[str]
- 아무것도 해당되지않으면 ["None"] 를 리턴한다.
- case insensitive 함
절차
1. seq 를 루프를 돌면서, 해당 element의 lowercase 와 query의 lowercase가 일치 혹은 subset 인지 확인한다.
2. 일치 혹은 subset 이라면, temp list 에 element를 추가한다.
3. 일치하지 않으면, 루프를 패슿ㄴ다.
4. 일치하는 것이 1개도 없다면, 리스트 내에 'None' 문자열을 넣은채로 리턴한다.
"""
