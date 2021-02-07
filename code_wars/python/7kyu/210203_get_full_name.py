import unittest


class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class TestDinglemouse(unittest.TestCase):
    def test_get_full_name(self):
        d = Dinglemouse(first_name="TaeHyoung", last_name="Kwon")
        self.assertEqual(d.get_full_name(), "TaeHyoung Kwon")

    def test_get_full_name_with_first_name_is_empty_string(self):
        d = Dinglemouse(first_name="", last_name="Kwon")
        self.assertEqual(d.get_full_name(), "Kwon")

    def test_get_full_name_with_last_name_is_empty_string(self):
        d = Dinglemouse(first_name="TaeHyoung", last_name="")
        self.assertEqual(d.get_full_name(), "TaeHyoung")

    def test_get_full_name_with_all_empty_string(self):
        d = Dinglemouse(first_name="", last_name="")
        self.assertEqual(d.get_full_name(), "")
