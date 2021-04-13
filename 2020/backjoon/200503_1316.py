import unittest
from unittest.mock import patch, Mock


def input_():
    return [input() for _ in range(int(input()))]


def solution():
    return sum(1 for word in input_() if word == "".join(sorted(word, key=word.find )))


if __name__ == "__main__":
    print(solution())


class TestSolution(unittest.TestCase):
    @patch("200503_1316.input_", Mock(return_value=["happy", "new", "year"]))
    def test_solution(self):
        actual = solution()
        self.assertEqual(actual, 3)
