from itertools import groupby
import unittest


def longest(s):
    # 나중에 다시
    result = []
    temp = []
    prev_key = ""
    initial = False
    for index, (key, group) in enumerate(groupby(s)):
        if index == 0:
            temp.append("".join(group))
            continue
        if prev_key < key:
            temp.append("".join(group))
        else:
            result.append("".join(temp))
            temp = []
            initial = True
        prev_key = key
    print(result)
    return
    
    
class TestLongest(unittest.TestCase):
    def test_longest(self):
        self.assertEqual(longest(s='asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')
