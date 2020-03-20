import unittest
import math


def count_pairs_int(diff, n_max):
    # 시간 초과로 못품
    def _get_divisors_count(n):
        cnt = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n / i == i:
                    cnt = cnt + 1
                else:
                    cnt = cnt + 2
        return cnt

    numbers_under_n_max = range(1, n_max + 1)
    print(_get_divisors_count(18))

    return len(
        [
            1
            for first, second in zip(numbers_under_n_max, numbers_under_n_max[diff:])
            if _get_divisors_count(first) == _get_divisors_count(second)
        ]
    )


class TestCountPairsInt(unittest.TestCase):
    def test_should_return_8_when_given_diffand_n_max_is_1_and_50(self):
        diff, n_max = 1, 50
        actual = count_pairs_int(diff, n_max)
        self.assertEqual(actual, 8)
