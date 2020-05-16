import unittest

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

    
class TestGooseFilter(unittest.TestCase):
    def test_should_return_birds_without_gees(self):
        birds = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
        actual = goose_filter(birds)
        self.assertEqual(actual, ["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
