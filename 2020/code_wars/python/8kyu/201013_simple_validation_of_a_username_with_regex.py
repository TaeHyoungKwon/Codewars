import unittest
import re


def validate_usr(username):
    return re.match('^[a-z0-9_]{4,16}$', username) is not None


class TestValidateUsr(unittest.TestCase):
    def test_validate_usr_with_only_char(self):
        self.assertTrue(validate_usr(username='asddsa'))

    def test_validate_usr_with_char_and_num(self):
        self.assertTrue(validate_usr(username='asd34dsa'))

    def test_validate_usr_with_under_score(self):
        self.assertTrue(validate_usr(username='asd34_dsa'))
