import unittest


def parts_sums(ls):
    result = [sum(ls)]
    for item in ls:
        result.append(result[-1]-item)
    return result


class TestSumOfParts(unittest.TestCase):
    def test_should_return_0_in_list_when_given_ls_is_empty_list(self):
        self.assertEqual(parts_sums([]), [0])

    def test_parts_sums(self):
        self.assertEqual(parts_sums([0, 1, 3, 6, 10]), [20, 20, 19, 16, 10, 0])

    def test_parts_sums_case_about_large_number(self):
        self.assertEqual(
            parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]),
            [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0],
        )
