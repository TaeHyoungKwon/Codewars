import unittest
from collections import Counter

SCORE_BOARD = {
    "Wild": (100, 10),
    "Star": (90, 9),
    "Bell": (80, 8),
    "Shell": (70, 7),
    "Seven": (60, 6),
    "Cherry": (50, 5),
    "Bar": (40, 4),
    "King": (30, 3),
    "Queen": (20, 2),
    "Jack": (10, 1),
}


def fruit(reels, spins):
    result = Counter([reels[index][spin] for index, spin in enumerate(spins)]).most_common()

    most_common_reel = result[0][0]
    if len(result) == 1:
        return SCORE_BOARD[most_common_reel][0]
    elif len(result) == 2:
        if result[1][0] == "Wild":
            return SCORE_BOARD[most_common_reel][1] * 2
        else:
            return SCORE_BOARD[most_common_reel][1]
    return 0


class TestFruit(unittest.TestCase):
    def test_fruit_with_plus_one_wild(self):
        reel1 = ["King", "Jack", "Wild", "Bell", "Star", "Seven", "Queen", "Cherry", "Shell", "Bar"]
        reel2 = ["Star", "Bar", "Jack", "Seven", "Queen", "Wild", "King", "Bell", "Cherry", "Shell"]
        reel3 = ["King", "Bell", "Jack", "Shell", "Star", "Cherry", "Queen", "Bar", "Wild", "Seven"]
        spin = [0, 5, 0]
        self.assertEqual(fruit(reels=[reel1, reel2, reel3], spins=spin), 6)

    def test_fruit(self):
        reel1 = ["King", "Cherry", "Bar", "Jack", "Seven", "Queen", "Star", "Shell", "Bell", "Wild"]
        reel2 = ["Bell", "Seven", "Jack", "Queen", "Bar", "Star", "Shell", "Wild", "Cherry", "King"]
        reel3 = ["Wild", "King", "Queen", "Seven", "Star", "Bar", "Shell", "Cherry", "Jack", "Bell"]
        spin = [0, 0, 1]
        self.assertEqual(fruit(reels=[reel1, reel2, reel3], spins=spin), 3)

    def test_fruit_with_not_matched(self):
        reel1 = ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"]
        reel2 = ["Bar", "Wild", "Queen", "Bell", "King", "Seven", "Cherry", "Jack", "Star", "Shell"]
        reel3 = ["Bell", "King", "Wild", "Bar", "Seven", "Jack", "Shell", "Cherry", "Queen", "Star"]
        spin = [5, 4, 3]
        self.assertEqual(fruit(reels=[reel1, reel2, reel3], spins=spin), 0)

    def test_fruit_with_all_matched(self):
        reel1 = ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"]
        reel2 = ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"]
        reel3 = ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"]
        spin = [0, 0, 0]
        self.assertEqual(fruit(reels=[reel1, reel2, reel3], spins=spin), 100)
