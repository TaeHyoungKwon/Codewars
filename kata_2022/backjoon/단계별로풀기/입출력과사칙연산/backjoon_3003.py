from unittest.mock import patch, Mock


def _input():
    return input()


def solution():
    input_numbers = list(map(int, _input().split()))
    standard_numbers = [1, 1, 2, 2, 2, 8]

    result = []
    for index, standard_number in enumerate(standard_numbers):
        result.append(standard_number - input_numbers[index])

    return result


if __name__ == "__main__":
    print(*solution())


class TestSolution:
    @patch("kata_2022.backjoon.backjoon_3003._input", Mock(return_value="0 1 2 2 2 7"))
    def test_solution_1(self):
        assert solution() == [1, 0, 0, 0, 0, 1]

    @patch("kata_2022.backjoon.backjoon_3003._input", Mock(return_value="2 1 2 1 2 1"))
    def test_solution_2(self):
        assert solution() == [-1, 0, 0, 1, 0, 7]