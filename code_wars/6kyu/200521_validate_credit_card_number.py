import unittest

CHECK_EVEN_FLAG = 0
CHECK_ODD_FLAG = 1


def _get_list_doubled_every_other_digit(n):
    def _inner_get_list_doubled_every_other_digit(flag):
        return [int(char) * 2 if idx % 2 == flag else int(char) for idx, char in enumerate(str(n))]

    if len(str(n)) % 2 == 1:
        return _inner_get_list_doubled_every_other_digit(CHECK_ODD_FLAG)

    return _inner_get_list_doubled_every_other_digit(CHECK_EVEN_FLAG)


def _set_list_on_result_is_greater_than_9(doubled_list):
    return [ele - 9 if ele > 9 else ele for ele in doubled_list]


def _get_sum_of_final_digit(final_list):
    return sum(final_list)


def _is_valid_credit_card_number(sum_of_final_list):
    return sum_of_final_list % 10 == 0


def validate(n):
    doubled_list = _get_list_doubled_every_other_digit(n)
    final_list = _set_list_on_result_is_greater_than_9(doubled_list)
    sum_of_final_list = _get_sum_of_final_digit(final_list)
    return _is_valid_credit_card_number(sum_of_final_list)


class TestValidate(unittest.TestCase):
    def test_double_every_other_digit_on_length_of_digit_n_is_odd(self):
        n = 12345
        actual = _get_list_doubled_every_other_digit(n)
        self.assertEqual(actual, [1, 4, 3, 8, 5])

    def test_double_every_other_digit_on_length_of_digit_n_is_even(self):
        n = 1714
        actual = _get_list_doubled_every_other_digit(n)
        self.assertEqual(actual, [2, 7, 2, 4])

    def test_set_list_on_result_is_greater_than_9(self):
        doubled_list = [8, 18, 1]
        actual = _set_list_on_result_is_greater_than_9(doubled_list)
        self.assertEqual(actual, [8, 9, 1])

    def test_sum_of_the_final_digit(self):
        final_list = [8, 9, 1]
        actual = _get_sum_of_final_digit(final_list)
        self.assertEqual(actual, 18)

    def test_is_valid_credit_card_number_should_return_false_when_sum_of_final_digit_is_18(self):
        sum_of_final_digit = 18
        actual = _is_valid_credit_card_number(sum_of_final_digit)
        self.assertFalse(actual)
