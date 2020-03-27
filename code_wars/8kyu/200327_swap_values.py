import unittest


# def swap_values(args):
#     # 문제 이상함...
#     return args[::-1]


def swap_values(args):
    args[0], args[1] = args[1], args[0]
    return args


class TestSwapValues(unittest.TestCase):
    def test_args_has_two_element(self):
        args = [1, 2]
        actual = swap_values(args)
        self.assertEqual(actual, [2, 1])

    def test_args_has_two_element_that_is_char(self):
        args = ['1', '2']
        actual = swap_values(args)
        self.assertEqual(actual, ['2', '1'])
