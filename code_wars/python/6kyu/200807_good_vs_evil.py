import unittest


EVIL_WIN = 'Battle Result: Evil eradicates all trace of Good'
GOOD_WIN = 'Battle Result: Good triumphs over Evil'
GOOD_AND_EVIL_TIE = 'Battle Result: No victor on this battle field'


GOOD_POINT_MAPPING = {
    0: 1,
    1: 2,
    2: 3,
    3: 3,
    4: 4,
    5: 10,
}

EVIL_POINT_MAPPING = {
    0: 1,
    1: 2,
    2: 2,
    3: 2,
    4: 3,
    5: 5,
    6: 10,
}


def goodVsEvil(good, evil):

    def _get_sum_of_point(score_list, mapping):
        return sum(mapping[index] * int(num) for index, num in enumerate(score_list.split()) if num != '0')

    sum_of_good_point = _get_sum_of_point(good, GOOD_POINT_MAPPING)
    sum_of_evil_point = _get_sum_of_point(evil, EVIL_POINT_MAPPING)

    if sum_of_good_point > sum_of_evil_point:
        return GOOD_WIN
    elif sum_of_evil_point > sum_of_good_point:
        return EVIL_WIN
    else:
        return GOOD_AND_EVIL_TIE
    
    
class TestGoodVsEveil(unittest.TestCase):
    def test_good_vs_evil_when_good_is_win(self):
        good, evil = '0 0 0 0 0 10', '0 1 1 1 1 0 0'
        actual = goodVsEvil(good, evil)
        self.assertEqual(actual, GOOD_WIN)

    def test_good_vs_evil_when_evil_is_win(self):
        good, evil = '1 1 1 1 1 1', '1 1 1 1 1 1 1'
        actual = goodVsEvil(good, evil)
        self.assertEqual(actual, EVIL_WIN)

    def test_good_vs_evil_when_evil_and_good_is_tie(self):
        good, evil = '1 0 0 0 0 0', '1 0 0 0 0 0 0'
        actual = goodVsEvil(good, evil)
        self.assertEqual(actual, GOOD_AND_EVIL_TIE)
