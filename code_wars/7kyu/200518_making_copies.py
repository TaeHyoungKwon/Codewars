import unittest
import copy
from unittest.mock import patch, Mock


def copy_list(l):
    if isinstance(l, list):
        return copy.deepcopy(l)
    else:
        raise TypeError
    
    
class TestCopyList(unittest.TestCase):
    def test_copy_list(self):
        l = [1, 2, 3, 4]
        actual = copy_list(l)
        l[1] += 5
        self.assertEqual(actual, [1, 2, 3, 4])

