import unittest

SPECIAL_NUMBERS = {0, 1, 2, 3, 4, 5}


def special_number(number: int) -> str:
    return "NOT!!" if any(int(digit) not in SPECIAL_NUMBERS for digit in str(number)) else "Special!!"


class TestSpecialNumber(unittest.TestCase):
    def test_special_number(self):
        self.assertEqual(special_number(number=23), "Special!!")

    def test_no_special_number(self):
        self.assertEqual(special_number(number=39), "NOT!!")
