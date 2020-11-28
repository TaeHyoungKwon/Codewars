import unittest

BRANCH_TO_GROUND_LENGTH = 400


def sakura_fall(v):
    return BRANCH_TO_GROUND_LENGTH // 5 if v > 0 else 0


class TestSakuraFall(unittest.TestCase):
    def test_sakura_fall(self):
        self.assertEqual(sakura_fall(v=5), 80)

    def test_sakura_fall_with_negative_number(self):
        self.assertEqual(sakura_fall(v=-5), 0)
