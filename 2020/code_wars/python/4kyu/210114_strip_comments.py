import unittest


def solution(string, markers):
    result = []
    for line in string.split('\n'):
        temp = ''
        for char in line:
            if char in markers:
                temp = line[:line.index(char)].strip()
                break
            else:
                temp += char
        result.append(temp)
    return '\n'.join(result)


class TestSolution(unittest.TestCase):
    def test_solution(self):
        string, markers = "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
        actual = solution(string, markers)
        self.assertEqual(actual, "apples, pears\ngrapes\nbananas")

    def test_solution_case_2(self):
        string, markers = "a #b\nc\nd $e f g", ["#", "$"]
        actual = solution(string, markers)
        self.assertEqual(actual, "a\nc\nd")
