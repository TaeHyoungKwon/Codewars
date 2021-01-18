import unittest


def whatday(num):
    return {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}.get(
        num, "Wrong, please enter a number between 1 and 7"
    )


class TestWhatday(unittest.TestCase):
    def test_watday_with_wrong_number(self):
        self.assertEqual(whatday(num=10), "Wrong, please enter a number between 1 and 7")

    def test_watday_num_is_3(self):
        self.assertEqual(whatday(num=3), "Tuesday")

    def test_watday_num_is_4(self):
        self.assertEqual(whatday(num=4), "Thursday")
