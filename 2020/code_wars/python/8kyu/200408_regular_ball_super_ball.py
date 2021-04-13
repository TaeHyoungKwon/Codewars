import unittest

REGULAR_BALL = "regular"
SUPER_BALL = "super"


class Ball(object):
    def __init__(self, ball_type=REGULAR_BALL):
        self.ball_type = ball_type


class TestBass(unittest.TestCase):
    def test_regular_ball_type(self):
        self.assertEqual(Ball().ball_type, REGULAR_BALL)

    def test_super_ball_type(self):
        self.assertEqual(Ball("super").ball_type, SUPER_BALL)
