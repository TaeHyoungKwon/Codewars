import unittest
import string

VOWEL = 'aeiou'
SPACE = ' '
EMPTY_SPACE = ''


def solve(s):
    def calc_max_value(filtered_list, alpha_to_num_mapping):
        max_val = 0
        for ele in filtered_list:
            result = 0
            for char in ele:
                result += alpha_to_num_mapping[char]
            if result > max_val:
                max_val = result
        return max_val

    alphabet_to_num = {alpha: idx + 1 for idx, alpha in enumerate(string.ascii_lowercase)}
    filtered_by_consonant = EMPTY_SPACE.join(ele if ele not in VOWEL else SPACE for ele in s).split()

    return calc_max_value(filtered_by_consonant, alphabet_to_num)
    
    
class TestConsonantValue(unittest.TestCase):
    def test_should_return_26_when_given_s_is_zodiac(self):
        actual = solve('zodiac')
        self.assertEqual(actual, 26)

    def test_should_return_80_when_given_s_is_chruschtschov(self):
        actual = solve('chruschtschov')
        self.assertEqual(actual, 80)
