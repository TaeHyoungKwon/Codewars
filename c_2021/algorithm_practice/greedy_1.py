# 큰 수의 법칙 p.92

import unittest


def big_num_law(given_list, able_to_add_count, consecutive_limit):
    max_num, second_max_num = sorted(given_list, reverse=True)[:2]
    result = 0

    while True:
        able_to_add_count, result = _sum_consecutive_max_num(able_to_add_count, consecutive_limit, max_num, result)
        if able_to_add_count == 0:
            break
        able_to_add_count, result = _sum_second_max_num_only_once(able_to_add_count, result, second_max_num)
    return result


def _sum_second_max_num_only_once(able_to_add_count, result, second_max_num):
    result += second_max_num
    able_to_add_count -= 1
    return able_to_add_count, result


def _sum_consecutive_max_num(able_to_add_count, consecutive_limit, max_num, result):
    for _ in range(consecutive_limit):
        if able_to_add_count == 0:
            break
        result += max_num
        able_to_add_count -= 1
    return able_to_add_count, result


class TestBigNumLaw(unittest.TestCase):
    def test_big_num_law(self):
        self.assertEqual(big_num_law(given_list=[2, 4, 5, 4, 6], able_to_add_count=8, consecutive_limit=3), 46)
