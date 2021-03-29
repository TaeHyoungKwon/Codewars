from collections import deque

N, M, V = map(int, input().split())

VERTEX_LIST = [ele for ele in range(1, N + 2)]

EDGE_LIST = []
for _ in range(M):
    EDGE_LIST.append(list(map(int, input().split())))

BFS_ADJACENCY_LIST = [[] for _ in VERTEX_LIST]
DFS_ADJACENCY_LIST = [[] for _ in VERTEX_LIST]

for edge in EDGE_LIST:
    BFS_ADJACENCY_LIST[edge[0]].append(edge[1])
    BFS_ADJACENCY_LIST[edge[0]].sort()
    BFS_ADJACENCY_LIST[edge[1]].append(edge[0])
    BFS_ADJACENCY_LIST[edge[1]].sort()

for edge in EDGE_LIST:
    DFS_ADJACENCY_LIST[edge[0]].append(edge[1])
    #DFS_ADJACENCY_LIST[edge[0]].sort(reverse=True)
    DFS_ADJACENCY_LIST[edge[1]].append(edge[0])
    #DFS_ADJACENCY_LIST[edge[1]].sort(reverse=True)


def dfs(start, visited):
    stack = [V]
    visited_vertex = []
    current = stack.pop()
    for neighbor in DFS_ADJACENCY_LIST[current]:
        if neighbor not in visited_vertex and neighbor not in stack:
            dfs(neighbor, visited_vertex)
    return ' '.join(map(str, visited_vertex))


def bfs():
    queue = deque([V])
    visited_vertex = []
    while queue:
        current = queue.popleft()
        for neighbor in BFS_ADJACENCY_LIST[current]:
            if neighbor not in visited_vertex and neighbor not in queue:
                queue.append(neighbor)
        visited_vertex.append(current)
    return ' '.join(map(str, visited_vertex))


if __name__ == '__main__':
    print(dfs(V, []))
    print(bfs())
