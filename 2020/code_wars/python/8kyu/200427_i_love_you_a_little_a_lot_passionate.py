import unittest
from collections import deque


def how_much_i_love_you(nb_petals):
    words = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    deque_words = deque(words)

    while nb_petals > 1:
        deque_words.append(deque_words.popleft())
        nb_petals -= 1
    return deque_words[0]


class TestHowMuchILoveYOu(unittest.TestCase):
    def test_how_much_i_love_you(self):
        nb_petals = 7
        actual = how_much_i_love_you(nb_petals)
        self.assertEqual(actual, "I love you")
