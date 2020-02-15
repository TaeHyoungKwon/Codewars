from collections import Counter
import unittest


def odd_one_out(s):
    # 답보고 품
    d = Counter(reversed(s))
    return [x for x in d if d[x] % 2][::-1]
#     return [ele for idx, ele in enumerate(s)
#             if check_last_index_of_ele_is_equal(s, ele, idx) and is_odd_num(s, ele)]
#
#
# def is_odd_num(s, ele):
#     count = Counter(s)
#     return count[ele] % 2 != 0
#
#
# def check_last_index_of_ele_is_equal(s, ele, idx):
#     return s.rindex(ele) == idx


class TestOddOneOut(unittest.TestCase):
    def _set_s_and_call_odd_one_out(self, s):
        return odd_one_out(s)

    def test_all_distinct_string(self):
        # Then: All distinct string 'code wars' should be ['c', 'o', 'd', 'e', ' ', 'w', 'a', 'r', 's']
        self.assertEqual(
            self._set_s_and_call_odd_one_out('code wars'),
            ['c', 'o', 'd', 'e', ' ', 'w', 'a', 'r', 's']
        )

    def test_completed_paried_string(self):
        # Then: All distinct string 'aabbccdd' should be empty list
        self.assertEqual(
            self._set_s_and_call_odd_one_out('aabbccdd'),
            []
        )

    def test_should_return_char_e_when_given_s_is_racecar(self):
        # Then: All distinct string 'racecar' should be ['e']
        self.assertEqual(
            self._set_s_and_call_odd_one_out('racecar'),
            ['e']
        )

    def test_should_return_heWrld_by_list_when_given_s_is_Hello_World(self):
        # Then: All distinct string 'racecar' should be ['e']
        self.assertEqual(
            self._set_s_and_call_odd_one_out('Hello World'),
            ["H", "e", " ", "W", "r", "l", "d"]
        )
