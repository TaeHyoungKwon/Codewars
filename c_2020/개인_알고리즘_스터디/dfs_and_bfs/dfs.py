import unittest

from 개인_알고리즘_스터디.dfs_and_bfs.constants import ADJACENCY_LIST


def dfs():
    stack = [0]
    visited_vertex = []
    while stack:
        current = stack.pop()
        for neighbor in ADJACENCY_LIST[current]:
            if neighbor not in visited_vertex:
                stack.append(neighbor)
        visited_vertex.append(current)
    return ', '.join(map(str, visited_vertex))


class TestDfs(unittest.TestCase):
    def test_dfs(self):
        self.assertEqual(dfs(), '0, 2, 5, 4, 6, 1, 3')
