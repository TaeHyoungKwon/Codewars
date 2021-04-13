import unittest


def _print(bigger, not_bigger):
    return f"{not_bigger}{bigger[::-1]}{not_bigger}"


def shorter_reverse_longer(a, b):
    return _print(a, b) if len(a) >= len(b) else _print(b, a)


class TestShorterReverseLonger(unittest.TestCase):
    def test_shorter_reverse_longer_with_same_length(self):
        self.assertEqual(shorter_reverse_longer("first", "abcde"), "abcdetsrifabcde")

    def test_shorter_reverse_longer_length_of_a_is_bigger_than_b(self):
        self.assertEqual(shorter_reverse_longer("hello", "bau"), "bauollehbau")

    def test_shorter_reverse_longer_length_of_b_is_bigger_than_a(self):
        self.assertEqual(shorter_reverse_longer("hel", "baubau"), "heluabuabhel")
