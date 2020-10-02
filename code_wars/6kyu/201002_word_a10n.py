import unittest

MAX_LENGTH = 4


def abbreviate(s):

    def _abbreviate_word(origin_word):
        if len(origin_word) < MAX_LENGTH:
            return origin_word

        return '{}{}{}'.format(origin_word[0], len(origin_word) - 2, origin_word[-1])

    if s.isalpha() or s == '':
        return _abbreviate_word(s)

    temp = []
    previous_index = 0
    for index, char in enumerate(s):
        if not char.isalpha():
            if previous_index != index:
                temp.append(_abbreviate_word(s[previous_index: index]))
            temp.append(char)
            previous_index = index + 1
    else:
        temp.append(_abbreviate_word(s[previous_index: index + 1]))

    return ''.join(temp)


class TestAbbreviate(unittest.TestCase):
    def test_abbreviate(self):
        self.assertEqual(abbreviate(s="internationalization"), "i18n")

    def test_abbreviate_with_hyphen(self):
        self.assertEqual(abbreviate(s="elephant-ride"), "e6t-r2e")

    def test_abbreviate_edge_case(self):
        self.assertEqual(
            abbreviate(s="double-barreled: is-on_balloon monolithic5cat:"),
            'd4e-b6d: is-on_b5n m8c5cat:',
        )
