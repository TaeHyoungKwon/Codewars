import unittest


def save(sizes, hd):
    cnt = 0
    result = 0
    for ele in sizes:
        result += ele
        if result <= hd:
            cnt += 1
    return cnt
    
    
class TestSave(unittest.TestCase):
    def test_save(self):
        sizes, hd = [4, 4, 4, 3, 3], 12
        actual = save(sizes, hd)
        self.assertEqual(actual, 3)
