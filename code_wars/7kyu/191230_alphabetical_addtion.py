import string
import unittest


def add_letters(*letters):
    alphabet = string.ascii_lowercase
    sum_of_ele = sum(alphabet.index(ele) + 1 for ele in letters)
    return alphabet[sum_of_ele % 26 - 1] if sum_of_ele > 26 else alphabet[sum_of_ele - 1]


class TestAlphabeticalAddition(unittest.TestCase):
    def test_should_return_z_when_given_letters_length_is_zero(self):
        # Given: Set letters list
        letters = []
        # When: Call add_letters
        actual = add_letters(letters)
        # Then: add_letters should return z
        self.assertEqual(actual, "z")

    def test_should_return_z_when_given_letters_has_element_only_z(self):
        # Given: Set letters list
        letters = ["z"]
        # When: Call add_letters
        actual = add_letters(letters)
        # Then: add_letters should return z
        self.assertEqual(actual, "z")

    def test_should_return_f_when_given_letters_is_a_b_c(self):
        # Given: Set letters list
        letters = ["a", "b", "c"]
        # When: Call add_letters
        actual = add_letters(letters)
        # Then: add_letters should return z
        self.assertEqual(actual, "f")

    def test_should_return_d_when_given_letters_is_y_c_b(self):
        # Given: Set letters list
        letters = ["y", "c", "b"]
        # When: Call add_letters
        actual = add_letters(letters)
        # Then: add_letters should return z
        self.assertEqual(actual, "d")
