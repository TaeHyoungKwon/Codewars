def dfs(graph: list[list[int]], vertex: int, visited: list[bool]):
    visited[vertex] = True
    yield vertex

    for candidate_vertex in graph[vertex]:
        if not visited[candidate_vertex]:
            yield from dfs(graph, candidate_vertex, visited)


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
        " -> ".join(map(str, dfs(graph=graph, vertex=1, visited=[False] * len(graph))))
    )
