import unittest


def is_leap_year():
    day = int(input("Enter a day of the week"))
    month = int(input("Enter a month"))
    year = int(input("Enter a year"))

    if 0 < day < 32 and month in {1, 3, 5, 7, 8, 10, 12}:
        print("This is a correct day")
    elif 0 < day < 32 and month in {4, 6, 9, 11}:
        print("This is a correct day")
    elif 0 < day < 32 and month == 2:
        print("This is a correct day")
    elif year % 4 == 0 and year % 400 == 0 and year % 100 != 0 and month == 2 and 0 < day < 32:
        print("This is a correct day")
    else:
        print("This is an incorrect day")


class TestSolution(unittest.TestCase):
    def test_should_fail(self):
        self.fail()
