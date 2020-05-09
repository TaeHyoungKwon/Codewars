import unittest

VALID_ID = 'Santa Claus'
VALID_PW = 'Ho Ho Ho!'


class Sleigh(object):
    def authenticate(self, name, password):
        return name == VALID_ID and password == VALID_PW


class TestSleigh(unittest.TestCase):
    def setUp(self) -> None:
        self.sleigh = Sleigh()

    def test_should_return_true_when_given_name_is_santa_claus_password_is_hohoho(self):
        self.assertEqual(self.sleigh.authenticate('Santa Claus', 'Ho Ho Ho!'), True)

    def test_should_return_false_when_given_name_is_not_santa_claus_password_is_hohoho(self):
        self.assertEqual(self.sleigh.authenticate('Test', '1234'), False)
