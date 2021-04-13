import unittest


def is_uppercase(inp):
    return inp.isupper()


class TestIsUpperCase(unittest.TestCase):
    def test_is_uppercase_should_return_true_when_all_of_element_is_uppercase(self):
        inp = "HELLO WORLD"
        actual = is_uppercase(inp)
        self.assertEqual(actual, True)

    def test_is_uppercase_should_return_false_when_all_of_element_is_not_uppercase(self):
        inp = "hello WORLD"
        actual = is_uppercase(inp)
        self.assertEqual(actual, False)

    def test_is_uppercase_should_return_false_when_some_element_is_special_char(self):
        inp = "#)_UPJY/PW.TNZ J5O]%7A+814VG"
        actual = is_uppercase(inp)
        self.assertEqual(actual, True)

