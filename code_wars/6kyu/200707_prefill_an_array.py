import unittest
from unittest import mock


def prefill(n, v):
    try:
        if isinstance(n, str) and not n.isdigit():
            raise TypeError

        n = int(n)
        if v is None:
            return [None] * n
        elif n == 0:
            return []
        else:
            return [v] * n

    except TypeError:
        return "{} is invalid".format(v)


class TestPrefille(unittest.TestCase):
    def test_should_list_with_none_when_v_is_none(self):
        self.assertEqual(prefill(n=2, v=None), [None, None])

    def test_should_empty_list_when_n_is_0(self):
        self.assertEqual(prefill(n=0, v=0), [])

    def test_prefill_with_just_int(self):
        self.assertEqual(prefill(n=2, v=123), [123, 123])

    def test_prefill_with_just_int_case_2(self):
        self.assertEqual(prefill(n='1', v=1), [1])

    def test_prefill_with_just_int_formatted_string(self):
        self.assertEqual(prefill(n=2, v="123"), ["123", "123"])

    @mock.patch("200707_prefill_an_array.prefill", mock.Mock(side_effect=TypeError))
    def test_prefill_with_type_error(self):
        with self.assertRaises(TypeError):
            self.assertEqual(prefill(n=2, v="123"), "xyz is invalid")
