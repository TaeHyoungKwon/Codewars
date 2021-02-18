import unittest


def leo(oscar):
    if oscar > 88:
        return "Leo got one already!"
    elif oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    else:
        return "When will you give Leo an Oscar?"


class TestLeo(unittest.TestCase):
    def test_leo_with_oscar_is_88(self):
        self.assertEqual(leo(oscar=88), "Leo finally won the oscar! Leo is happy")

    def test_leo_with_oscar_is_86(self):
        self.assertEqual(leo(oscar=86), "Not even for Wolf of wallstreet?!")

    def test_leo_with_oscar_is_not_88_or_86(self):
        self.assertEqual(leo(oscar=87), "When will you give Leo an Oscar?")

    def test_leo_with_oscar_is_over_88(self):
        self.assertEqual(leo(oscar=898), "Leo got one already!")
