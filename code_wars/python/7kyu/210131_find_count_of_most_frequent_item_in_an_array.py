import unittest


def most_frequent_item_count(collection):
    set_collection = set(collection)
    max_count = 0
    for item in set_collection:
        item_count = collection.count(item)
        if item_count > max_count:
            max_count = item_count
    return max_count


class TestMostFrequentItemCount(unittest.TestCase):
    def test_most_frequent_item_count_should_return_0_when_collection_is_empty_list(self):
        self.assertEqual(most_frequent_item_count(collection=[]), 0)

    def test_most_frequent_item_count_common_case_1(self):
        self.assertEqual(most_frequent_item_count(collection=[3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]), 5)

    def test_most_frequent_item_count_common_case_2(self):
        self.assertEqual(most_frequent_item_count(collection=[3, -1, -1]), 2)
