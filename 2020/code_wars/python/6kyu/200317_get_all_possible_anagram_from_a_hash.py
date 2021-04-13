from itertools import permutations
import unittest


def get_words(hash_of_letters):
    letters = ''.join(''.join(hash_of_letters[count] * count) for count in hash_of_letters)
    return sorted(set(''.join(ele) for ele in permutations(letters)))

    
class TestGetWords(unittest.TestCase):
    def test_get_words_sorted_all_combinations(self):
        actual = get_words({1: ["a", "b", "c"]})
        self.assertEqual(actual, ["abc", "acb", "bac", "bca", "cab", "cba"])

    def test_get_words_sorted_all_combinations_element_is_two(self):
        actual = get_words({2: ["a"], 1: ["b", "c"]})
        self.assertEqual(actual, ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"])


