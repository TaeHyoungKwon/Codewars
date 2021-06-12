import itertools
import unittest


def squares_needed(gains):
    return next(i for i in itertools.count(0) if 2 ** i > gains)


class TestSquaresNeeded(unittest.TestCase):
    def test_squares_needed(self):
        self.assertEqual(squares_needed(gains=4), 3)
