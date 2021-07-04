import unittest

FIXED_ANGLE = 30


def what_time_is_it(angle):
    if angle == 0:
        return "12:00"
    quotient, rest = divmod(angle, FIXED_ANGLE)
    if rest >= 5:
        quotient += 1
    return f"{str(quotient).zfill(2)}:00"


class TestWhatItmeIsit(unittest.TestCase):
    def test_what_time_is_it(self):
        self.assertEqual(what_time_is_it(angle=61), "02:00")
