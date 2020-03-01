import unittest


"""
* 대 소문자 구분 없이 오름차순 정렬한다.
    - 테스트 케이스
        1. element가 1개일 때는 그대로 출력한다.
        2. element가 2개 이상일 때는 대 소문자 구분 없이 오름차순 정렬한다.
    - 참고 사항
        1. 없음
"""


def sortme(words):
    return sorted(words, key=lambda w: w.lower())


class TestSortMe(unittest.TestCase):
    def test_should_return_origin_element_when_given_words_element_is_one(self):
        words = ["CodeWars"]
        actual = sortme(words)
        self.assertEqual(actual, ["CodeWars"])

    def test_should_return_sorted_element_when_given_words_element_is_one(self):
        words = ["C", "d", "a", "B"]
        actual = sortme(words)
        self.assertEqual(actual, ["a", "B", "C", "d"])
