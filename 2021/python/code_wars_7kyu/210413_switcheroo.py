import unittest


def switcheroo(string: str) -> str:
    def generate_switcheroo():
        for chr in string:
            if chr == "b":
                yield "a"
            elif chr == "a":
                yield "b"
            else:
                yield chr

    return "".join(generate_switcheroo())


class TestSwitcheroo(unittest.TestCase):
    def test_switcheroo(self):
        self.assertEqual(switcheroo(string="aaabcccbaaa"), "bbbacccabbb")
