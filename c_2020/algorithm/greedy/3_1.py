import unittest


def solution(n, m, k, data):
    data = sorted(data, reverse=True)
    result = 0
    index = 0
    while index < m:
        for _ in range(k):
            if index == m:
                break
            result += data[0]
            index += 1
        if index == m:
            break
        result += data[1]
        index += 1
    return result


class TestSolution(unittest.TestCase):
    def test_solution_case_1(self):
        # n = 배열의 크기
        # m = 숫자가 더해지는 횟수
        # k = 최대 더해질 수 있는 횟수
        # data = 배열 크기에 맞는 숫자 리스트
        n, m, k = 2, 1, 1
        data = [1, 2]
        actual = solution(n, m, k, data)
        self.assertEqual(actual, 2)

    def test_solution_case_2(self):
        n, m, k = 2, 2, 2
        data = [2, 2]
        actual = solution(n, m, k, data)
        self.assertEqual(actual, 4)

    def test_solution_case_3(self):
        n, m, k = 5, 8, 3
        data = [2, 4, 5, 4, 6]
        actual = solution(n, m, k, data)
        self.assertEqual(actual, 46)

    def test_solution_case_4(self):
        n, m, k = 5, 7, 2
        data = [3, 4, 3, 4, 3]
        actual = solution(n, m, k, data)
        self.assertEqual(actual, 28)
