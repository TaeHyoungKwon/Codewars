import unittest


def check_exam(arr1, arr2):
    exam_result = {
        'o': 0,
        'x': 0,
        'blank': 0,
    }

    for index, ele in enumerate(arr2):
        if ele == arr1[index]:
            exam_result['o'] += 4
        elif ele == '':
            return exam_result['o'] + exam_result['x']
        elif ele != arr1[index]:
            exam_result['x'] -= 1

    return exam_result['o'] + exam_result['x']


class TestCheckExam(unittest.TestCase):
    def test_check_exam(self):
        arr1, arr2 = ["a", "a", "b", "b"], ["a", "c", "b", "d"]
        actual = check_exam(arr1, arr2)
        self.assertEqual(actual, 6)
