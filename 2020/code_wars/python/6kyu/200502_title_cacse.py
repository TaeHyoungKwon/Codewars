import unittest


def title_case(title, minor_words=''):
    result = []

    if not title:
        return ''

    minor_words_list = minor_words.lower().split()

    result.append(title.split()[0].capitalize())

    for word in title.split()[1:]:
        if word.lower() not in minor_words_list:
            result.append(word.capitalize())
        else:
            result.append(word.lower())

    return ' '.join(result)



class TestTitleCase(unittest.TestCase):
    def test_should_empty_string_when_given_title_is_empty_string(self):
        title = ''
        actual = title_case(title)
        self.assertEqual(actual, '')

    def test_title_case(self):
        title = 'a clash of KINGS'
        minor_words = 'a an the of'
        actual = title_case(title, minor_words)
        self.assertEqual(actual, 'A Clash of Kings')
