import unittest


STOCK = {"못": 125, "나사못": 35, "나비너트": 8, "와셔": 24}
ORDER = ["나사못", "나비너트", "클립"]


def get_batches(count, size):
    return count // size


def solution_with_for_loop():
    """
    책에 나와있는 코드 그대로
    """
    result = {}
    for name in ORDER:
        count = STOCK.get(name, 0)
        batches = get_batches(count, 8)
        if batches:
            result[name] = batches
    return result


def solution_with_dict_comprehension():
    return {name: get_batches(STOCK.get(name, 0), 8) for name in ORDER if get_batches(STOCK.get(name, 0), 8)}


def solution():
    return {name: batches for name in ORDER if (batches := get_batches(STOCK.get(name, 0), 8))}


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution()["나사못"], 4)
        self.assertEqual(solution()["나비너트"], 1)
