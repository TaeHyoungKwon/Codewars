import unittest


def remove_duplicate_words(s):
    splited_s_by_list = s.split()
    checking_duplicated = {word: 0 for word in splited_s_by_list}
    temp = []
    for word in splited_s_by_list:
        if checking_duplicated[word] == 0:
            temp.append(word)
            checking_duplicated[word] = 1
    return ' '.join(temp)
    
    
class TestRemoveDuplicateWords(unittest.TestCase):
    def test_remove_duplicate_words_should_return_not_duplcated_words(self):
        s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
        actual = remove_duplicate_words(s)
        self.assertEqual(actual, "alpha beta gamma delta")
        