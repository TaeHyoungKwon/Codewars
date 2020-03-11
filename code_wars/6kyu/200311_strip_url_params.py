import unittest

"""
* 리스트 안의 문자열을 나열하는 문자열을 새롭게 만든다
    - 테스트 케이스
        0. None 일 때, 빈 string을 리턴한다.
        1. 단어가 1개 일 때, 한 단어만 리턴한다.
        2. 단어가 2개 일 때, 중간에 'and'를 넣는다.
        3. 단어가 3개 이상 일 때, 중간은 ',' 를 넣고, 맨 마지막에 'and'를 넣는다.
"""

COMMA = ", "
AND = " and "
EMPTY_STRING = ""


def format_words(words):
    if not words:
        return EMPTY_STRING

    list_without_empty_string = [ele for ele in words if ele]
    if len(list_without_empty_string) < 3:
        return AND.join(list_without_empty_string)

    return COMMA.join(list_without_empty_string[:-1]) + AND + list_without_empty_string[-1]


class TestFormatWords(unittest.TestCase):
    def test_should_return_empty_string_when_given_word_is_none(self):
        words = None
        actual = format_words(words)
        self.assertEqual(actual, "")

    def test_should_return_one_word_when_given_word_count_is_one(self):
        words = ["one"]
        actual = format_words(words)
        self.assertEqual(actual, "one")

    def test_should_return_one_string_with_and_when_given_word_count_is_two(self):
        words = ["one", "two"]
        actual = format_words(words)
        self.assertEqual(actual, "one and two")

    def test_should_return_one_string_with_comma_and_and_when_given_word_count_is_more_than_two(self):
        words = ["one", "two", "three"]
        actual = format_words(words)
        self.assertEqual(actual, "one, two and three")

    def test_format_words_with_two_words_and_empty_string(self):
        words = ["one", "two", ""]
        actual = format_words(words)
        self.assertEqual(actual, "one and two")

    def test_format_words_with_two_words_and_empty_string(self):
        words = ['abcdefghijklmn', 'a', 'a', 'abcdefg', 'ab', 'abcdefgh', 'a', 'abcd', '']
        actual = format_words(words)
        self.assertEqual(actual, 'abcdefghijklmn, a, a, abcdefg, ab, abcdefgh, a and abcd')
