import unittest


def add_length(str_):
    return [
        "{word}{space}{word_length}".format(word=word, space=" ", word_length=str(len(word))) for word in str_.split()
    ]


class TestAddLength(unittest.TestCase):
    def test_add_length(self):
        self.assertEqual(add_length(str_="apple ban"), ["apple 5", "ban 3"])
