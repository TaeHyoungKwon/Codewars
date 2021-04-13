import unittest
import string

ALPHABET_ASCII = string.ascii_lowercase


def name_value(my_list):
    result = []
    for index, ele in enumerate(my_list):
        temp = 0
        for char in ele:
            if char != ' ':
                temp += ALPHABET_ASCII.index(char) + 1
        result.append(temp * (index + 1))
    return result


class TestNameValue(unittest.TestCase):
    def test_name_value(self):
        self.assertEqual(name_value(my_list=["abc", "abc abc"]), [6, 24])
