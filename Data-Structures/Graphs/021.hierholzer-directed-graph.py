from collections import defaultdict
from itertools import pairwise


# Assumes eulerian path exists (directed graph)
def hierholzer(edges: list[list[int]]) -> list[list[int]]:
    adj: defaultdict[int, list[int]] = defaultdict(list)
    indegree: defaultdict[int, int] = defaultdict(int)
    outdegree: defaultdict[int, int] = defaultdict(int)

    for u, v in edges:
        adj[u].append(v)
        outdegree[u] += 1
        indegree[v] += 1

    start = -1
    for node in adj:
        if outdegree[node] - indegree[node] == 1:
            start = node
            break

    if start == -1:
        start = edges[0][0] if edges else 0

    def dfs(u: int, path_stack: list[int]):
        while adj[u]:
            v = adj[u].pop()
            dfs(v, path_stack)
        path_stack.append(u)

    stack: list[int] = []
    dfs(start, stack)

    path_nodes = stack[::-1]
    return [[x, y] for x, y in pairwise(path_nodes)]
