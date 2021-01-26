import unittest


def multi_table(number):
    return "\n".join(f"{index} * {number} = {index * number}" for index in range(1, 11))


class TestMultiTable(unittest.TestCase):
    def test_multi_table(self):
        expected = "1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10"
        self.assertEqual(multi_table(number=1), expected)
