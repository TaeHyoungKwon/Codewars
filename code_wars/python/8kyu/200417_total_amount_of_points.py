import unittest


def points(games):
    point = 0
    for game in games:
        x, y = game.split(':')
        if x > y:
            point += 3
        elif x < y:
            point += 0
        else:
            point += 1
    return point


class TestPoints(unittest.TestCase):
    def test_points(self):
        games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
        actual = points(games)
        self.assertEqual(actual, 30)
