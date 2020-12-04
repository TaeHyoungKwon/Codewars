import unittest


def dashatize(n):
    if not n:
        return 'None'

    if not isinstance(n, int):
        return None

    prev_odd = False
    result = ''
    for num in str(n):
        if int(num) % 2:
            result += '-'
            result += num
            prev_odd = True
        else:
            if prev_odd:
                result += '-'
            result += num
            prev_odd = False
    return ''.join(result).strip('-')


class TestDashatize(unittest.TestCase):
    def test_dashatize_with_n_is_not_int(self):
        self.assertIsNone(dashatize("abcde"))

    def test_dashatize_common(self):
        self.assertEqual(dashatize(274), '2-7-4')

    def test_dashatize_with_many_even_num(self):
        self.assertEqual(dashatize(86320), '86-3-20')

    def test_dashatize_with_delete_first_dash(self):
        self.assertEqual(dashatize(974302), '9-7-4-3-02')
