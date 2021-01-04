import unittest


def triple_trouble(one, two, three):
    return ''.join(''.join(ele) for ele in zip(one, two, three))
    
    
class TestTripleTrouble(unittest.TestCase):
    def test_triple_trouble(self):
        one, two, three = "aaa", "bbb", "ccc"
        actual = triple_trouble(one, two, three)
        self.assertEqual(actual, 'abcabcabc')
