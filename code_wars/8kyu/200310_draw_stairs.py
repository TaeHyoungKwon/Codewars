import unittest

NEW_LINE = "\n"
ONE_SPACE = " "
STAIR = "I"


def draw_stairs(n):
    return NEW_LINE.join((ONE_SPACE * idx) + STAIR for idx in range(n))


class TestDrawStairs(unittest.TestCase):
    def test_should_return_I_when_given_n_is_1(self):
        n = 1
        actual = draw_stairs(n)
        self.assertEqual(actual, "I")

    def test_should_return_I_and_I_with_new_line_when_given_n_is_2(self):
        n = 2
        actual = draw_stairs(n)
        self.assertEqual(actual, "I\n I")
