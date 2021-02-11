import unittest


def name_shuffler(str_):
    first_name, last_name = str_.split()
    return f"{last_name} {first_name}"


class TestNameShuffler(unittest.TestCase):
    def test_name_shuffler(self):
        self.assertEqual(name_shuffler(str_="john McClane"), "McClane john")
