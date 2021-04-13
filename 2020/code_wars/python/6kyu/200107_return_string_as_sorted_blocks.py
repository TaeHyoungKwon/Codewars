import unittest
from collections import Counter


def blocks(s):
    # 정답 보고 품
    sort = lambda c: (c.isdigit(), c.isupper(), c)
    answer, counter = [], Counter(s)
    while counter:
        block = ''.join(sorted(counter, key=sort))
        answer.append(block)
        counter = counter - Counter(block)
    return '-'.join(answer)
    
    
class TestReturnStringAsSortedBlocks(unittest.TestCase):
    def test_should_return_empty_string_when_given_s_is_empty_string(self):
        s = ''
        actual = blocks(s)
        self.assertEqual(actual, '')

    def test_should_return_sorted_letters_without_dash_when_given_s_has_not_repeated_alphabet(self):
        s = '21AxBz'
        actual = blocks(s)
        self.assertEqual(actual, 'xzAB12')

    def test_should_return_sorted_letters_with_dash_when_given_s_has_repeated_alphabet(self):
        s = 'abacad'
        actual = blocks(s)
        self.assertEqual(actual, 'abcd-a-a')
        