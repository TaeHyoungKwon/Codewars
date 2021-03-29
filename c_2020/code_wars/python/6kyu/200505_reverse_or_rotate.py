import unittest


def revrot(strng, sz):
    def _can_not_take_a_chunk():
        return sz <= 0 or not strng or sz > len(strng)

    def _is_divisible_by_2(str_):
        return sum(map(int, str_)) % 2 == 0

    def _reverse(str_):
        return str_[::-1]

    def _rotate(str_):
        return str_[1:] + str_[0]

    def _is_length_of_strng_divisible_by_sz():
        return len(strng) % sz == 0

    if _can_not_take_a_chunk():
        return ""

    if not _is_length_of_strng_divisible_by_sz():
        strng = strng[: (len(strng) // sz) * sz]

    chunks = [strng[i : i + sz] for i in range(0, len(strng), sz)]

    return "".join(_reverse(chunk) if _is_divisible_by_2(chunk) else _rotate(chunk) for chunk in chunks)


class TestRevrot(unittest.TestCase):
    def test_should_return_empty_string_when_sz_is_equal_less_than_zero(self):
        self.assertEqual(revrot("abcde", 0), "")

    def test_should_return_empty_string_when_strng_is_empty(self):
        self.assertEqual(revrot("", 0), "")

    def test_should_return_empty_string_when_sz_is_greater_than_length_of_strng(self):
        self.assertEqual(revrot("abcde", 10), "")

    def test_revrot_when_strng_is_divisible_by_sz_on_success(self):
        self.assertEqual(revrot("123456987654", 6), "234561876549")

    def test_revrot_when_strng_is_not_divisible_by_sz_on_success(self):
        self.assertEqual(revrot("733049910872815764", 5), "330479108928157")
