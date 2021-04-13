import unittest


def all_rationals():
    # BFS로 다시 풀어보기
    yield (1, 1)


class Test(unittest.TestCase):
    def test_should_fail(self):
        self.fail()
