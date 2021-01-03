import unittest


def array(string):
    split_string = string.split(",")
    if len(split_string) < 3:
        return
    return " ".join(split_string[1:-1])


class TestArray(unittest.TestCase):
    def test_array_with_None(self):
        self.assertIsNone(array(string=""))

    def test_array_with_number_count_is_less_than_2(self):
        self.assertIsNone(array(string="1, 3"))

    def test_array_with_common_success_case(self):
        self.assertEqual(array(string="1,2,3,4"), "2 3")
