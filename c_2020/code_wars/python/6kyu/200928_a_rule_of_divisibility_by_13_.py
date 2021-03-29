import unittest

REMAINDERS = (1, 10, 9, 12, 3, 4)


def thirt(initial_number):

    def calculate_thirt(number):
        return sum(int(ele) * REMAINDERS[index % len(REMAINDERS)]
                   for index, ele in enumerate(str(number)[::-1]))

    result = calculate_thirt(number=initial_number)
    before = result

    while True:
        new_result = calculate_thirt(number=before)
        if new_result == before:
            break
        before = new_result
    return new_result


class TestThirt(unittest.TestCase):
    def test_thirt(self):
        n = 8529
        actual = thirt(n)
        self.assertEqual(actual, 79)

    def test_thirt_too_long_n(self):
        n = 1111111111
        actual = thirt(n)
        self.assertEqual(actual, 71)

    def test_thirt_edge_case(self):
        n = 928622945
        actual = thirt(n)
        self.assertEqual(actual, 16)


