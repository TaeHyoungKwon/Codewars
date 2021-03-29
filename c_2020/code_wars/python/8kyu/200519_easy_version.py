import unittest

GOOD = 'good'

SMELL_MSG = 'I smell a series!'
PUBLISH_MSG = 'Publish!'
FAIL_MSG = 'Fail!'


def well(x):
    if x.count(GOOD) > 2:
        return SMELL_MSG
    elif x.count(GOOD) == 1 or x.count(GOOD) == 2:
        return PUBLISH_MSG
    else:
        return FAIL_MSG


class TestWell(unittest.TestCase):
    def test_should_return_fail_when_x_has_no_good_ideas(self):
        x = ['bad', 'bad', 'bad']
        actual = well(x)
        self.assertEqual(actual, 'Fail')

    def test_should_return_publish_when_x_has_one_good_ideas(self):
        x = ['good', 'bad', 'bad', 'bad']
        actual = well(x)
        self.assertEqual(actual, 'Publish')

    def test_should_return_publish_when_x_has_two_good_ideas(self):
        x = ['good', 'good', 'bad', 'bad']
        actual = well(x)
        self.assertEqual(actual, 'Publish')

    def test_should_return_smell_series_when_good_ideas_is_more_than_two(self):
        x = ['good', 'good', 'bad', 'bad', 'good']
        actual = well(x)
        self.assertEqual(actual, 'I smell a series!')
