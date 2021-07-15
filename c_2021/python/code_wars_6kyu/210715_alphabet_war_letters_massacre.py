import unittest
from itertools import groupby

LEFT_SIDE = {
    "w": 4,
    "p": 3,
    "b": 2,
    "s": 1,
}

RIGHT_SIDE = {
    "m": 4,
    "q": 3,
    "d": 2,
    "z": 1,
}


def _has_asterisk_before_and_after(index, fight):
    if index == 0:
        if fight[index + 1] != "*":
            return False
        else:
            return True

    if index == len(fight) - 1:
        if fight[index - 1] != "*":
            return False
        else:
            return True

    if fight[index - 1] == "*" or fight[index + 1] == "*":
        return True
    else:
        return False


def _get_message(result):
    left_side_score, right_side_score = _calculate_sum(result)
    if left_side_score > right_side_score:
        return "Left side wins!"
    elif right_side_score > left_side_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"

def _is_left_side_letter(letter):
    return letter in LEFT_SIDE

def _calculate_sum(result):
    left_side_score = 0
    right_side_score = 0
    cleaned = [letter for letter in result if letter in LEFT_SIDE or letter in RIGHT_SIDE]
    for k, group in groupby(sorted(cleaned, key=_is_left_side_letter), key=_is_left_side_letter):
        if k:
            left_side_score = sum(LEFT_SIDE[letter] for letter in group)
        else:
            right_side_score = sum(RIGHT_SIDE[letter] for letter in group)
    return left_side_score, right_side_score


def alphabet_war(fight):
    if len(fight) == 1:
        return _get_message(fight)
    return _get_message([
        letter
        for index, letter in enumerate(fight)
        if letter != "*" and not _has_asterisk_before_and_after(index, fight)
    ])


class TestAlphabetWar(unittest.TestCase):
    def test_alphabet_war(self):
        self.assertEqual(alphabet_war(fight="z*z*z*zs"), "Left side wins!")

    def test_alphabet_war_edge(self):
        self.assertEqual(alphabet_war(fight="mb**qwwp**dm"), "Let's fight again!")

    def test_alphabet_war_edge_2(self):
        self.assertEqual(alphabet_war(fight="zdqmwpbs"), "Let's fight again!")

    def test_alphabet_war_edge_3(self):
        self.assertEqual(alphabet_war(fight='pdmsmq*ad*eeebdbs*dpf*zwdbb*w*'), 'Left side wins!')
