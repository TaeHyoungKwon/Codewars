import unittest


def remove_duplicate_words(s):
    temp = []
    for word in s.split():
        if word not in temp:
            temp.append(word)
    return ' '.join(temp)
    
    
class TestRemoveDuplicateWords(unittest.TestCase):
    def test_remove_duplicate_words_should_return_not_duplcated_words(self):
        s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
        actual = remove_duplicate_words(s)
        self.assertEqual(actual, "alpha beta gamma delta")
        