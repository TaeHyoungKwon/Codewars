import unittest


def partlist(arr):
    return [(' '.join(arr[:idx + 1]), ' '.join(arr[idx + 1:])) for idx in range(len(arr) -1)]
    
    
class TestPartList(unittest.TestCase):
    def test_should_fail(self):
        arr = ["I", "wish", "I", "hadn't", "come"]
        actual = partlist(arr)
        self.assertEqual(actual, [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"), ("I wish I hadn't", "come")])
