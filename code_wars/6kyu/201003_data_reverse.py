import unittest


def data_reverse(data):
    temp = []
    result = []
    for index, element in enumerate(data):
        temp.append(element)
        if (index + 1) % 8 == 0:
            result.append(temp)
            temp = []

    return [ele for group in result[::-1] for ele in group]


class TestDataReverse(unittest.TestCase):
    def test_data_reverse(self):
        data = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
        actual = data_reverse(data)
        self.assertEqual(actual, [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0])
