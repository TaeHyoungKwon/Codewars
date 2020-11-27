import unittest


def check_exam(arr1, arr2):
    exam_result = {
        'o': 0,
        'x': 0,
    }

    for index, ele in enumerate(arr2):
        if ele == '':
            continue

        if ele == arr1[index]:
            exam_result['o'] += 4
        else:
            exam_result['x'] -= 1

    total = exam_result['o'] + exam_result['x']

    return total if total > 0 else 0


class TestCheckExam(unittest.TestCase):
    def test_check_exam(self):
        arr1, arr2 = ["a", "a", "b", "b"], ["a", "c", "b", "d"]
        actual = check_exam(arr1, arr2)
        self.assertEqual(actual, 6)

    def test_check_exam_with_edge_case(self):
        arr1, arr2 = ["a", "a", "c", "b"], ["a", "a", "b", ""]
        actual = check_exam(arr1, arr2)
        self.assertEqual(actual, 7)
