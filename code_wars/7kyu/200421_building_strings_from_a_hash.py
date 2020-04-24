from collections import OrderedDict
import unittest


def solution(pairs):
    if not pairs:
        return ''

    return ','.join('{} = {}'.format(str(ele), str(pairs[ele])) for ele in sorted(pairs.keys()))


class TestSolution(unittest.TestCase):
    def test_should_return_empty_space_when_given_pairs_is_empty(self):
        self.assertEqual(solution(pairs={}), '')

    def test_pairs(self):
        # Given: Set pairs
        pairs = {'a': 1, 'b': 2}

        # When: Call solution
        actual = solution(pairs)

        # Then: Should return replacement by string
        self.assertEqual(actual, 'a = 1,b = 2')



    def test_pairs_with_numeric(self):
        # Given: Set pairs
        pairs = {0: 'a', 'b': 2}

        # When: Call solution
        actual = solution(pairs)

        # Then: Should return replacement by string
        self.assertEqual(actual, '0 = a,b = 2')