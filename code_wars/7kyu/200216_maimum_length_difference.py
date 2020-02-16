import unittest


def calc_maximum_length_diff(a1, a2):
    max_a1 = max(map(len, a1))
    max_a2 = max(map(len, a2))
    min_a1 = min(map(len, a1))
    min_a2 = min(map(len, a2))
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))


def mxdiflg(a1, a2):
    return -1 if not (a1 and a2) else calc_maximum_length_diff(a1, a2)


class TestMaximumLengthDifference(unittest.TestCase):
    def test_should_return_minus_one_when_given_a1_and_a2_are_empty(self):
        a1, a2 = [], []
        actual = mxdiflg(a1, a2)
        self.assertEqual(actual, -1)

    def test_should_return_minus_one_when_given_a1_or_a2_are_empty(self):
        a1, a2 = [], ['abcde','asdf']
        actual = mxdiflg(a1, a2)
        self.assertEqual(actual, -1)

    def test_max_length_difference_between_a1_and_b2(self):
        a1 = [
            "hoqq",
            "bbllkw",
            "oox",
            "ejjuyyy",
            "plmiis",
            "xxxzgpsssa",
            "xxwwkktt",
            "znnnnfqknaz",
            "qqquuhii",
            "dvvvwz",
        ]
        a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        actual = mxdiflg(a1, a2)
        self.assertEqual(actual, 13)

    def test_max_length_difference_between_a1_and_b2_two(self):
        a1 = ['ejjjjmmtthh', 'zxxuueeg', 'aanlljrrrxx', 'dqqqaaabbb', 'oocccffuucccjjjkkkjyyyeehh']
        a2 = ['bbbaaayddqbbrrrv']
        actual = mxdiflg(a1, a2)
        self.assertEqual(actual, 10)