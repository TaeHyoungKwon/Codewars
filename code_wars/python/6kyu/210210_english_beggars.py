import unittest


def beggars(values, n):
    result = []
    loop = 0
    cnt = 0

    if n == 0:
        return []d

    if n > len(values):
        return values + [0] * (n - len(values))

    while cnt != len(values):
        temp = []
        for ele in values[loop::n]:
            cnt += 1
            temp.append(ele)
        loop += 1
        result.append(sum(temp))
    return result


class TestBeggars(unittest.TestCase):
    def test_beggars_with_n_is_0(self):
        self.assertEqual(beggars(values=[1, 2, 3, 4, 5], n=0), [])

    def test_beggars_with_n_is_1(self):
        self.assertEqual(beggars(values=[1, 2, 3, 4, 5], n=1), [15])

    def test_beggars_with_n_is_2(self):
        self.assertEqual(beggars(values=[1, 2, 3, 4, 5], n=2), [9, 6])

    def test_beggars_with_n_is_3(self):
        self.assertEqual(beggars(values=[1, 2, 3, 4, 5], n=3), [5, 7, 3])

    def test_beggars_with_n_is_6(self):
        self.assertEqual(beggars(values=[1, 2, 3, 4, 5], n=6), [1, 2, 3, 4, 5, 0])
