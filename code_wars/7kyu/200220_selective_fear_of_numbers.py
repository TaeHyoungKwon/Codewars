import unittest


def is_afraid(day, num):
    afraid_dict = {
        "Monday": num == 12,
        "Tuesday": num > 95,
        "Wednesday": num == 34,
        "Thursday": num == 0,
        "Friday": num % 2 == 0,
        "Saturday": num == 56,
        "Sunday": num == 666 or num == -666,
    }
    return afraid_dict[day]


def am_I_afraid(day, num):
    return is_afraid(day, num)


class TestAmIAfraid(unittest.TestCase):
    def test_should_return_true_when_day_is_mon_and_num_is_12(self):
        actual = am_I_afraid("Monday", 12)
        self.assertEqual(actual, True)

    def test_should_return_false_when_day_is_mon_and_num_is_not_12(self):
        actual = am_I_afraid("Monday", 13)
        self.assertEqual(actual, False)

    def test_should_return_true_when_day_is_tue_and_num_is_greater_than_95(self):
        actual = am_I_afraid("Tuesday", 96)
        self.assertEqual(actual, True)

    def test_should_return_true_when_day_is_wed_and_num_is_34(self):
        actual = am_I_afraid("Wednesday", 34)
        self.assertEqual(actual, True)

    def test_should_return_true_when_day_is_thu_and_num_is_0(self):
        actual = am_I_afraid("Thursday", 0)
        self.assertEqual(actual, True)

    def test_should_return_true_when_day_is_fri_and_num_is_divisible_by_2(self):
        actual = am_I_afraid("Friday", 4)
        self.assertEqual(actual, True)

    def test_should_return_true_when_day_is_sat_and_num_is_56(self):
        actual = am_I_afraid("Saturday", 56)
        self.assertEqual(actual, True)

    def test_should_return_true_when_day_is_sun_and_num_is_666(self):
        actual = am_I_afraid("Sunday", 666)
        self.assertEqual(actual, True)

    def test_should_return_true_when_day_is_sun_and_num_is_negative_666(self):
        actual = am_I_afraid("Sunday", -666)
        self.assertEqual(actual, True)
