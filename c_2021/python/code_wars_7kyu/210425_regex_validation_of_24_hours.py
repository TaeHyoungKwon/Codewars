import re
import unittest


def validate_time(time):
    return bool(re.fullmatch(r'([0|1]?[0-9])|(2[0-3]):([0-5][0-9])', time))


class TestValidateTime(unittest.TestCase):
    def test_validate_time(self):
        self.assertFalse(validate_time(time="13:1"))
