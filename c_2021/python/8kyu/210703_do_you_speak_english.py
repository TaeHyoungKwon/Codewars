import re
import unittest


def sp_eng(sentence):
    return True if re.search(r"english", sentence.lower(), re.IGNORECASE) else False


class TestSpEng(unittest.TestCase):
    def test_sp_eng_on_true(self):
        self.assertTrue(sp_eng(sentence="english"))

    def test_sp_eng_on_false(self):
        self.assertFalse(sp_eng(sentence="egnlish"))
