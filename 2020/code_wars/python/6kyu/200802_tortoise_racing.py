import unittest


def race(v1, v2, g):
    if v1 > v2:
        return None

    seconds = g * 3600 // (v2 - v1)

    return [seconds//3600, seconds % 3600 // 60, seconds % 60]
    
    
class TestRace(unittest.TestCase):
    def test_race(self):
        v1, v2, g = 80, 100, 40
        actual = race(v1, v2, g)
        self.assertEqual(actual, [2, 0, 0])

    def test_race_with_under_1_houres(self):
        v1, v2, g = 720, 850, 70
        actual = race(v1, v2, g)
        self.assertEqual(actual, [0, 32, 18])
