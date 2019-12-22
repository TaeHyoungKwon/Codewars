# https://www.codewars.com/kata/scramblies/train/python
import unittest


def scramble(s1, s2):
    for char in set(s2):
        if s1.count(char) < s2.count(char):
            return False
    return True


class TestScramble(unittest.TestCase):
    def test_should_false_when_s2_is_not_belong_to_s1(self):
        s1, s2 = "katas", "steak"
        result = scramble(s1, s2)
        self.assertEqual(result, False)

    def test_should_true_when_s2_is_belong_to_s1(self):
        s1, s2 = "scriptingjava", "javascript"
        result = scramble(s1, s2)
        self.assertEqual(result, True)

    def test_should_true_when_s2_is_belong_to_s1_case_two(self):
        s1, s2 = "cedewaraaossoqqyt", "codewars"
        result = scramble(s1, s2)
        self.assertEqual(result, True)

    def test_should_true_when_s2_is_belong_to_s1_case_three(self):
        s1, s2 = "rkqodlw", "world"
        result = scramble(s1, s2)
        self.assertEqual(result, True)

    def test_should_true_when_s2_is_belong_to_s1_case_four(self):
        s1, s2 = "scriptjava", "javascript"
        result = scramble(s1, s2)
        self.assertEqual(result, True)

    def test_should_false_when_s2_is_not_belong_to_s1_case_two(self):
        s1, s2 = "scriptjavx", "javascript"
        result = scramble(s1, s2)
        self.assertEqual(result, False)
