import unittest

ADAK = "adak"
ANANE = "anane"


def count_arara(n: int) -> str:
    def calc_adak():
        return [ADAK for _ in range(n // 2)]

    if n == 1:
        return ANANE
    elif n == 2:
        return ADAK
    else:
        temp = calc_adak()
        if n % 2:
            temp.append(ANANE)

    return ' '.join(temp)


class TestCountArara(unittest.TestCase):
    def test_count_arara_when_n_is_1(self):
        self.assertEqual(count_arara(n=1), ANANE)

    def test_count_arara_when_n_is_2(self):
        self.assertEqual(count_arara(n=2), ADAK)

    def test_count_arara_when_n_is_3(self):
        self.assertEqual(count_arara(n=3), "adak anane")

    def test_count_arara(self):
        self.assertEqual(count_arara(n=9), "adak adak adak adak anane")

    def test_count_arara(self):
        self.assertEqual(count_arara(n=10), "adak adak adak adak adak")
