from collections import defaultdict
from itertools import pairwise


# Assumes eulerian path exists (undirected graph)
def hierholzer_undirected(edges: list[list[int]]) -> list[list[int]]:
    adj: defaultdict[int, list[int]] = defaultdict(list)
    degree: defaultdict[int, int] = defaultdict(int)

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Find start node:
    # Eulerian path → exactly 2 odd degree vertices (start & end)
    # Eulerian circuit → all even degree vertices
    start = -1
    odd_nodes = [node for node in degree if degree[node] % 2 == 1]

    if odd_nodes:
        start = odd_nodes[0]
    else:
        start = edges[0][0] if edges else 0

    def dfs(u: int, path_stack: list[int]):
        while adj[u]:
            v = adj[u].pop()
            adj[v].remove(u)  # remove reverse edge
            dfs(v, path_stack)
        path_stack.append(u)

    stack: list[int] = []
    dfs(start, stack)

    path_nodes = stack[::-1]
    return [[x, y] for x, y in pairwise(path_nodes)]
