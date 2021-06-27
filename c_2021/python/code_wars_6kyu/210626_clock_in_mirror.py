import unittest

CLOCK_TIME_MAP = {
    1: (11, 10),
    2: (10, 9),
    3: (9, 8),
    4: (8, 7),
    5: (7, 6),
    6: (6, 5),
    7: (5, 4),
    8: (4, 3),
    9: (3, 2),
    10: (2, 1),
    11: (1, 12),
    12: (12, 11),
}


def what_is_the_time(time_in_mirror):
    hour, min = time_in_mirror.split(":")
    now, prev = CLOCK_TIME_MAP[int(hour)]
    if min == "00":
        return f"{now:>02}:00"
    return f"{prev:>02}:{60 - int(min):>02}"


class TestWhatIsTheTime(unittest.TestCase):
    def test_what_is_the_time_case_1(self):
        self.assertEqual(what_is_the_time(time_in_mirror="11:59"), "12:01")

    def test_what_is_the_time_case_2(self):
        self.assertEqual(what_is_the_time(time_in_mirror="06:35"), "05:25")

    def test_what_is_the_time_on_time(self):
        self.assertEqual(what_is_the_time(time_in_mirror="04:00"), "08:00")
