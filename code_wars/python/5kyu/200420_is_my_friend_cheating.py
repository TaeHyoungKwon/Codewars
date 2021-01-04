import unittest


def removNb(n):
    sequence = range(1, n + 1)
    sum_of_sequence = (n * (n + 1)) // 2

    result = []
    for num in sequence:
        if (sum_of_sequence - num) % (num + 1) == 0 and (sum_of_sequence - num) // (num + 1) < n:
            result.append((num, (sum_of_sequence - num) // (num + 1)))
    return result


class TestRemoveNb(unittest.TestCase):
    def test_remove_nb(self):
        n = 26
        actual = removNb(n)
        self.assertEqual(actual, [(15, 21), (21, 15)])
