import unittest


def remove(s):
    temp = list(s)
    for ele in s[::-1]:
        if ele == '!':
            temp.pop()
        else:
            break
    return ''.join(temp)


class TestRemove(unittest.TestCase):
    def test_should_return_sentence_without_all_of_exclamation_marks_from_the_end(self):
        s = 'Hi!'
        actual = remove(s)
        self.assertEqual(actual, 'Hi')

    def test_should_return_sentence_without_all_of_exclamation_marks_from_the_end_but_has_empty_space(self):
        s = 'Hi! Hi!'
        actual = remove(s)
        self.assertEqual(actual, 'Hi! Hi')
