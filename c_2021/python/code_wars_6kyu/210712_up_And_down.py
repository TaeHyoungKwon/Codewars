import unittest


def arrange(strng):
    # 못 품`
    split_strng = result = strng.split()
    prev = ""
    result = list(map(str.lower, result))
    return " ".join(ele.upper() if index % 2 else ele for index, ele in enumerate(_arrange(prev, result, split_strng)))


def _arrange(prev, result, split_strng):
    for index, current in enumerate(split_strng):
        if index == 0:
            prev = current
            continue
        if index % 2:
            if len(prev) <= len(current):
                prev = current
            else:
                result.remove(current.lower())
                result.insert(index - 1, current.lower())
        else:
            if len(prev) >= len(current):
                prev = current
            else:
                result.remove(current.lower())
                result.insert(index - 1, current.lower())
    return result


class TestArrange(unittest.TestCase):
    def test_arrange(self):
        self.assertEqual(arrange(strng="who hit retaining The That a we taken"), "who RETAINING hit THAT a THE we TAKEN")
        