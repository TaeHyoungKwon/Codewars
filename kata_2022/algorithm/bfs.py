from collections import deque


def bfs(graph: list[list[int]], vertex: int, visited: list[bool]):
    queue = deque([vertex])
    visited[vertex] = True

    while queue:
        target_vertex = queue.popleft()
        yield target_vertex

        for candidate_vertex in graph[target_vertex]:
            if not visited[candidate_vertex]:
                queue.append(candidate_vertex)
                visited[candidate_vertex] = True


if __name__ == "__main__":
    graph: list[list[int]] = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7],
    ]
    print(
        " -> ".join(map(str, bfs(graph=graph, vertex=1, visited=[False] * len(graph))))
    )
