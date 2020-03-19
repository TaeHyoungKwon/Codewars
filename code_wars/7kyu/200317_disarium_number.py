import unittest

NOT_STRING = "Not !!"
DISARIUM_STRING = "Disarium !!"


def disarium_number(number):
    return (DISARIUM_STRING
            if sum(int(ele) ** (idx + 1) for idx, ele in enumerate(str(number))) == number
            else NOT_STRING)


class TestDisariumNumber(unittest.TestCase):
    def test_should_return_disarium_string_when_given_number_is_89(self):
        self.assertEqual(disarium_number(89), DISARIUM_STRING)

    def test_should_return_not_string_when_given_number_is_1024(self):
        self.assertEqual(disarium_number(1024), NOT_STRING)
