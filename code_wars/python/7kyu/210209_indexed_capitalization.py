import unittest


def capitalize(s, ind):
    result = list(s)
    for ele in ind:
        try:
            result[ele] = result[ele].upper()
        except IndexError:
            pass
    return ''.join(result)


class TestCapitalize(unittest.TestCase):
    def test_capitalize(self):
        self.assertEqual(capitalize(s="abcdef", ind=[1, 2, 5]), "aBCdeF")

    def test_capitalize_with_index_error(self):
        self.assertEqual(capitalize(s="abcdef", ind=[1,2,5,100]), "aBCdeF")
