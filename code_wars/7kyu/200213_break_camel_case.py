import unittest


def generate_string_with_empty_space(s):
    split_words = []
    start_idx = 0

    for idx, ele in enumerate(s):
        if ele.isupper():
            split_words.append(s[start_idx:idx])
            start_idx = idx
    else:
        split_words.append(s[start_idx:])
    return split_words


def solution(s):
    return ' '.join(generate_string_with_empty_space(s))


class TestBreakCamelCase(unittest.TestCase):

    @staticmethod
    def _call_solution(s):
        return solution(s)

    def test_should_have_only_one_empty_space_when_given_s_has_only_one_upper_case_alphabet(self):
        self.assertEqual(self._call_solution('helloWord').count(' '), 1)

    def test_should_have_two_empty_space_when_given_s_has_two_upper_case_alphabet(self):
        self.assertEqual(self._call_solution('breakCamelCase').count(' '), 2)
