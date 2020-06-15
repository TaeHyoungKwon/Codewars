import unittest


def twice_as_old(dad_years_old, son_years_old):
    # 문제가 이상함.. ㅠ
    cnt = 0
    for _ in range(max(dad_years_old, son_years_old) + 1):

        if dad_years_old == son_years_old * 2:
            return cnt

        dad_years_old += 1
        son_years_old += 1
        cnt += 1
    else:
        return 0
    
    
class TestTwiceAsOld(unittest.TestCase):
    def test_twice_as_old(self):
        dad_years_old, son_years_old = 36, 7
        actual = twice_as_old(dad_years_old, son_years_old)
        self.assertEqual(actual, 22)

    def test_twice_as_old_second_case(self):
        dad_years_old, son_years_old = 42, 21
        actual = twice_as_old(dad_years_old, son_years_old)
        self.assertEqual(actual, 0)

    def test_twice_as_old_third_case(self):
        dad_years_old, son_years_old = 29, 0
        actual = twice_as_old(dad_years_old, son_years_old)
        self.assertEqual(actual, 29)

    def test_twice_as_old_fourth_case(self):
        dad_years_old, son_years_old = 68, 47
        actual = twice_as_old(dad_years_old, son_years_old)
        self.assertEqual(actual, 29)
