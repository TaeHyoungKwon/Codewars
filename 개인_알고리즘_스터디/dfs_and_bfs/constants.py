VERTEX_LIST = [ele for ele in range(7)]
EDGE_LIST = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4), (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]

ADJACENCY_LIST = [[] for _ in VERTEX_LIST]

for edge in EDGE_LIST:
    ADJACENCY_LIST[edge[0]].append(edge[1])
