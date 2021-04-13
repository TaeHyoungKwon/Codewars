import unittest


def group_check(s):
    parentheses = {'[': ']', '(': ')', '{': '}'}

    stack = []
    for ele in s:
        if ele in parentheses:
            stack.append(ele)
        else:
            if stack:
                if ele == parentheses.get(stack[-1]):
                    stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False


class TestCheckingGroups(unittest.TestCase):
    def test_should_true_when_given_s_is_empty_string(self):
        s = ''
        actual = group_check(s)
        self.assertEqual(actual, True)

    def test_should_true_when_given_s_is_grouped_correctly(self):
        s = '()'
        actual = group_check(s)
        self.assertEqual(actual, True)

    def test_should_false_when_given_s_is_grouped_not_correctly(self):
        s = '{){)'
        actual = group_check(s)
        self.assertEqual(actual, False)

    def test_should_false_when_groups_left_open_or_closed_before_opened(self):
        s = '[])'
        actual = group_check(s)
        self.assertEqual(actual, False)
