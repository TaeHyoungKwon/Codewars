import unittest


def group_by_commas(n):
    result = []
    temp = ""
    reversed_ = str(n)[::-1]
    for index, ele in enumerate(reversed_):
        if index > 2 and index % 3 == 0:
            result.append(temp[::-1])
            temp = ""
        temp += ele
    result.append(temp[::-1])
    return ",".join(result[::-1])


class TestGroupByCommas(unittest.TestCase):
    def test_group_by_commas_n_is_1(self):
        self.assertEqual(group_by_commas(n=1), "1")

    def test_group_by_commas_n_is_10(self):
        self.assertEqual(group_by_commas(n=10), "10")

    def test_group_by_commas_n_is_100(self):
        self.assertEqual(group_by_commas(n=100), "100")

    def test_group_by_commas_n_is_1000(self):
        self.assertEqual(group_by_commas(n=1000), "1,000")

    def test_group_by_commas_n_is_10000(self):
        self.assertEqual(group_by_commas(n=10000), "10,000")

    def test_group_by_commas_n_is_100000(self):
        self.assertEqual(group_by_commas(n=100000), "100,000")

    def test_group_by_commas_n_is_35235235(self):
        self.assertEqual(group_by_commas(n=35235235), "35,235,235")
