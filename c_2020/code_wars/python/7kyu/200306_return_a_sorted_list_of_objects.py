import unittest


def sort_list(sort_by, lst):
    return sorted(lst, key=lambda lst: lst[sort_by], reverse=True)


class TestSortList(unittest.TestCase):
    def test_sort_list_should_be_sorted_lst_by_sort_by_desc(self):
        sort_by = "a"
        lst = [{"a": 1, "b": 3}, {"a": 3, "b": 2}, {"a": 2, "b": 40}, {"a": 4, "b": 12}]
        actual = sort_list(sort_by, lst)
        self.assertEqual(actual, [{"a": 4, "b": 12}, {"a": 3, "b": 2}, {"a": 2, "b": 40}, {"a": 1, "b": 3}])
