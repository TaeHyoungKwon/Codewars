import re
import unittest


def remove_parentheses(s):
    # 다시 풀어보기
    return re.sub(r"\(\w+\s\w+\)", "", s)


class TestRemoveParentheses(unittest.TestCase):
    def test_remove_parentheses(self):
        self.assertEqual(remove_parentheses(s="example (unwanted thing) example"), "example  example")

    def test_remove_parentheses_on_edge_case(self):
        self.assertEqual(remove_parentheses(s="(first group) (second group) (third group)"), "  ")
