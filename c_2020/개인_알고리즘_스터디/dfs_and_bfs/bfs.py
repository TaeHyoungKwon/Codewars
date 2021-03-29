import unittest
from collections import deque

from 개인_알고리즘_스터디.dfs_and_bfs.constants import ADJACENCY_LIST


def bfs():
    queue = deque([0])
    visited_vertex = []
    while queue:
        current = queue.pop()
        for neighbor in ADJACENCY_LIST[current]:
            if neighbor not in visited_vertex:
                queue.appendleft(neighbor)
        visited_vertex.append(current)
    return ', '.join(map(str, visited_vertex))


class TestBFS(unittest.TestCase):
    def test_bfs(self):
        self.assertEqual(bfs(), '0, 1, 2, 3, 4, 5, 6')
