import unittest


def contain_all_rots(strng, arr):
    rotation_list = []
    temp = list(strng)
    for _ in range(len(strng)):
        temp.append(temp.pop(0))
        rotation_list.append("".join(temp))
    return all(rotation_strng in arr for rotation_strng in rotation_list)


class TestContainAllRots(unittest.TestCase):
    def test_contain_should_return_true_when_strng_is_empty_string(self):
        self.assertTrue(contain_all_rots(strng="", arr=[]))
        self.assertTrue(contain_all_rots(strng="", arr=["abcde"]))

    def test_contain_all_rots_should_return_true_on_all_rotation_of_strng_are_included(self):
        self.assertTrue(contain_all_rots(strng="bsjq", arr=["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))

    def test_contain_all_rots_should_return_false_on_all_rotation_of_strng_are_not_included(self):
        self.assertFalse(
            contain_all_rots(
                strng="XjYABhR",
                arr=["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"],
            )
        )
