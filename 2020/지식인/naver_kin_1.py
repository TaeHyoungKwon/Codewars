import unittest


def val_change(d, v, c):
    if v not in d:
        return d, False
    d[d.index(v)] = c
    return d, True

    
class TestValChange(unittest.TestCase):
    def test_should_return_not_updated_data_and_flag_is_false(self):
        d, v, c = ['python', 'c++', 'java'], 'j++', 'm++'

        actual = val_change(d, v, c)

        self.assertEqual(actual[0], ['python', 'c++', 'java'])
        self.assertEqual(actual[1], False)

    def test_should_return_updated_data_and_flag_is_true(self):
        d, v, c = ['python', 'c++', 'java'], 'python', 'go'

        actual = val_change(d, v, c)

        self.assertEqual(actual[0], ['go', 'c++', 'java'])
        self.assertEqual(actual[1], True)
