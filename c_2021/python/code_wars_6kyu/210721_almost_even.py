import unittest


def split_integer(num, parts):
    origin = num
    result = []

    q, r = divmod(num, parts)
    if r == 0:
        return [q] * parts

    target = origin // parts + 1
    while num > 0:
        num -= target
        result.append(target)
        q, r = divmod(num, target - 1)
        if r == 0 and q + len(result) == parts:
            result.extend([target - 1] * q)
            break
    return result[::-1]


class TestSplitInteger(unittest.TestCase):
    def test_split_integer(self):
        self.assertEqual(split_integer(num=20, parts=6), [3, 3, 3, 3, 4, 4])
        self.assertEqual(split_integer(num=2, parts=2), [1, 1])
        self.assertEqual(split_integer(num=20, parts=5), [4, 4, 4, 4, 4])
        self.assertEqual(split_integer(num=10, parts=1), [10])
        self.assertEqual(split_integer(num=41, parts=17), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3])
