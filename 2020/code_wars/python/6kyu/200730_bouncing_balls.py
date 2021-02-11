import unittest


def bouncing_ball(h, bounce, window):

    def is_invalid_parameter_conditions():
        return h <= 0 or not (0 < bounce < 1) or not (window < h)

    def get_up_down_count(h, bounce, window):
        cnt = 0
        while True:
            result = h * bounce
            if result <= window:
                break
            h = result
            cnt += 1
        return cnt

    if is_invalid_parameter_conditions():
        return -1

    return get_up_down_count(h, bounce, window) * 2 + 1


class TestBouncingBallCommon(unittest.TestCase):
    def test_bouncing_ball_with_common_case(self):
        self.assertEqual(bouncing_ball(h=3, bounce=0.66, window=1.5), 3)

    def test_bouncing_ball_with_common_second_case(self):
        self.assertEqual(bouncing_ball(h=30, bounce=0.66, window=1.5), 15)

    def test_bouncing_ball_with_common_third_case(self):
        self.assertEqual(bouncing_ball(h=2, bounce=0.5, window=1), 1)


class TestBouncingBallFailed(unittest.TestCase):
    def test_bouncing_ball_should_return_negative_one_when_h_is_not_greater_than_0(self):
        self.assertEqual(bouncing_ball(h=-1, bounce=1, window=1), -1)

    def test_bouncing_ball_should_return_negative_one_when_bounce_is_not_between_zero_and_one(self):
        self.assertEqual(bouncing_ball(h=0.5, bounce=1, window=1), -1)

    def test_bouncing_ball_should_return_negative_one_when_window_is_not_less_than_h(self):
        self.assertEqual(bouncing_ball(h=1, bounce=0.5, window=3), -1)
