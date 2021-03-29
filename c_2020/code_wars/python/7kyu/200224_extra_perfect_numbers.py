import unittest


def extra_perfect_number(n):
    n = format(n, 'b')
    return n[0] == n[-1] == '1'


def extra_perfect(n):
    return list(filter(extra_perfect_number, range(1, n+1)))


class TestExtraPerfect(unittest.TestCase):
    @staticmethod
    def _set_n_and_call_extra_perfect(n):
        actual = extra_perfect(n)
        return actual

    def test_should_return_1_and_3_when_given_n_is_3(self):
        self.assertEqual(self._set_n_and_call_extra_perfect(3), [1, 3])

    def test_should_return_1_and_3_and_5_when_given_n_is_5(self):
        self.assertEqual(self._set_n_and_call_extra_perfect(5), [1, 3, 5])
