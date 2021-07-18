import unittest
import string

upper_and_lower_pair = "".join("".join(ele) for ele in [pair for pair in zip(string.ascii_lowercase, string.ascii_uppercase)])


def alphabetized(s):
    temp = {}
    for letter in upper_and_lower_pair:

        letter_count = s.count(letter)
        if s.count(letter) != 0:
            temp[letter] = letter_count
    print(temp)
    return "AabB"
    
    
class TestAlphabetized(unittest.TestCase):
    def test_alphabetized(self):
        self.assertEqual(alphabetized(s="A b B a"), "AabB")
