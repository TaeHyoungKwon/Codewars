import unittest

SHEEP = 'sheep'
WOLF = 'wolf'

NOT_CLOSEST_WOLF_MSG = "Oi! Sheep number {}! You are about to be eaten by a wolf!"
CLOSEST_WOLF_MSG = 'Pls go away and stop eating my sheep'


def warn_the_sheep(queue):
    length = len(queue)
    if queue[length - 1] == WOLF:
        return CLOSEST_WOLF_MSG

    count = 0
    for ele in queue[::-1]:
        if ele == WOLF:
            break
        if ele == SHEEP:
            count += 1

    return NOT_CLOSEST_WOLF_MSG.format(count)


class TestWarnTheSheep(unittest.TestCase):
    def test_warn_the_sheep_with_closest_wolf(self):
        self.assertEqual(warn_the_sheep(['sheep', 'sheep', 'wolf']), CLOSEST_WOLF_MSG)

    def test_warn_the_sheep_with_not_closest_wolf(self):
        queue = ['sheep', 'wolf', 'sheep']
        actual = warn_the_sheep(queue)
        self.assertEqual(actual, NOT_CLOSEST_WOLF_MSG.format(1))
