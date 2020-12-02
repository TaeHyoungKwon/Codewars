import unittest

SON_CONGRATURATION_MSG = 'Congratulations! You\'re going to have a son.'
DAUGHTER_CONGRATURATION_MSG = 'Congratulations! You\'re going to have a daughter.'


def chromosome_check(sperm):
    return SON_CONGRATURATION_MSG if sperm.count('X') == 1 else DAUGHTER_CONGRATURATION_MSG
    
    
class TestChromosomeCheck(unittest.TestCase):
    def test_chromosome_check_with_son(self):
        self.assertEqual(chromosome_check('XY'), SON_CONGRATURATION_MSG)

    def test_chromosome_check_with_daughter(self):
        self.assertEqual(chromosome_check('XX'), DAUGHTER_CONGRATURATION_MSG)
