import unittest


def capitals(word):
    return sorted([idx for idx, ele in enumerate(word) if ele.isupper()])
    
    
class TestFindTheCapitals(unittest.TestCase):
    def test_should_return_index_of_capital_char(self):
        word = 'CodEWaRs'
        actual = capitals(word)
        self.assertEqual(actual, [0, 3, 4, 6])

    def test_should_return_index_of_capital_char_when_given_word_is_IKWZxZGKFomilb(self):
        word = 'IKWZxZGKFomil'
        actual = capitals(word)
        self.assertEqual(actual, [0, 1, 2, 3, 5, 6, 7, 8])

    def test_should_return_sorted_by_index(self):
        word = 'KwonTaeHKyoung'
        actual = capitals(word)
        self.assertEqual(actual, [0, 4, 7, 8])
        