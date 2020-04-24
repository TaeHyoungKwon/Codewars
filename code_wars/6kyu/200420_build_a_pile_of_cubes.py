import unittest


def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1
    
    
class TestFindNb(unittest.TestCase):
    def test_find_nb_when_n_is_not_exist(self):
        m = 24723578342962
        actual = find_nb(m)
        self.assertEqual(actual, -1)

    def test_find_nb_when_n_is_exist(self):
        m = 1071225
        actual = find_nb(m)
        self.assertEqual(actual, 45)
