import unittest


def number(lines):
    return ['{}: {}'.format(idx + 1, ele)
            for idx, ele in enumerate(lines)]


class TestNumber(unittest.TestCase):
    def test_should_return_empty_list_when_given_lines_empty(self):
        # Given: Set lines empty
        lines = []
        # When: Call number
        result = number(lines)
        # Then: test should return empty list
        self.assertEqual(result, [])

    def test_success_case(self):
        # Given: Set lines empty
        lines = ['a', 'b', 'c']
        # When: Call number
        result = number(lines)
        # Then: test should return empty list
        self.assertEqual(result, ["1: a", "2: b", "3: c"])
        