import unittest


def search_names(logins):
    return list(filter(lambda x: '_' in x[0], logins))
    
    
class TestSearchNames(unittest.TestCase):
    def test_search_names_with_underscore(self):
        logins = [["foo", "foo@foo.com"], ["bar_", "bar@bar.com"]]
        actual = search_names(logins)
        self.assertEqual(actual, [["bar_", "bar@bar.com"]])

    def test_search_names_without_underscore(self):
        logins = [["foo", "foo@foo.com"], ["bar", "bar@bar.com"]]
        actual = search_names(logins)
        self.assertEqual(actual, [])
