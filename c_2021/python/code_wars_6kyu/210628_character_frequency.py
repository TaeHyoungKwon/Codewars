import unittest
from collections import Counter


def letter_frequency(text):
    return sorted([(k, v) for k, v in Counter(text.lower()).items() if k.isalpha()], key=lambda x: (-x[1], x[0]))


class TestLetterFrequency(unittest.TestCase):
    def test_letter_frequency(self):
        self.assertEqual(
            letter_frequency(text="As long as I'm learning something, I figure I'm OK - it's a decent day."),
            [
                ("i", 7),
                ("a", 5),
                ("e", 5),
                ("n", 5),
                ("g", 4),
                ("s", 4),
                ("m", 3),
                ("o", 3),
                ("t", 3),
                ("d", 2),
                ("l", 2),
                ("r", 2),
                ("c", 1),
                ("f", 1),
                ("h", 1),
                ("k", 1),
                ("u", 1),
                ("y", 1),
            ],
        )
