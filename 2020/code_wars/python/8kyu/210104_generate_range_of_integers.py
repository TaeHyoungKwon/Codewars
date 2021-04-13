import unittest


def generate_range(min_, max_, step_):
    return list(range(min_, max_ + 1, step_))


class TestGenerateRange(unittest.TestCase):
    def test_generate_range(self):
        self.assertEqual(generate_range(2, 10, 2), [2, 4, 6, 8, 10])

    def test_generate_range_with_edge_case(self):
        self.assertEqual(generate_range(2, 10, 3), [2, 5, 8])
