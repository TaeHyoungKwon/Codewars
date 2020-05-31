import unittest

INCREASE = 'i'
OUTPUT = 'o'
SQUARE = 's'
DECREASE = 'd'


def parse(data):
    result = []
    temp = 0
    for command in data:
        if command == OUTPUT:
            result.append(temp)
        elif command == INCREASE:
            temp += 1
        elif command == DECREASE:
            temp -= 1
        elif command == SQUARE:
            temp **= 2

    return result
    
    
class TestParse(unittest.TestCase):
    def test_data_is_only_o_command(self):
        data = 'ooo'
        actual = parse(data)
        self.assertEqual(actual, [0, 0, 0])

    def test_data_is_o_and_i_command(self):
        data = 'ioioio'
        actual = parse(data)
        self.assertEqual(actual, [1, 2, 3])

    def test_data_is_s_and_o_and_i_command(self):
        data = 'isoisoiso'
        actual = parse(data)
        self.assertEqual(actual, [1, 4, 25])

    def test_data_is_d_and_o_and_i_command(self):
        data = 'idoiido'
        actual = parse(data)
        self.assertEqual(actual, [0,1])
