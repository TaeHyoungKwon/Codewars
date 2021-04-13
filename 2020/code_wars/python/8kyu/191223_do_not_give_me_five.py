import unittest


def dont_give_me_five(start, end):
    return len([ele for ele in range(start, end + 1) if '5' not in str(ele)])


class TestDontGiveMeFive(unittest.TestCase):
    def test_should_return_count_without_multiple_of_five(self):
        start, end = 4, 17
        result = dont_give_me_five(start, end)
        self.assertEqual(result, 12)

    def test_should_return_43_between_88_and_135(self):
        start, end = 88, 135
        result = dont_give_me_five(start, end)
        self.assertEqual(result, 43)