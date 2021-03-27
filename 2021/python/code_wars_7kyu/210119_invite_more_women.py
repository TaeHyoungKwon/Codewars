import unittest


def invite_more_women(arr):
    return sum(arr) >= 1


class TestInviteMoreWomen(unittest.TestCase):
    def test_invite_more_women_should_return_false_when_sum_of_arr_is_empty_list(self):
        self.assertFalse(invite_more_women(arr=[]))

    def test_invite_more_women_should_return_false_when_sum_of_arr_is_less_than_1(self):
        self.assertFalse(invite_more_women(arr=[1, -1, 1, -1]))

    def test_invite_more_women_should_return_true_when_sum_of_arr_is_equal_more_than_1(self):
        self.assertTrue(invite_more_women(arr=[1, -1, 1]))
