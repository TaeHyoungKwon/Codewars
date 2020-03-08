import unittest


def cyclic_string(s):
    # 다시 풀기
    return next((i for i, _ in enumerate(s[1:], 1) if s.startswith(s[i:])), len(s))


class TestCyclicString(unittest.TestCase):
    def test_should_return_1_when_given_s_is_same_char(self):
        s = 'cccccccc'
        actual = cyclic_string(s)
        self.assertEqual(actual, 1)

    def test_should_return_3_when_given_s_is_cabca(self):
        s = 'cabca'
        actual = cyclic_string(s)
        self.assertEqual(actual, 3)

    def test_should_return_5_when_given_s_is_ecbda(self):
        s = 'ecbda'
        actual = cyclic_string(s)
        self.assertEqual(actual, 5)

    def test_should_return_3_when_given_s_is_fbafbafbafbafb(self):
        s = 'fbafbafbafbafb'
        actual = cyclic_string(s)
        self.assertEqual(actual, 3)
