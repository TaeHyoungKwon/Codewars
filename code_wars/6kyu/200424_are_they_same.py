import unittest


def comp(array1, array2):
    if not (array1 or array2):
        return False
    return sorted(list(map(lambda x: x ** 2, array1))) == sorted(array2)


class TestComp(unittest.TestCase):
    def test_should_return_false_when_given_array_is_none(self):
        array1 = None
        array2 = [1, 2, 3]
        result = comp(array1, array2)
        self.assertEqual(result, False)

